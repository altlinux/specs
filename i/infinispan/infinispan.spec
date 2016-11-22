Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name infinispan
%define version 6.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

# Use this switch to rebuild without infinispan
# This is useful to break the infinispan circular dependency
%define with_infinispan 1

Name:             infinispan
Version:          6.0.2
Release:          alt1_8jpp8
Summary:          Data grid platform
License:          LGPLv2+
URL:              http://www.jboss.org/infinispan
Source0:          https://github.com/infinispan/infinispan/archive/%{namedversion}.tar.gz

Patch0:           0001-Avro-1.6.2-support.patch
Patch1:           0002-ISPN-3974-Make-it-compile-with-JDK8.patch
Patch2:           infinispan-6.0.2-lucene4.10-support.patch

BuildArch:        noarch

%if %{with_infinispan}
BuildRequires:    infinispan
%endif

BuildRequires:    maven-local
BuildRequires:    mvn(c3p0:c3p0)
BuildRequires:    mvn(com.puppycrawl.tools:checkstyle)
BuildRequires:    mvn(commons-pool:commons-pool)
BuildRequires:    mvn(gnu-getopt:getopt)
BuildRequires:    mvn(log4j:log4j)
BuildRequires:    mvn(net.jcip:jcip-annotations)
BuildRequires:    mvn(org.apache.avro:avro)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.lucene:lucene-core:3)
%if 0%{?fedora} >= 23
# Require these anyhow, always
BuildRequires:    mvn(org.apache.lucene:lucene-core:4)
BuildRequires:    mvn(org.apache.lucene:lucene-analyzers-common:4)
%else
BuildRequires:    mvn(org.apache.lucene:lucene-core)
BuildRequires:    mvn(org.apache.lucene:lucene-analyzers-common)
%endif
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:    mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:    mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:    mvn(org.hibernate:hibernate-search-engine) >= 4.5.1
BuildRequires:    mvn(org.hibernate:hibernate-search-infinispan)
BuildRequires:    mvn(org.hibernate.hql:hibernate-hql-lucene)
BuildRequires:    mvn(org.hibernate.hql:hibernate-hql-parser)
BuildRequires:    mvn(org.infinispan.protostream:protostream)
BuildRequires:    mvn(org.jboss.aesh:aesh)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:    mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires:    mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires:    mvn(org.jgroups:jgroups)
BuildRequires:    mvn(org.osgi:org.osgi.core)
Source44: import.info


%description
Infinispan is an extremely scalable, highly available data grid
platform - 100% open source, and written in Java. The purpose of
Infinispan is to expose a data structure that is highly concurrent,
designed ground-up to make the most of modern multi-processor/multi-core
architectures while at the same time providing distributed cache
capabilities.  At its core Infinispan exposes a Cache interface which
extends java.util.Map. It is also optionally is backed by a peer-to-peer
network architecture to distribute state efficiently around a data grid.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Rename the license file
cp -r license/src/main/resources/META-INF/LICENSE.txt.vm LICENSE.txt

# Disable unnecessary at this point modules
%pom_disable_module extended-statistics
%pom_disable_module tools
%pom_disable_module tree
%if 0%{?fedora} < 21
%pom_disable_module lucene/lucene-v4
%endif
%pom_disable_module server
%pom_disable_module server/core
%pom_disable_module server/memcached
%pom_disable_module server/hotrod
%pom_disable_module server/websocket
%pom_disable_module server/rest
%pom_disable_module cli/cli-server
%pom_disable_module rhq-plugin
%pom_disable_module spring
%pom_disable_module demos/gui
%pom_disable_module demos/ec2
%pom_disable_module demos/distexec
%pom_disable_module demos/ec2-ui
%pom_disable_module demos/directory
%pom_disable_module demos/lucene-directory-demo
%pom_disable_module demos/gridfs-webdav
%pom_disable_module demos/nearcache
%pom_disable_module demos/nearcache-client
%pom_disable_module cdi/extension
%pom_disable_module integrationtests/luceneintegration
%pom_disable_module remote-query/remote-query-server
%pom_disable_module persistence/leveldb
%pom_disable_module persistence/rest
%pom_disable_module server/integration

# Remove the 5.2.x migration support
rm persistence/remote/src/main/java/org/infinispan/persistence/remote/upgrade/HotRodTargetMigrator.java
%pom_remove_dep ":infinispan-adaptor52x" persistence/remote
%pom_disable_module compatibility52x

%pom_disable_module compatibility52x/adaptor52x
%pom_disable_module compatibility52x/custom52x-store
%pom_disable_module compatibility52x/cli-migrator52x

%pom_disable_module as-modules
%pom_disable_module jcache

%if !%{with_infinispan}
%pom_disable_module query
%endif

# https://bugs.openjdk.java.net/browse/JDK-8067747
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" \
 "<useIncrementalCompilation>false</useIncrementalCompilation>" commons
for p in core persistence/jdbc query client/hotrod-client persistence/remote ;do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 ${p} '
<configuration>
 <useIncrementalCompilation>false</useIncrementalCompilation>
 <source>1.6</source>
 <target>1.6</target>
 <encoding>UTF-8</encoding>
</configuration>'
done

%pom_remove_dep "org.jboss.arquillian:arquillian-bom" parent/pom.xml
%pom_remove_dep "org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom" parent/pom.xml

%pom_remove_plugin ":maven-remote-resources-plugin" parent/pom.xml

%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope = 'test']/pom:scope" lucene/lucene-directory/pom.xml

%if 0%{?fedora} < 21
# Lucene 4 is unavailable
%pom_remove_dep ":infinispan-lucene-v4" lucene/lucene-directory/pom.xml
%pom_remove_dep ":infinispan-lucene-v4" parent/pom.xml
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-dependency-plugin']/pom:executions/pom:execution/pom:configuration/pom:artifactItems/pom:artifactItem[pom:artifactId = 'infinispan-lucene-v4']" lucene/lucene-directory/pom.xml
%endif

%pom_remove_plugin ":animal-sniffer-maven-plugin" parent/pom.xml

# Support for JGroups 3.4.0
sed -i "s|SiteUUID.getSiteName(src.getSite())|src.getSite()|" core/src/main/java/org/infinispan/xsite/BackupReceiverRepositoryImpl.java

# Use lucene3 compat package
%pom_xpath_set "pom:properties/pom:version.lucene.v3" 3 parent
# Use lucene4 compat package
%pom_xpath_set "pom:properties/pom:version.lucene.v4" 4 parent

# TMP
sed -i "s|error|first|" lucene/lucene-directory/pom.xml

%pom_remove_dep "org.scala-lang:scala-library" server/pom.xml
%pom_remove_plugin "org.scala-tools:maven-scala-plugin" server/core/pom.xml

%pom_remove_dep "org.jboss.as:jboss-as-parent" server/integration/versions/pom.xml
%pom_remove_plugin ":animal-sniffer-maven-plugin" server/integration/versions/pom.xml

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_7jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_3jpp7
- new version

