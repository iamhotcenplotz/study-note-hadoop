# Hadoop Cluster yarn-site config

```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<configuration>

<!-- Site specific YARN configuration properties -->
        <!-- shuffle -->
        <property>
                <name>yarn.nodemanager.aux-services</name>
                <value>mapreduce_shuffle</value>
        </property>

        <!-- resource manager address  -->
        <property>
                <name>yarn.resourcemanager.hostname</name>
                <value>server2</value>
        </property>
        
        <!--  -->
        <property>
                <name>yarn.log-aggregation-enable</name>
                <value>true</value>
        </property>
        
        <!--  -->
        <property>
                <name>yarn.log.server.url</name>
                <value>http://server2:19888/jobhistory/logs</value>
        </property>
        
        <!--  -->
        <property>
                <name>yarn.log-aggregation.retain-seconds</name>
                <value>604800</value>
        </property>
    
        <!-- new for server -->
        <property>
                <name>yarn.resourcemanager.scheduler.class</name>
                <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>
        </property>
        <property>
                <!-- 1-2 *1 + (2*4)*3 ~ 14 Threads ~~ 5 -->
                <name>yarn.resourcemanager.scheduler.client.thread-count</name>
                <value>5</value>
        </property>
    
        <property>
                <name>yarn.nodemanager.resource.detect-hardware-capabilities</name>
                <value>false</value>
        </property>
        
        <property>
                <name>yarn.nodemanager.resource.count-logical-processors-as-cores</name>
                <value>true</value>
        </property>
        
        <property>
                <name>yarn.nodemanager.resource.pcores-vcores-multiplier</name>
                <value>2.0</value>
        </property>
    
        <property>
                <name>yarn.nodemanager.resource.memory-mb</name>
                <value>4096</value>
        </property>
    
        <property>
                <name>yarn.nodemanager.resource.cpu-vcores</name>
                <value>2</value>
        </property>
    
        <property>
                <name>yarn.scheduler.minimum-allocation-mb</name>
                <value>1024</value>
        </property>
    
        <property>
                <name>yarn.scheduler.maximum-allocation-mb</name>
                <value>3072</value>
        </property>
    
        <property>
                <name>yarn.scheduler.minimum-allocation-vcores</name>
                <value>1</value>
        </property>
    
        <property>
                <name>yarn.scheduler.maximum-allocation-vcores</name>
                <value>1</value>
        </property>
    
        <property>
                <name>yarn.nodemanager.vmem-check-enabled</name>
                <value>false</value>
        </property>
        
        <property>
                <name>yarn.nodemanager.vmem-pmem-ratio</name>
                <value>2.1</value>
        </property>

</configuration>


```