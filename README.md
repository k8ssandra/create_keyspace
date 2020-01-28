This is a small Python script that creates a keyspace. It is primarily intended to be run in a container.

I have written this for [reaper-operator](https://github.com/jsanda/reaper-operator). All schema initialization except for creating the keyspace is done by [Reaper](http://cassandra-reaper.io) itself.

The intent is for the operator to run this as a k8s job; however, it can also be run on its own or in a container outside of Kubernetes.

The script requires three environment variables to be set:

**KEYSPACE**

The name of the keyspace to create.

**CONTACT_POINTS**

A list of node hostnames or IP addresses with which to create initial connections. In Kubernetes the headless service for the Cassandra statefulset can be used instead.

**REPLICATION**
The replication settings, e.g., 

```
{'class': 'NetworkTopologyStrategy', 'dc1': 3}
