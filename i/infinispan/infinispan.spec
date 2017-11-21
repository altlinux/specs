Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 8.2.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

# Use this switch to rebuild without infinispan
# This is useful to break the infinispan circular dependency
%if 0%{?fedora}
%bcond_with infinispan
# https://bugzilla.redhat.com/show_bug.cgi?id=1363923
%bcond_with spring4
%endif

Name:          infinispan
Version:       8.2.4
Release:       alt1_3jpp8
Summary:       Data grid platform
License:       ASL 2.0 and LGPLv2+ and Public Domain
URL:           http://infinispan.org/
Source0:       https://github.com/infinispan/infinispan/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

# Port to lucene 6.x
Patch0: lucene-6.patch

BuildRequires: maven-local
BuildRequires: mvn(com.clearspring.analytics:stream)
BuildRequires: mvn(com.mchange:c3p0)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-pool:commons-pool)
BuildRequires: mvn(gnu-getopt:getopt)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(net.jcip:jcip-annotations)
BuildRequires: mvn(org.antlr:antlr-runtime)
BuildRequires: mvn(org.antlr:antlr3-maven-plugin)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jcache_1.0_spec)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.logging.log4j:log4j-jcl)
BuildRequires: mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires: mvn(org.apache.lucene:lucene-core) >= 5.3.1
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-common) >= 5.3.1
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.fusesource.leveldbjni:leveldbjni)
BuildRequires: mvn(org.hibernate:hibernate-core)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
%if %{with infinispan}
BuildRequires: mvn(org.hibernate.hql:hibernate-hql-lucene) >= 1.3.0
BuildRequires: mvn(org.hibernate.hql:hibernate-hql-parser) >= 1.3.0
BuildRequires: mvn(org.hibernate:hibernate-search-engine) >= 5.5.1
BuildRequires: mvn(org.hibernate:hibernate-search-serialization-avro) >= 5.5.1
BuildRequires: mvn(org.infinispan:infinispan-core)
BuildRequires: mvn(org.infinispan:infinispan-lucene-directory)
BuildRequires: mvn(org.infinispan:infinispan-query-dsl)
%endif
BuildRequires: mvn(org.infinispan.protostream:protostream) >= 3.0.4
BuildRequires: mvn(org.iq80.leveldb:leveldb)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.aesh:aesh)
BuildRequires: mvn(org.jboss.arquillian:arquillian-bom:pom:)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-osgi)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.remotingjmx:remoting-jmx)
BuildRequires: mvn(org.jboss.sasl:jboss-sasl)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom:pom:)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires: mvn(org.jboss.xnio:xnio-nio)
BuildRequires: mvn(org.jgroups:jgroups) >= 3.6.4
BuildRequires: mvn(org.kohsuke.metainf-services:metainf-services)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.springframework:spring-context)
%if %{with spring4}
BuildRequires: mvn(org.springframework:spring-context:4)
%endif
BuildRequires: mvn(org.wildfly.core:wildfly-controller)
BuildRequires: mvn(org.wildfly.core:wildfly-core-parent:pom:)

# Public Domain: ./commons/src/main/java/org/infinispan/commons/util/Base64.java
Provides:      bundled(java-base64) = 4.2

BuildArch:     noarch
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
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
#patch0

find .  -name "*.jar" -print -delete
find .  -name "*.class" -print -delete

# Rename the license file
cp -pr license/src/main/resources/META-INF/LICENSE.txt.vm LICENSE.txt

# Checkstyle is unnecessary for RPM builds
%pom_disable_module checkstyle
%pom_remove_plugin -r org.apache.maven.plugins:maven-checkstyle-plugin

%pom_disable_module all
%pom_disable_module all/cli
%pom_disable_module all/embedded
%pom_disable_module all/embedded-query
%pom_disable_module all/remote
%pom_disable_module as-modules/embedded
%pom_disable_module as-modules/client
%pom_disable_module demos/gui
%pom_disable_module demos/distexec
%pom_disable_module demos/lucene-directory-demo
%pom_disable_module demos/gridfs-webdav
%pom_disable_module demos/nearcache
%pom_disable_module demos/nearcache-client
%pom_disable_module integrationtests
%pom_disable_module integrationtests/as-integration-embedded
%pom_disable_module integrationtests/as-integration-client
%pom_disable_module integrationtests/as-lucene-directory
%pom_disable_module integrationtests/compatibility-mode-it
%pom_disable_module integrationtests/cdi-jcache-it
%pom_disable_module integrationtests/security-it
%pom_disable_module integrationtests/security-manager-it
%pom_disable_module integrationtests/osgi
%pom_disable_module integrationtests/cdi-weld-se-it
%pom_disable_module integrationtests/all-embedded-it
%pom_disable_module integrationtests/all-embedded-query-it
%pom_disable_module integrationtests/all-remote-it
%pom_disable_module javadoc
%pom_disable_module persistence/rest
%pom_disable_module rhq-plugin
%pom_disable_module server/integration
%pom_disable_module server/rest
%pom_disable_module tck-runner jcache

%if %{without spring4}
%pom_disable_module spring/spring4
%pom_disable_module spring/spring4/spring4-common
%pom_disable_module spring/spring4/spring4-embedded
%pom_disable_module spring/spring4/spring4-remote
%else
%pom_xpath_set pom:properties/pom:version.spring4 4 parent
%pom_change_dep -r org.springframework: ::'${version.spring4}' spring/spring4/spring4-common spring/spring4/spring4-embedded spring/spring4/spring4-remote
%endif

%pom_xpath_set pom:properties/pom:version.jboss.logging.processor 1 parent

%pom_remove_plugin ":maven-remote-resources-plugin" parent
# org.scala-tools:maven-scala-plugin:2.15.2 used for generate-blueprint task
%pom_remove_plugin -r ":maven-scala-plugin" parent jcache/embedded

%pom_remove_plugin :jetty-maven-plugin persistence/rest

%pom_remove_plugin :maven-invoker-plugin jcache/embedded
%pom_remove_plugin :maven-failsafe-plugin parent

# Use eclipse apis: type ServiceTracker does not take parameters
%pom_change_dep -r org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi commons persistence/jpa osgi bom
%pom_remove_dep -r org.osgi:org.osgi.compendium commons persistence/jpa
%pom_change_dep -r org.osgi:org.osgi.compendium org.eclipse.osgi:org.eclipse.osgi.services osgi bom

%pom_change_dep -r javax.cache:cache-api org.apache.geronimo.specs:geronimo-jcache_1.0_spec:1.0-alpha-1 jcache/commons jcache/embedded jcache/remote bom core cdi/remote

%pom_change_dep :leveldbjni-all :leveldbjni persistence/leveldb

# https://bugs.openjdk.java.net/browse/JDK-8067747
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" '
<useIncrementalCompilation>false</useIncrementalCompilation>
<source>${version.java}</source>
<target>${version.java}</target>' commons
for p in core server/core persistence/jdbc lucene/lucene-directory \
 query server/hotrod \
 tree client/hotrod-client persistence/remote persistence/leveldb server/memcached \
 server/websocket cli/cli-interpreter cdi/embedded cdi/remote jcache/embedded;do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 ${p} '
<configuration>
 <useIncrementalCompilation>false</useIncrementalCompilation>
 <source>${version.java}</source>
 <target>${version.java}</target>
 <encoding>UTF-8</encoding>
</configuration>'
done

# Compile scala stuff
for p in core \
 hotrod \
 memcached;do
%pom_remove_plugin ":maven-scala-plugin" server/${p}
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 server/${p} '
<executions>
  <execution>
    <id>compile</id>
    <phase>process-sources</phase>
    <configuration>
      <tasks>
        <property name="build.compiler" value="extJavac"/>
        <taskdef resource="scala/tools/ant/antlib.xml" classpathref="maven.compile.classpath"/>
        <mkdir dir="target/classes"/>
        <scalac srcdir="src/main" destdir="target/classes" classpathref="maven.compile.classpath" encoding="UTF-8">
          <include name="**/*.*"/>
        </scalac>
      </tasks>
    </configuration>
      <goals>
        <goal>run</goal>
      </goals>
  </execution>
</executions>
<dependencies>
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-compiler</artifactId>
      <version>${version.scala}</version>
  </dependency>
</dependencies>'
done

%if %{without infinispan}
%pom_disable_module lucene/directory-provider
%pom_disable_module object-filter
%pom_disable_module query
%pom_disable_module remote-query/remote-query-server
%pom_disable_module scripting
%pom_disable_module server/hotrod
%pom_disable_module tasks
%pom_disable_module tools
%endif

%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:scope" tools
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:systemPath" tools

# org.hibernate:hibernate-search-engine:tests:5.5.1.Final
%pom_xpath_remove "pom:dependency[pom:groupId = 'org.hibernate']/pom:classifier" lucene/directory-provider

# This component is now owned and maintained by the Infinispan team
%mvn_alias :infinispan-directory-provider org.hibernate:hibernate-search-infinispan

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md README-i18n.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_3jpp8
- fixed build with new checkstyle

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 8.2.4-alt1_2jpp8
- new version

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

