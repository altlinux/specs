Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          ldaptive
Version:       1.1.0
Release:       alt1_1jpp8
Summary:       LDAP library for Java
License:       ASL 2.0 or LGPLv3
URL:           http://www.ldaptive.org/
Source0:       https://github.com/vt-middleware/ldaptive/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove migbase64 and use Java 8 base64 encoder and decoder
Patch0:        https://github.com/vt-middleware/ldaptive/commit/44a0d8222f27eef7b848316ef136dc539f53c51f.patch

BuildRequires: maven-local
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(com.sun.codemodel:codemodel)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-expression)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
Ldaptive is a simple, extensible Java API for interacting with LDAP servers.
It was designed to provide easy LDAP integration for application developers.

%package beans
Group: Development/Java
Summary:       Ldaptive Beans

%description beans
Mapping, persistence, and code generation API for reading and
writing POJOs to an LDAP directory.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package json
Group: Development/Java
Summary:       Ldaptive Json

%description json
Provides JSON reader and writer.

%package parent
Group: Development/Java
Summary:       Ldaptive Parent POM

%description parent
Ldaptive Parent POM.

%package templates
Group: Development/Java
Summary:       Ldaptive Templates

%description templates
Templating functionality for aggregating LDAP searches.

%prep
%setup -q -n %{name}-%{version}
# Cleanup
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1
rm -f core/src/main/java/org/ldaptive/io/Base64.java

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

%pom_disable_module webapp

cp -p distribution/LICENSE* .
cp -p distribution/NOTICE .

%pom_change_dep -r :ehcache :ehcache-core

%build

# Test suite (disable) use web connection:
# UnknownHostException: buildvm-25.phx2.fedoraproject.org: buildvm-25.phx2.fedoraproject.org: unknown error
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc LICENSE* NOTICE

%files beans -f .mfiles-%{name}-beans
%files javadoc -f .mfiles-javadoc
%doc LICENSE* NOTICE

%files json -f .mfiles-%{name}-json
%files parent -f .mfiles-%{name}-parent
%doc LICENSE* NOTICE

%files templates -f .mfiles-%{name}-templates

%changelog
* Wed Dec 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp8
- new version

