Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             owasp-esapi-java
Version:          2.1.0
Release:          alt1_5jpp8
Summary:          OWASP Enterprise Security API
License:          BSD
URL:              https://www.owasp.org/index.php/Main_Page
# 3.x series is available @ https://github.com/ESAPI/esapi-java/
Source0:          https://github.com/ESAPI/esapi-java-legacy/archive/esapi-%{version}.tar.gz

# Antisammy is not available
Patch0:           0001-Remove-validator-implementation-bsed-on-Antisammy.patch
# Use different directory in tests
Patch1:           0002-Use-different-directory-to-testing-bin-is-a-symlink.patch
# Missing implementations
Patch2:           0003-Implement-missing-servlet-3.0-methods-in-mock.patch
Patch3:           owasp-esapi-java-2.1.0-servlet3.1.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(commons-beanutils:commons-beanutils-core)
BuildRequires:    mvn(commons-collections:commons-collections)
BuildRequires:    mvn(commons-configuration:commons-configuration)
BuildRequires:    mvn(commons-fileupload:commons-fileupload)
BuildRequires:    mvn(commons-io:commons-io)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.apache.tomcat:tomcat-jsp-api)
BuildRequires:    mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:    mvn(org.beanshell:bsh)
BuildRequires:    mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:    mvn(xom:xom)
Source44: import.info

%description
OWASP ESAPI (The OWASP Enterprise Security API) is a free, open source,
web application security control library that makes it easier for programmers
to write lower-risk applications. The ESAPI for Java library is designed to
make it easier for programmers to retrofit security into existing applications.
ESAPI for Java also serves as a solid foundation for new development. 

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package doc
Group: Development/Java
Summary:          Documentation for %{name}
License:          CC-BY-SA

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q -n esapi-java-legacy-esapi-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Plugin not available
%pom_remove_plugin "org.codehaus.mojo:versions-maven-plugin"
# Unwanted task
%pom_remove_plugin "org.apache.maven.plugins:maven-eclipse-plugin"

# Atisammy not available
%pom_remove_dep "org.owasp.antisamy:antisamy"

%pom_change_dep ":bsh-core" "org.beanshell:bsh"

%pom_change_dep ":log4j" "::12"
%pom_change_dep "javax.servlet:jsp-api" "org.apache.tomcat:tomcat-jsp-api"
%pom_change_dep "javax.servlet:servlet-api" "org.apache.tomcat:tomcat-servlet-api"

sed -i "s|public void testSetCookie()|public void ignoredSetCookie()|" src/test/java/org/owasp/esapi/reference/HTTPUtilitiesTest.java

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE-README

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-README

%files doc
%doc documentation/*
%doc LICENSE-CONTENT LICENSE-README

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_5jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_9jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_7jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3jpp7
- fixed build

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp7
- fc update

