Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 9bd33de81ccdce1c1c448cdd3c0aa8d9480eff9a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          datanucleus-rdbms
Version:       3.2.13
Release:       alt1_8jpp8
Summary:       DataNucleus RDBMS
License:       ASL 2.0
URL:           http://www.datanucleus.org/%{name}
Source:        https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: java-devel
BuildRequires: mvn(com.mchange:c3p0)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-dbcp:commons-dbcp)
BuildRequires: mvn(commons-pool:commons-pool)
BuildRequires: mvn(javax.time:time-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
BuildRequires: mvn(proxool:proxool)
BuildRequires: mvn(org.apache.tomcat:tomcat-jdbc)
# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j)

BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: datanucleus-maven-parent

# fix for broken proxool metadata
BuildRequires: mvn(net.sf.cglib:cglib)

BuildArch:     noarch
Source44: import.info

%description
Plugin for DataNucleus providing persistence to RDBMS data-stores.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{commit}

# Fix c3p0 gId
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'c3p0' ]/pom:groupId" com.mchange

# Non free
%pom_remove_dep oracle:ojdbc14_g
%pom_remove_dep oracle:xdb
%pom_remove_dep oracle:xmlparser
rm -r src/java/org/datanucleus/store/rdbms/mapping/oracle/Oracle*.java \
 src/java/org/datanucleus/store/rdbms/mapping/oracle/XMLTypeRDBMSMapping.java \
 src/java/org/datanucleus/store/rdbms/adapter/OracleAdapter.java

# Unavailable dep
%pom_remove_dep com.jolbox:bonecp
rm -r src/java/org/datanucleus/store/rdbms/connectionpool/BoneCP*.java
# Required by bonecp
%pom_remove_dep org.slf4j:slf4j-api
%pom_remove_dep org.slf4j:slf4j-log4j12

%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]/pom:configuration/pom:instructions" '
<Require-Bundle>org.datanucleus;bundle-version="${project.version}"</Require-Bundle>
<Bundle-Name>${project.name}</Bundle-Name>
<Bundle-Vendor>DataNucleus</Bundle-Vendor>'
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]" "
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

sed -i 's/\r//' META-INF/LICENSE.txt META-INF/NOTICE.txt META-INF/README.txt
cp -p META-INF/LICENSE.txt .
cp -p META-INF/NOTICE.txt .
cp -p META-INF/README.txt .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.13-alt1_8jpp8
- java update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.13-alt1_7jpp8
- new version

