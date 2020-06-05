import sys
import os
import json
import logging
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

logger = logging.getLogger('init_keyspace')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

def getenv(name):
  value = os.getenv(name)
  if not value:
    raise Exception("The environment variable {0} is undefined".format(name))
  return str(value)

def create_table(table_name, table_def):
  logger.info("Creating {}.{} table".format(keyspace, table_name))
  session.execute("CREATE TABLE {}.{} {}".format(keyspace, table_name, table_def)

keyspace = getenv("KEYSPACE")
contact_points = getenv("CONTACT_POINTS").split(",")
replication = getenv("REPLICATION")

logger.info("keyspace = %s", keyspace)
logger.info("contact_points = %s", contact_points)
logger.info("replication = %s", replication)

auth_provider = PlainTextAuthProvider(username="cassandra", password="cassandra")
cluster = Cluster(contact_points, auth_provider=auth_provider)
session = cluster.connect()
session.execute("CREATE KEYSPACE IF NOT EXISTS {0} WITH REPLICATION = {1}".format(keyspace, replication))

create_table("schema_migration" "(applied_successful boolean, version int, script_name varchar, script text, executed_at timestamp, PRIMARY KEY (applied_successful, version))")
create_table("schema_migration_leader", "(keyspace_name text, leader uuid, took_lead_at timestamp, leader_hostname text, PRIMARY KEY (keyspace_name))")
