Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
Name:          HikariCP
# Latest release use hibernate-core >= 5.0.9.Final and javassist >= 3.20.0-GA
Version:       2.4.0
Release:       alt1_1jpp8
Summary:       JDBC Connection Pool
# Source files without license headers https://github.com/brettwooldridge/HikariCP/issues/665
License:       ASL 2.0
URL:           http://brettwooldridge.github.io/HikariCP/
Source0:       https://github.com/brettwooldridge/HikariCP/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
%if %{?fedora} < 24
BuildRequires: mvn(com.codahale.metrics:metrics-core)
BuildRequires: mvn(com.codahale.metrics:metrics-healthchecks)
%else
BuildRequires: mvn(io.dropwizard.metrics:metrics-core)
BuildRequires: mvn(io.dropwizard.metrics:metrics-healthchecks)
%endif
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.hibernate:hibernate-core)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(simple-jndi:simple-jndi)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Fast, simple, reliable. HikariCP is a "zero-overhead" production
ready JDBC connection pool.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%if %{?fedora} < 24
%pom_change_dep -r io.dropwizard.metrics: com.codahale.metrics:
%endif

# org.ops4j.pax.exam:pax-exam-container-native:4.5.0
# org.ops4j.pax.exam:pax-exam-junit4:4.5.0
# org.ops4j.pax.exam:pax-exam-link-mvn:4.5.0
%pom_remove_dep org.ops4j.pax.exam:
# org.ops4j.pax.url:pax-url-aether:2.4.1
# org.ops4j.pax.url:pax-url-reference:2.4.1
%pom_remove_dep org.ops4j.pax.url:
rm -r src/test/java/com/zaxxer/hikari/osgi

# package org.junit does not exist
%pom_add_dep junit:junit:4.12:test

%mvn_file : %{name}
%mvn_alias : com.zaxxer:%{name}-java6

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES  README.md TODO.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1jpp8
- new version

