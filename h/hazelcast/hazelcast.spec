Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          hazelcast
Version:       3.2.2
Release:       alt1_8jpp8
Summary:       Hazelcast CE In-Memory DataGrid
License:       ASL 2.0
URL:           http://www.hazelcast.com/
Source0:       https://github.com/hazelcast/hazelcast/archive/v%{version}.tar.gz


BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sourceforge.findbugs:annotations)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.codehaus.groovy:groovy)
BuildRequires: mvn(org.hibernate:hibernate-core:4)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires: mvn(org.jruby:jruby-core)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: glassfish-jsp-api

%if 0
# hazelcast-spring
BuildRequires: hibernate3
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.mongodb:mongo-java-driver) >= 2.7.3
# Unavailable dep
BuildRequires: mvn(org.springframework.data:spring-data-mongodb) >= 1.0.1.RELEASE

# hazelcast-spring test deps
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework:spring-test)

# test deps
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%endif

BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)

BuildRequires: maven-local
BuildRequires: maven-dependency-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
Hazelcast CE is an open source highly scalable data distribution platform.
Hazelcast allows you to easily share and partition your data across your
cluster.

%package client
Group: Development/Java
Summary:       Hazelcast Client

%description client
Hazelcast Client enables you to do all Hazelcast
operations without being a member of the cluster.

%package cloud
Group: Development/Java
Summary:       Hazelcast EC2 Auto Discovery

%description cloud
Hazelcast EC2 Auto Discovery.

%package hibernate
Group: Development/Java
Summary:       Integration of Hazelcast with Hibernate 3
Provides:      %{name}-hibernate3 = %{version}-%{release}
Obsoletes:     %{name}-hibernate3 < %{version}-%{release}

%description hibernate
Hazelcast second level cache provider for Hibernate 3.

%package ra
Group: Development/Java
Summary:       Hazelcast Resource Adapter
Requires:      %{name} = %{version}-%{release}

%description ra
Hazelcast Resource Adapter.

%if 0
%package spring
Group: Development/Java
Summary:       Integration of Hazelcast with Spring

%description spring
Hazelcast Spring cache provider.
%endif

%package wm
Group: Development/Java
Summary:       Hazelcast WebFilter

%description wm
Hazelcast dynamic HTTP session clustering.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name "*.bat" -delete
find . -name "*.class" -delete
find . -name "*.jar" -delete
find . -name "*.rar" -delete
find . -name "*.war" -delete

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin 
%pom_remove_plugin -r :jetty-maven-plugin

%pom_disable_module %{name}-documentation
%pom_disable_module hazelcast-hibernate3 %{name}-hibernate
%pom_disable_module hazelcast-jca-rar %{name}-ra
# requires org.springframework.data:spring-data-mongodb
%pom_disable_module %{name}-spring

%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package" %{name}-all
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" "
<Import-Package>
    !junit.framework,
    !org.junit,
    !org.mockito,
    org.apache.log4j;resolution:=optional,
    org.apache.log4j.*;resolution:=optional,
    org.slf4j;resolution:=optional,
    org.hibernate;resolution:=optional,
    org.hibernate.*;resolution:=optional,
    *
</Import-Package>" %{name}-all

%pom_remove_plugin :maven-shade-plugin %{name}-all

%pom_change_dep :hazelcast-hibernate3 :hazelcast-hibernate4 %{name}-all

%pom_change_dep -r org.mockito: :mockito-core
%pom_change_dep org.jruby: :jruby-core %{name}
%pom_change_dep org.codehaus.groovy: :groovy %{name}

%pom_change_dep :geronimo-j2ee-connector_1.5_spec org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec %{name}-ra/%{name}-jca

%pom_remove_dep org.jboss.spec:jboss-javaee-6.0 %{name}-ra/%{name}-jca
%pom_remove_dep org.jboss.arquillian.extension:arquillian-transaction-bom %{name}-ra/%{name}-jca
%pom_remove_dep org.jboss.arquillian:arquillian-bom %{name}-ra/%{name}-jca

%pom_change_dep javax.servlet:javax.servlet-api org.apache.tomcat:tomcat-servlet-api %{name}-wm

cp -p src/main/resources/apache-v2-license.txt license.txt
cp -p src/main/resources/notice.txt .

sed -i 's|../lib/hazelcast-${project.version}.jar|%{_javadir}/%{name}/%{name}.jar|' \
 %{name}/src/main/resources/*.sh
sed -i 's|../lib/hazelcast-client-${project.version}.jar|%{_javadir}/%{name}/%{name}-client.jar|' \
%{name}/src/main/resources/client.sh

%pom_xpath_remove -r "pom:project/pom:dependencies/pom:dependency[pom:scope='test']"
rm -rf hazelcast*/src/test/java/*

%pom_xpath_set -r "pom:properties/pom:log4j.version" 1.2.17
%pom_xpath_set -r "pom:properties/pom:hibernate.core.version" 4

%mvn_package ":%{name}-root" %{name}
%mvn_package ":%{name}-hibernate*" %{name}-hibernate
%mvn_package ":%{name}-jca" %{name}-ra

%build

# takes too much time and @ random fails
# e.g.
# [INFO] hazelcast ......................................... SUCCESS [49:00.842s]
# Tests in error: 
#  putIfAbsentWithTtl(com.hazelcast.client.HazelcastClientMapTest): No cluster member available to connect
#  testNoClusterAfterStart(com.hazelcast.client.HazelcastClientClusterTest): Unexpected exception, expected<com.hazelcast.client.NoMemberAvailableException> but was<java.lang.RuntimeException>

%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%doc README.md
%doc license.txt notice.txt

%files client -f .mfiles-%{name}-client
%doc license.txt notice.txt

%files cloud -f .mfiles-%{name}-cloud
%doc license.txt notice.txt

%files hibernate -f .mfiles-%{name}-hibernate
%doc license.txt notice.txt

%files ra -f .mfiles-%{name}-ra
%doc license.txt notice.txt

%if 0
%files spring -f .mfiles-%{name}-spring
%doc license.txt notice.txt
%endif

%files wm -f .mfiles-%{name}-wm
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_8jpp8
- new version

