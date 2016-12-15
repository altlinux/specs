Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
BuildRequires: /usr/bin/openssl bzlib-devel gcc-c++ java-devel-default libcurl-devel rpm-build-java
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires: zlib-devel
BuildRequires: avro-maven-plugin
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hadoop
%define version 2.4.1
%global _hardened_build 1

# libhdfs is only supported on intel architectures atm.
%ifarch %ix86 x86_64
%global package_libhdfs 1
%else
%global package_libhdfs 0
%endif

%global commit 9e2ef43a240fb0f603d8c384e501daec11524510
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global hadoop_version %{version}
%global hdfs_services hadoop-zkfc.service hadoop-datanode.service hadoop-secondarynamenode.service hadoop-namenode.service hadoop-journalnode.service
%global mapreduce_services hadoop-historyserver.service
%global yarn_services hadoop-proxyserver.service hadoop-resourcemanager.service hadoop-nodemanager.service hadoop-timelineserver.service

# Filter out undesired provides and requires
%global __requires_exclude_from ^%{_libdir}/%{name}/libhadoop.so$
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$

Name:   hadoop
Version: 2.4.1
Release: alt2_23jpp8
Summary: A software platform for processing vast amounts of data
# The BSD license file is missing
# https://issues.apache.org/jira/browse/HADOOP-9849
License: ASL 2.0 and BSD
URL: http://hadoop.apache.org
Source0: https://github.com/apache/hadoop-common/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1: %{name}-layout.sh
Source2: %{name}-hdfs.service.template
Source3: %{name}-mapreduce.service.template
Source4: %{name}-yarn.service.template
Source6: %{name}.logrotate
Source8: %{name}-core-site.xml
Source9: %{name}-hdfs-site.xml
Source10: %{name}-mapred-site.xml
Source11: %{name}-yarn-site.xml
Source12: %{name}-httpfs.sysconfig
Source13: hdfs-create-dirs
Source14: %{name}-tomcat-users.xml
# This patch includes the following upstream tickets:
# https://issues.apache.org/jira/browse/HADOOP-9613
# https://issues.apache.org/jira/browse/HDFS-5411
# https://issues.apache.org/jira/browse/HADOOP-10068
# https://issues.apache.org/jira/browse/HADOOP-10075
# https://issues.apache.org/jira/browse/HADOOP-10076
Patch0: %{name}-fedora-integration.patch
# Fedora packaging guidelines for JNI library loading
Patch2: %{name}-jni-library-loading.patch
# Clean up warnings with maven 3.0.5
Patch3: %{name}-maven.patch
# Don't download tomcat
Patch4: %{name}-no-download-tomcat.patch
# Use dlopen to find libjvm.so
Patch5: %{name}-dlopen-libjvm.patch
# Update to Guava 17.0
Patch7: %{name}-guava.patch
# Update to Netty 3.6.6-Final
Patch8: %{name}-netty-3-Final.patch
# Remove problematic issues with tools.jar
Patch9: %{name}-tools.jar.patch
# Workaround for bz1012059
Patch10: %{name}-build.patch
# Build with hard-float on ARMv7
Patch12: %{name}-armhfp.patch

# fix Jersey1 support
Patch13: hadoop-2.4.1-jersey1.patch
# fix java8 doclint
Patch14: hadoop-2.4.1-disable-doclint.patch
# fix exception org.jets3t.service.S3ServiceException is never thrown in body of corresponding try statement
Patch15: hadoop-2.4.1-jets3t0.9.3.patch
# add some servlet3.1 missing methods
Patch16: hadoop-2.4.1-servlet-3.1-api.patch
# Adapt to the new BookKeeper ZkUtils API
Patch17: hadoop-2.4.1-new-bookkeeper.patch
# Fix POM warnings which become errors in newest Maven
Patch18: fix-pom-errors.patch

# This is not a real BR, but is here because of rawhide shift to eclipse
# aether packages which caused a dependency of a dependency to not get
# pulled in.
BuildRequires: aether

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: aopalliance
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-configuration
BuildRequires: apache-commons-daemon
BuildRequires: apache-commons-el
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-math
BuildRequires: apache-commons-net
BuildRequires: apache-rat-plugin
BuildRequires: atinject
BuildRequires: avalon-framework
BuildRequires: avalon-logkit
BuildRequires: avro
BuildRequires: avro-maven-plugin
BuildRequires: bookkeeper-java
BuildRequires: cglib
BuildRequires: checkstyle
BuildRequires: chrpath
BuildRequires: ctest cmake
BuildRequires: ecj >= 1:4.2.1
BuildRequires: libfuse-devel
BuildRequires: fusesource-pom
BuildRequires: geronimo-jms
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jsp
BuildRequires: glassfish-jsp-api
BuildRequires: google-guice
BuildRequires: grizzly
BuildRequires: guava
BuildRequires: guice-servlet
BuildRequires: hamcrest
BuildRequires: hawtjni
BuildRequires: hsqldb
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: istack-commons
BuildRequires: jackson
BuildRequires: jakarta-commons-httpclient
BuildRequires: java-base64
BuildRequires: java-devel
BuildRequires: java-xmlbuilder
BuildRequires: javamail
BuildRequires: maven-local
BuildRequires: jdiff
BuildRequires: jersey1
BuildRequires: jersey1-contribs
BuildRequires: jets3t
BuildRequires: jettison
BuildRequires: jetty8
BuildRequires: jsch
BuildRequires: json_simple
BuildRequires: jspc
BuildRequires: jsr-305
BuildRequires: jsr-311
BuildRequires: junit
BuildRequires: jzlib
BuildRequires: leveldbjni
BuildRequires: groovy18
BuildRequires: log4j12
BuildRequires: maven-antrun-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-exec
BuildRequires: maven-plugin-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-war-plugin
BuildRequires: metrics
BuildRequires: mockito
BuildRequires: native-maven-plugin
BuildRequires: netty3
BuildRequires: objectweb-asm
BuildRequires: objenesis >= 1.2
BuildRequires: libssl-devel
BuildRequires: paranamer
BuildRequires: protobuf-compiler
BuildRequires: protobuf-java
BuildRequires: relaxngDatatype
BuildRequires: servlet3
BuildRequires: slf4j
BuildRequires: libsnappy-devel
BuildRequires: snappy-java
BuildRequires: journalctl libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-services systemd-utils
BuildRequires: tomcat
BuildRequires: tomcat-el-3.0-api
BuildRequires: tomcat
BuildRequires: tomcat-servlet-3.1-api
BuildRequires: txw2
BuildRequires: xmlenc
BuildRequires: znerd-oss-parent
BuildRequires: zookeeper-java > 3.4.5
# For tests
BuildRequires: jersey1-test-framework
Source44: import.info
Patch33: hadoop-2.4.1-alt-sh-syntax.patch

%description
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

%package client
Group: Development/Java
Summary: Libraries for Apache Hadoop clients
BuildArch: noarch
Requires: %{name}-common = %{version}
Requires: %{name}-hdfs = %{version}
Requires: %{name}-mapreduce = %{version}
Requires: %{name}-yarn = %{version}

%description client
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package provides libraries for Apache Hadoop clients.

%package common
Group: Development/Java
Summary: Common files needed by Apache Hadoop daemons
BuildArch: noarch
Requires(pre): /usr/sbin/useradd
Obsoletes: %{name}-javadoc < 2.4.1-22%{?dist}

# These are required to meet the symlinks for the classpath
Requires: antlr-tool
Requires: apache-commons-beanutils
Requires: avalon-framework
Requires: avalon-logkit
Requires: checkstyle
Requires: coreutils
Requires: geronimo-jms
Requires: glassfish-jaxb
Requires: glassfish-jsp
Requires: glassfish-jsp-api
Requires: istack-commons
Requires: jakarta-commons-httpclient
Requires: java-base64
Requires: java-xmlbuilder
Requires: javamail
Requires: jettison
Requires: jetty8
Requires: jsr-311
Requires: mockito
Requires: objectweb-asm
Requires: objenesis
Requires: paranamer
Requires: relaxngDatatype
Requires: servlet3
Requires: snappy-java
Requires: txw2
Requires: which

%description common
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package contains common files and utilities needed by other Apache
Hadoop modules.

%package common-native
Group: Development/Java
Summary: The native Apache Hadoop library file
Requires: %{name}-common = %{version}

%description common-native
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package contains the native-hadoop library

%if %{package_libhdfs}
%package devel
Group: Development/Java
Summary: Headers for Apache Hadoop
Requires: libhdfs%{?_isa} = %{version}

%description devel
Header files for Apache Hadoop's hdfs library and other utilities
%endif

%package hdfs
Group: Development/Java
Summary: The Apache Hadoop Distributed File System
BuildArch: noarch
Requires: apache-commons-daemon-jsvc
Requires: %{name}-common = %{version}

%description hdfs
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

The Hadoop Distributed File System (HDFS) is the primary storage system
used by Apache Hadoop applications.

%if %{package_libhdfs}
%package hdfs-fuse
Group: Development/Java
Summary: Allows mounting of Apache Hadoop HDFS
Requires: fuse
Requires: libhdfs%{?_isa} = %{version}
Requires: %{name}-common = %{version}
Requires: %{name}-hdfs = %{version}
Requires: %{name}-mapreduce = %{version}
Requires: %{name}-yarn = %{version}

%description hdfs-fuse
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package provides tools that allow HDFS to be mounted as a standard
file system through fuse.
%endif

%package httpfs
Group: Development/Java
Summary: Provides web access to HDFS
BuildArch: noarch
Requires: apache-commons-dbcp
Requires: ecj >= 1:4.2.1
Requires: json_simple
Requires: tomcat
Requires: tomcat-lib
Requires: tomcat-native

%description httpfs
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package provides a server that provides HTTP REST API support for
the complete FileSystem/FileContext interface in HDFS.

%if %{package_libhdfs}
%package -n libhdfs
Group: Development/Java
Summary: The Apache Hadoop Filesystem Library
Requires: %{name}-hdfs = %{version}
Requires: liblzo2

%description -n libhdfs
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package provides the Apache Hadoop Filesystem Library.
%endif

%package mapreduce
Group: Development/Java
Summary: Apache Hadoop MapReduce (MRv2)
BuildArch: noarch
Requires: %{name}-common = %{version}

%description mapreduce
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package provides Apache Hadoop MapReduce (MRv2).

%package mapreduce-examples
Group: Development/Java
Summary: Apache Hadoop MapReduce (MRv2) examples
BuildArch: noarch
Requires: hsqldb

%description mapreduce-examples
This package contains mapreduce examples.

%package maven-plugin
Group: Development/Java
Summary: Apache Hadoop maven plugin
BuildArch: noarch
Requires: maven

%description maven-plugin
The Apache Hadoop maven plugin

%package tests
Group: Development/Java
Summary: Apache Hadoop test resources
BuildArch: noarch
Requires: %{name}-common = %{version}
Requires: %{name}-hdfs = %{version}
Requires: %{name}-mapreduce = %{version}
Requires: %{name}-yarn = %{version}

%description tests
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package contains test related resources for Apache Hadoop.

%package yarn
Group: Development/Java
Summary: Apache Hadoop YARN
BuildArch: noarch
Requires: %{name}-common = %{version}
Requires: %{name}-mapreduce = %{version}
Requires: aopalliance
Requires: atinject
Requires: hamcrest
Requires: hawtjni
Requires: leveldbjni

%description yarn
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package contains Apache Hadoop YARN.

%package yarn-security
Group: Development/Java
Summary: The ability to run Apache Hadoop YARN in secure mode
Requires: %{name}-yarn = %{version}

%description yarn-security
Apache Hadoop is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each
offering local computation and storage.

This package contains files needed to run Apache Hadoop YARN in secure mode.

%prep
%setup -q -n %{name}-common-%{commit}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%if !%{package_libhdfs}
# rollback non-applicable patch after autosetup applies all patches
%patch5 -p1 -R
%endif

%pom_xpath_set "pom:properties/pom:protobuf.version" 2.6.1 hadoop-project
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions/pom:execution[pom:phase='test-compile']" "<id>default-jar</id>"  hadoop-yarn-project/hadoop-yarn/hadoop-yarn-applications/hadoop-yarn-applications-distributedshell

# Remove the maven-site-plugin.  It's not needed
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-site-plugin hadoop-common-project/hadoop-auth
%pom_remove_plugin :maven-site-plugin hadoop-hdfs-project/hadoop-hdfs-httpfs

# Remove the findbugs-maven-plugin.  It's not needed and isn't available
%pom_remove_plugin :findbugs-maven-plugin hadoop-hdfs-project/hadoop-hdfs-httpfs
%pom_remove_plugin :findbugs-maven-plugin hadoop-hdfs-project/hadoop-hdfs/src/contrib/bkjournal
%pom_remove_plugin :findbugs-maven-plugin hadoop-mapreduce-project/hadoop-mapreduce-client
%pom_remove_plugin :findbugs-maven-plugin hadoop-mapreduce-project/hadoop-mapreduce-examples
%pom_remove_plugin :findbugs-maven-plugin hadoop-mapreduce-project
%pom_remove_plugin :findbugs-maven-plugin hadoop-project-dist
%pom_remove_plugin :findbugs-maven-plugin hadoop-project
%pom_remove_plugin :findbugs-maven-plugin hadoop-tools/hadoop-rumen
%pom_remove_plugin :findbugs-maven-plugin hadoop-tools/hadoop-streaming
%pom_remove_plugin :findbugs-maven-plugin hadoop-yarn-project/hadoop-yarn
%pom_remove_plugin :findbugs-maven-plugin hadoop-yarn-project

# Remove the maven-project-info-reports plugin.  It's not needed and isn't available
%pom_remove_plugin :maven-project-info-reports-plugin hadoop-common-project/hadoop-auth
%pom_remove_plugin :maven-project-info-reports-plugin hadoop-hdfs-project/hadoop-hdfs-httpfs
%pom_remove_plugin :maven-project-info-reports-plugin hadoop-project

# Remove the maven-checkstyle plugin.  It's not needed and isn't available
%pom_remove_plugin :maven-checkstyle-plugin hadoop-project-dist
%pom_remove_plugin :maven-checkstyle-plugin hadoop-project
%pom_remove_plugin :maven-checkstyle-plugin hadoop-tools/hadoop-distcp

# Disable the hadoop-minikdc module due to missing deps
%pom_disable_module hadoop-minikdc hadoop-common-project
%pom_remove_dep :hadoop-minikdc hadoop-common-project/hadoop-auth
%pom_remove_dep :hadoop-minikdc hadoop-project
%pom_remove_dep :hadoop-minikdc hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-tests
rm -f hadoop-common-project/hadoop-auth/src/test/java/org/apache/hadoop/security/authentication/client/TestKerberosAuthenticator.java
rm -f hadoop-common-project/hadoop-auth/src/test/java/org/apache/hadoop/security/authentication/server/TestKerberosAuthenticationHandler.java
rm -f hadoop-common-project/hadoop-auth/src/test/java/org/apache/hadoop/security/authentication/server/TestAltKerberosAuthenticationHandler.java
rm -f hadoop-common-project/hadoop-auth/src/test/java/org/apache/hadoop/security/authentication/server/TestKerberosAuthenticationHandler.java
rm -f hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-tests/src/test/java/org/apache/hadoop/yarn/server/TestContainerManagerSecurity.java

%if 0%{?fedora} > 25
# Disable hadoop-pipes, because it needs upstream patching for Openssl 1.1.0
%pom_disable_module hadoop-pipes hadoop-tools
%pom_remove_dep :hadoop-pipes hadoop-tools/hadoop-tools-dist
%endif

# Add dependencies for timeline service
%pom_add_dep org.iq80.leveldb:leveldb hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-applicationhistoryservice
%pom_add_dep org.fusesource.hawtjni:hawtjni-runtime hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-applicationhistoryservice

# Fix scope on hadoop-common:test-jar
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='hadoop-common' and pom:type='test-jar']/pom:scope" test hadoop-tools/hadoop-openstack

# Modify asm version to version 5.0.2 and groupId to org.ow2.asm
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='asm']/pom:version" 5.0.2 hadoop-project
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='asm']/pom:groupId" org.ow2.asm hadoop-project


# War files we don't want
%mvn_package :%{name}-auth-examples __noinstall
%mvn_package :%{name}-hdfs-httpfs __noinstall

# Parts we don't want to distribute
%mvn_package :%{name}-assemblies __noinstall

# Workaround for bz1012059
%mvn_package :%{name}-project-dist __noinstall

# Create separate file lists for packaging
%mvn_package :::tests: %{name}-tests
%mvn_package :%{name}-*-tests::{}: %{name}-tests
%mvn_package :%{name}-client*::{}: %{name}-client
%mvn_package :%{name}-hdfs*::{}: %{name}-hdfs
%mvn_package :%{name}-mapreduce-examples*::{}: %{name}-mapreduce-examples
%mvn_package :%{name}-mapreduce*::{}: %{name}-mapreduce
%mvn_package :%{name}-archives::{}: %{name}-mapreduce
%mvn_package :%{name}-datajoin::{}: %{name}-mapreduce
%mvn_package :%{name}-distcp::{}: %{name}-mapreduce
%mvn_package :%{name}-extras::{}: %{name}-mapreduce
%mvn_package :%{name}-gridmix::{}: %{name}-mapreduce
%mvn_package :%{name}-openstack::{}: %{name}-mapreduce
%mvn_package :%{name}-rumen::{}: %{name}-mapreduce
%mvn_package :%{name}-sls::{}: %{name}-mapreduce
%mvn_package :%{name}-streaming::{}: %{name}-mapreduce
%if 0%{?fedora} <= 25
%mvn_package :%{name}-pipes::{}: %{name}-mapreduce
%endif
%mvn_package :%{name}-tools*::{}: %{name}-mapreduce
%mvn_package :%{name}-maven-plugins::{}: %{name}-maven-plugin
%mvn_package :%{name}-minicluster::{}: %{name}-tests
%mvn_package :%{name}-yarn*::{}: %{name}-yarn

# Jar files that need to be overridden due to installation location
%mvn_file :%{name}-common::tests: %{name}/%{name}-common
%patch33 -p0
%pom_add_dep org.fusesource.leveldbjni:leveldbjni hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-applicationhistoryservice

%build
# increase JVM memory limits to avoid OOM during build
%ifarch s390x ppc64le
export MAVEN_OPTS="-Xms2048M -Xmx4096M"
%endif
%mvn_build -j -- -Drequire.snappy=true -Dcontainer-executor.conf.dir=%{_sysconfdir}/%{name} -Pdist,native -DskipTests -DskipTest -DskipIT

# This takes a long time to run, so comment out for now
#%%check
#mvn-rpmbuild -Pdist,native test -Dmaven.test.failure.ignore=true

%install
# Copy all jar files except those generated by the build
# $1 the src directory
# $2 the dest directory
copy_dep_jars()
{
  find $1 ! -name "hadoop-*.jar" -name "*.jar" | xargs install -m 0644 -t $2
  rm -f $2/tools-*.jar
}

# Create symlinks for jars from the build
# $1 the location to create the symlink
link_hadoop_jars()
{
  for f in `ls hadoop-* | grep -v tests | grep -v examples`
  do
    n=`echo $f | sed "s/-%{version}//"`
    if [ -L $1/$n ]
    then
      continue
    elif [ -e $1/$f ]
    then
      rm -f $1/$f $1/$n
    fi
    p=`find %{buildroot}/%{_jnidir} %{buildroot}/%{_javadir}/%{name} -name $n | sed "s#%{buildroot}##"`
    %{__ln_s} $p $1/$n
  done
}

%mvn_install

install -d -m 0755 %{buildroot}/%{_libdir}/%{name}
install -d -m 0755 %{buildroot}/%{_includedir}/%{name}
install -d -m 0755 %{buildroot}/%{_jnidir}/%{name}

install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/client/lib
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/common/lib
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/hdfs/lib
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/hdfs/webapps
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/mapreduce/lib
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/yarn/lib
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}/tomcat/Catalina/localhost
install -d -m 0755 %{buildroot}/%{_sysconfdir}/logrotate.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}-hdfs
install -d -m 0755 %{buildroot}/%{_sharedstatedir}/tomcats/httpfs
install -d -m 0755 %{buildroot}/%{_var}/cache/%{name}-yarn
install -d -m 0755 %{buildroot}/%{_var}/cache/%{name}-httpfs/temp
install -d -m 0755 %{buildroot}/%{_var}/cache/%{name}-httpfs/work
install -d -m 0755 %{buildroot}/%{_var}/cache/%{name}-mapreduce
install -d -m 0755 %{buildroot}/%{_var}/log/%{name}-yarn
install -d -m 0755 %{buildroot}/%{_var}/log/%{name}-hdfs
install -d -m 0755 %{buildroot}/%{_var}/log/%{name}-httpfs
install -d -m 0755 %{buildroot}/%{_var}/log/%{name}-mapreduce
install -d -m 0755 %{buildroot}/%{_var}/run/%{name}-yarn
install -d -m 0755 %{buildroot}/%{_var}/run/%{name}-hdfs
install -d -m 0755 %{buildroot}/%{_var}/run/%{name}-mapreduce

basedir='%{name}-dist/target/%{name}-%{hadoop_version}'

for dir in bin libexec sbin
do
  cp -arf $basedir/$dir %{buildroot}/%{_prefix}
done

# This binary is obsoleted and causes a conflict with qt-devel
rm -rf %{buildroot}/%{_bindir}/rcc

# We don't care about this
rm -f %{buildroot}/%{_bindir}/test-container-executor

# Duplicate files
rm -f %{buildroot}/%{_sbindir}/hdfs-config.sh

cp -arf $basedir/etc/* %{buildroot}/%{_sysconfdir}
cp -arf $basedir/lib/native/libhadoop.so* %{buildroot}/%{_libdir}/%{name}
chrpath --delete %{buildroot}/%{_libdir}/%{name}/*
%if %{package_libhdfs}
cp -arf $basedir/include/hdfs.h %{buildroot}/%{_includedir}/%{name}
cp -arf $basedir/lib/native/libhdfs.so* %{buildroot}/%{_libdir}
chrpath --delete %{buildroot}/%{_libdir}/libhdfs*
cp -af hadoop-hdfs-project/hadoop-hdfs/target/native/main/native/fuse-dfs/fuse_dfs %{buildroot}/%{_bindir}
chrpath --delete %{buildroot}/%{_bindir}/fuse_dfs
%endif

# Not needed since httpfs is deployed with existing systemd setup
rm -f %{buildroot}/%{_sbindir}/httpfs.sh
rm -f %{buildroot}/%{_libexecdir}/httpfs-config.sh
rm -f %{buildroot}/%{_bindir}/httpfs-env.sh

# Remove files with .cmd extension
find %{buildroot} -name *.cmd | xargs rm -f 

# Modify hadoop-env.sh to point to correct locations for JAVA_HOME
# and JSVC_HOME.
sed -i "s|\${JAVA_HOME}|/usr/lib/jvm/jre|" %{buildroot}/%{_sysconfdir}/%{name}/%{name}-env.sh
sed -i "s|\${JSVC_HOME}|/usr/bin|" %{buildroot}/%{_sysconfdir}/%{name}/%{name}-env.sh

# Ensure the java provided DocumentBuilderFactory is used
sed -i "s|\(HADOOP_OPTS.*=.*\)\$HADOOP_CLIENT_OPTS|\1 -Djavax.xml.parsers.DocumentBuilderFactory=com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl \$HADOOP_CLIENT_OPTS|" %{buildroot}/%{_sysconfdir}/%{name}/%{name}-env.sh
echo "export YARN_OPTS=\"\$YARN_OPTS -Djavax.xml.parsers.DocumentBuilderFactory=com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl\"" >> %{buildroot}/%{_sysconfdir}/%{name}/yarn-env.sh

# Workaround for bz1012059
install -pm 644 hadoop-project-dist/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-%{name}-project-dist.pom
%{__ln_s} %{_jnidir}/%{name}/hadoop-common.jar %{buildroot}/%{_datadir}/%{name}/common
%{__ln_s} %{_javadir}/%{name}/hadoop-hdfs.jar %{buildroot}/%{_datadir}/%{name}/hdfs
%{__ln_s} %{_javadir}/%{name}/hadoop-client.jar %{buildroot}/%{_datadir}/%{name}/client

# client jar depenencies
copy_dep_jars %{name}-client/target/%{name}-client-%{hadoop_version}/share/%{name}/client/lib %{buildroot}/%{_datadir}/%{name}/client/lib
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/client/lib
pushd  %{name}-client/target/%{name}-client-%{hadoop_version}/share/%{name}/client/lib
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/client/lib
popd
pushd  %{name}-client/target/%{name}-client-%{hadoop_version}/share/%{name}/client
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/client
popd

# common jar depenencies
copy_dep_jars $basedir/share/%{name}/common/lib %{buildroot}/%{_datadir}/%{name}/common/lib
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/common/lib
pushd $basedir/share/%{name}/common
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/common
popd
for f in `ls %{buildroot}/%{_datadir}/%{name}/common/*.jar`
do
  echo "$f" | sed "s|%{buildroot}||" >> .mfiles
done
pushd $basedir/share/%{name}/common/lib
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/common/lib
popd

# hdfs jar dependencies
copy_dep_jars $basedir/share/%{name}/hdfs/lib %{buildroot}/%{_datadir}/%{name}/hdfs/lib
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/hdfs/lib
%{__ln_s} %{_jnidir}/%{name}/%{name}-hdfs-bkjournal.jar %{buildroot}/%{_datadir}/%{name}/hdfs/lib
pushd $basedir/share/%{name}/hdfs
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/hdfs
popd

# httpfs
# Create the webapp directory structure
pushd %{buildroot}/%{_sharedstatedir}/tomcats/httpfs
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/conf conf
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/lib lib
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/logs logs
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/temp temp
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/webapps webapps
  %{__ln_s} %{_datadir}/%{name}/httpfs/tomcat/work work
popd

# Copy the tomcat configuration and overlay with specific configuration bits.
# This is needed so the httpfs instance won't collide with a system running
# tomcat
for cfgfile in catalina.policy catalina.properties context.xml \
  tomcat.conf web.xml server.xml logging.properties;
do
  cp -a %{_sysconfdir}/tomcat/$cfgfile %{buildroot}/%{_sysconfdir}/%{name}/tomcat
done

# Replace, in place, the Tomcat configuration files delivered with the current
# Fedora release. See BZ#1295968 for some reason.
sed -i -e 's/8005/${httpfs.admin.port}/g' -e 's/8080/${httpfs.http.port}/g' %{buildroot}/%{_sysconfdir}/%{name}/tomcat/server.xml
sed -i -e 's/catalina.base/httpfs.log.dir/g' %{buildroot}/%{_sysconfdir}/%{name}/tomcat/logging.properties
# Given the permission, only the root and tomcat users can access to that file,
# not the build user. So, the build would fail here.
install -m 660 %{SOURCE14} %{buildroot}/%{_sysconfdir}/%{name}/tomcat/tomcat-users.xml

# Copy the httpfs webapp
cp -arf %{name}-hdfs-project/%{name}-hdfs-httpfs/target/webhdfs %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps

# Tell tomcat to follow symlinks
cat > %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps/webhdfs/META-INF/context.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<Context allowLinking="true">
</Context>
EOF

# Remove the jars included in the webapp and create symlinks
rm -f %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps/webhdfs/WEB-INF/lib/tools*.jar
rm -f %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps/webhdfs/WEB-INF/lib/tomcat-*.jar
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps/webhdfs/WEB-INF/lib
pushd %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat/webapps/webhdfs/WEB-INF/lib
  link_hadoop_jars .
popd

pushd %{buildroot}/%{_datadir}/%{name}/httpfs/tomcat
  %{__ln_s} %{_datadir}/tomcat/bin bin
  %{__ln_s} %{_sysconfdir}/%{name}/tomcat conf
  %{__ln_s} %{_datadir}/tomcat/lib lib
  %{__ln_s} %{_var}/cache/%{name}-httpfs/temp temp
  %{__ln_s} %{_var}/cache/%{name}-httpfs/work work
  %{__ln_s} %{_var}/log/%{name}-httpfs logs
popd

# mapreduce jar dependencies
copy_dep_jars $basedir/share/%{name}/mapreduce/lib %{buildroot}/%{_datadir}/%{name}/mapreduce/lib
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/mapreduce/lib
%{__ln_s} %{_javadir}/%{name}/%{name}-annotations.jar %{buildroot}/%{_datadir}/%{name}/mapreduce/lib
pushd $basedir/share/%{name}/mapreduce
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/mapreduce
popd

# yarn jar dependencies
copy_dep_jars $basedir/share/%{name}/yarn/lib %{buildroot}/%{_datadir}/%{name}/yarn/lib
%{_bindir}/xmvn-subst %{buildroot}/%{_datadir}/%{name}/yarn/lib
%{__ln_s} %{_javadir}/%{name}/%{name}-annotations.jar %{buildroot}/%{_datadir}/%{name}/yarn/lib
pushd $basedir/share/%{name}/yarn
  link_hadoop_jars %{buildroot}/%{_datadir}/%{name}/yarn
popd

# Install hdfs webapp bits
cp -arf $basedir/share/hadoop/hdfs/webapps/* %{buildroot}/%{_datadir}/%{name}/hdfs/webapps

# hadoop layout. Convert to appropriate lib location for 32 and 64 bit archs
lib=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$lib" = "%_libdir" ]; then
  echo "_libdir is not located in /usr.  Lib location is wrong"
  exit 1
fi
sed -e "s|HADOOP_COMMON_LIB_NATIVE_DIR\s*=.*|HADOOP_COMMON_LIB_NATIVE_DIR=$lib/%{name}|" %{SOURCE1} > %{buildroot}/%{_libexecdir}/%{name}-layout.sh

# Default config
cp -f %{SOURCE8} %{buildroot}/%{_sysconfdir}/%{name}/core-site.xml
cp -f %{SOURCE9} %{buildroot}/%{_sysconfdir}/%{name}/hdfs-site.xml
cp -f %{SOURCE10} %{buildroot}/%{_sysconfdir}/%{name}/mapred-site.xml
cp -f %{SOURCE11} %{buildroot}/%{_sysconfdir}/%{name}/yarn-site.xml

# systemd configuration
install -d -m 0755 %{buildroot}/%{_unitdir}/
for service in %{hdfs_services} %{mapreduce_services} %{yarn_services}
do
  s=`echo $service | cut -d'-' -f 2 | cut -d'.' -f 1`
  daemon=$s
  if [[ "%{hdfs_services}" == *$service* ]]
  then
    src=%{SOURCE2}
  elif [[ "%{mapreduce_services}" == *$service* ]]
  then
    src=%{SOURCE3}
  elif [[ "%{yarn_services}" == *$service* ]]
  then
    if [[ "$s" == "timelineserver" ]]
    then
      daemon='historyserver'
    fi
    src=%{SOURCE4}
  else
    echo "Failed to determine type of service for %service"
    exit 1
  fi
  sed -e "s|DAEMON|$daemon|g" $src > %{buildroot}/%{_unitdir}/%{name}-$s.service
done

cp -f %{SOURCE12} %{buildroot}/%{_sysconfdir}/sysconfig/tomcat@httpfs

# Ensure /var/run directories are recreated on boot
echo "d %{_var}/run/%{name}-yarn 0775 yarn hadoop -" > %{buildroot}/%{_tmpfilesdir}/%{name}-yarn.conf
echo "d %{_var}/run/%{name}-hdfs 0775 hdfs hadoop -" > %{buildroot}/%{_tmpfilesdir}/%{name}-hdfs.conf
echo "d %{_var}/run/%{name}-mapreduce 0775 mapred hadoop -" > %{buildroot}/%{_tmpfilesdir}/%{name}-mapreduce.conf

# logrotate config
for type in hdfs httpfs yarn mapreduce
do
  sed -e "s|NAME|$type|" %{SOURCE6} > %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}-$type
done
sed -i "s|{|%{_var}/log/hadoop-hdfs/*.audit\n{|" %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}-hdfs

# hdfs init script
install -m 755 %{SOURCE13} %{buildroot}/%{_sbindir}

%pre common
getent group hadoop >/dev/null || groupadd -r hadoop

%pre hdfs
getent group hdfs >/dev/null || groupadd -r hdfs
getent passwd hdfs >/dev/null || /usr/sbin/useradd --comment "Apache Hadoop HDFS" --shell /sbin/nologin -M -r -g hdfs -G hadoop --home %{_sharedstatedir}/%{name}-hdfs hdfs

# from pretrans
path = "%{_datadir}/%{name}/hdfs/webapps"
if [ -L $path ]; then
  rm -f $path
fi ||:



%pre mapreduce
getent group mapred >/dev/null || groupadd -r mapred
getent passwd mapred >/dev/null || /usr/sbin/useradd --comment "Apache Hadoop MapReduce" --shell /sbin/nologin -M -r -g mapred -G hadoop --home %{_var}/cache/%{name}-mapreduce mapred

%pre yarn
getent group yarn >/dev/null || groupadd -r yarn
getent passwd yarn >/dev/null || /usr/sbin/useradd --comment "Apache Hadoop Yarn" --shell /sbin/nologin -M -r -g yarn -G hadoop --home %{_var}/cache/%{name}-yarn yarn

%post hdfs
if [[ `getent passwd hdfs | cut -d: -f 6` != "%{_sharedstatedir}/%{name}-hdfs" ]]
then
  /usr/sbin/usermod -d %{_sharedstatedir}/%{name}-hdfs hdfs
fi

if [ $1 -gt 1 ]
then
  if [ -d %{_var}/cache/%{name}-hdfs ] && [ ! -L %{_var}/cache/%{name}-hdfs ]
  then
    # Move the existing hdfs data to the new location
    mv -f %{_var}/cache/%{name}-hdfs/* %{_sharedstatedir}/%{name}-hdfs/
  fi
fi
if [ ! -e %{_var}/cache/%{name}-hdfs ]
then
  %{__ln_s} %{_sharedstatedir}/%{name}-hdfs %{_var}/cache
fi


%postun hdfs
%systemd_postun_with_restart %{hdfs_services}

if [ $1 -lt 1 ]
then
  # Remove the compatibility symlink
  rm -f %{_var}/cache/%{name}-hdfs
fi

%postun mapreduce
%systemd_postun_with_restart %{mapreduce_services}

%postun yarn
%systemd_postun_with_restart %{yarn_services}

%files -f .mfiles-%{name}-client client
%{_datadir}/%{name}/client

%files -f .mfiles common
%doc hadoop-dist/target/hadoop-%{hadoop_version}/share/doc/hadoop/common/*
%config(noreplace) %{_sysconfdir}/%{name}/configuration.xsl
%config(noreplace) %{_sysconfdir}/%{name}/core-site.xml
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-env.sh
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-metrics.properties
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-metrics2.properties
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-policy.xml
%config(noreplace) %{_sysconfdir}/%{name}/log4j.properties
%config(noreplace) %{_sysconfdir}/%{name}/slaves
%config(noreplace) %{_sysconfdir}/%{name}/ssl-client.xml.example
%config(noreplace) %{_sysconfdir}/%{name}/ssl-server.xml.example
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/common
%{_datadir}/%{name}/common/lib
%{_libexecdir}/%{name}-config.sh
%{_libexecdir}/%{name}-layout.sh

# Workaround for bz1012059
%{_mavenpomdir}/JPP.%{name}-%{name}-project-dist.pom

%{_bindir}/%{name}
%{_sbindir}/%{name}-daemon.sh
%{_sbindir}/%{name}-daemons.sh
%{_sbindir}/start-all.sh
%{_sbindir}/start-balancer.sh
%{_sbindir}/start-dfs.sh
%{_sbindir}/start-secure-dns.sh
%{_sbindir}/stop-all.sh
%{_sbindir}/stop-balancer.sh
%{_sbindir}/stop-dfs.sh
%{_sbindir}/stop-secure-dns.sh
%{_sbindir}/slaves.sh

%files common-native
%{_libdir}/%{name}/libhadoop.*

%if %{package_libhdfs}
%files devel
%{_includedir}/%{name}
%{_libdir}/libhdfs.so
%endif

%files -f .mfiles-%{name}-hdfs hdfs
%config(noreplace) %{_sysconfdir}/%{name}/hdfs-site.xml
%{_datadir}/%{name}/hdfs
%{_unitdir}/%{name}-datanode.service
%{_unitdir}/%{name}-namenode.service
%{_unitdir}/%{name}-journalnode.service
%{_unitdir}/%{name}-secondarynamenode.service
%{_unitdir}/%{name}-zkfc.service
%{_libexecdir}/hdfs-config.sh
%{_bindir}/hdfs
%{_sbindir}/distribute-exclude.sh
%{_sbindir}/refresh-namenodes.sh
%{_sbindir}/hdfs-create-dirs
%{_tmpfilesdir}/%{name}-hdfs.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}-hdfs
%attr(0755,hdfs,hadoop) %dir %{_var}/run/%{name}-hdfs
%attr(0755,hdfs,hadoop) %dir %{_var}/log/%{name}-hdfs
%attr(0755,hdfs,hadoop) %dir %{_sharedstatedir}/%{name}-hdfs

%if %{package_libhdfs}
%files hdfs-fuse
%attr(755,hdfs,hadoop) %{_bindir}/fuse_dfs
%endif

%files httpfs
%config(noreplace) %{_sysconfdir}/sysconfig/tomcat@httpfs
%config(noreplace) %{_sysconfdir}/%{name}/httpfs-env.sh
%config(noreplace) %{_sysconfdir}/%{name}/httpfs-log4j.properties
%config(noreplace) %{_sysconfdir}/%{name}/httpfs-signature.secret
%config(noreplace) %{_sysconfdir}/%{name}/httpfs-site.xml
%attr(-,tomcat,tomcat) %config(noreplace) %{_sysconfdir}/%{name}/tomcat/*.*
%attr(0775,root,tomcat) %dir %{_sysconfdir}/%{name}/tomcat
%attr(0775,root,tomcat) %dir %{_sysconfdir}/%{name}/tomcat/Catalina
%attr(0775,root,tomcat) %dir %{_sysconfdir}/%{name}/tomcat/Catalina/localhost
%{_datadir}/%{name}/httpfs
%{_sharedstatedir}/tomcats/httpfs
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}-httpfs
%attr(0775,root,tomcat) %dir %{_var}/log/%{name}-httpfs
%attr(0775,root,tomcat) %dir %{_var}/cache/%{name}-httpfs
%attr(0775,root,tomcat) %dir %{_var}/cache/%{name}-httpfs/temp
%attr(0775,root,tomcat) %dir %{_var}/cache/%{name}-httpfs/work

%if %{package_libhdfs}
%files -n libhdfs
%doc hadoop-dist/target/hadoop-%{hadoop_version}/share/doc/hadoop/hdfs/LICENSE.txt
%{_libdir}/libhdfs.so.*
%endif

%files -f .mfiles-%{name}-mapreduce mapreduce
%config(noreplace) %{_sysconfdir}/%{name}/mapred-env.sh
%config(noreplace) %{_sysconfdir}/%{name}/mapred-queues.xml.template
%config(noreplace) %{_sysconfdir}/%{name}/mapred-site.xml
%config(noreplace) %{_sysconfdir}/%{name}/mapred-site.xml.template
%{_datadir}/%{name}/mapreduce
%{_libexecdir}/mapred-config.sh
%{_unitdir}/%{name}-historyserver.service
%{_bindir}/mapred
%{_sbindir}/mr-jobhistory-daemon.sh
%{_tmpfilesdir}/%{name}-mapreduce.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}-mapreduce
%attr(0755,mapred,hadoop) %dir %{_var}/run/%{name}-mapreduce
%attr(0755,mapred,hadoop) %dir %{_var}/log/%{name}-mapreduce
%attr(0755,mapred,hadoop) %dir %{_var}/cache/%{name}-mapreduce

%files -f .mfiles-%{name}-mapreduce-examples mapreduce-examples

%files -f .mfiles-%{name}-maven-plugin maven-plugin
%doc hadoop-dist/target/hadoop-%{hadoop_version}/share/doc/hadoop/common/LICENSE.txt

%files -f .mfiles-%{name}-tests tests

%files -f .mfiles-%{name}-yarn yarn
%config(noreplace) %{_sysconfdir}/%{name}/capacity-scheduler.xml
%config(noreplace) %{_sysconfdir}/%{name}/yarn-env.sh
%config(noreplace) %{_sysconfdir}/%{name}/yarn-site.xml
%{_unitdir}/%{name}-nodemanager.service
%{_unitdir}/%{name}-proxyserver.service
%{_unitdir}/%{name}-resourcemanager.service
%{_unitdir}/%{name}-timelineserver.service
%{_libexecdir}/yarn-config.sh
%{_datadir}/%{name}/yarn
%{_bindir}/yarn
%{_sbindir}/yarn-daemon.sh
%{_sbindir}/yarn-daemons.sh
%{_sbindir}/start-yarn.sh
%{_sbindir}/stop-yarn.sh
%{_tmpfilesdir}/%{name}-yarn.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}-yarn
%attr(0755,yarn,hadoop) %dir %{_var}/run/%{name}-yarn
%attr(0755,yarn,hadoop) %dir %{_var}/log/%{name}-yarn
%attr(0755,yarn,hadoop) %dir %{_var}/cache/%{name}-yarn

%files yarn-security
%config(noreplace) %{_sysconfdir}/%{name}/container-executor.cfg
# Permissions set per upstream guidelines: http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html#Configuration_in_Secure_Mode
%attr(6010,root,yarn) %{_bindir}/container-executor

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_23jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_17jpp8
- new fc release

* Wed Jun 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_14jpp8
- fixed build w/tomcat 8

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_14jpp8
- new version

