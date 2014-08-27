Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name arquillian-core
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           arquillian-core
Version:        1.0.3
Release:        alt1_2jpp7
Summary:        Arquillian is a revolutionary testing platform built on the JVM
License:        ASL 2.0
URL:            http://www.jboss.org/arquillian
Source0:        https://github.com/arquillian/arquillian-core/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jboss-parent
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-enforcer-plugin

BuildRequires:    apiviz
BuildRequires:    junit4

BuildRequires:    shrinkwrap
BuildRequires:    shrinkwrap-descriptors
BuildRequires:    shrinkwrap-resolver
BuildRequires:    cdi-api
BuildRequires:    weld-core
BuildRequires:    weld-parent
BuildRequires:    slf4j
BuildRequires:    testng
BuildRequires:    geronimo-ejb
BuildRequires:    geronimo-annotation
BuildRequires:    jboss-el-2.2-api
BuildRequires:    mockito
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-servlet-3.0-api
Source44: import.info

%description
Arquillian is a revolutionary testing platform built on the JVM that
substantially reduces the effort required to write and execute Java 
middleware integration and functional tests. No more mocks. 
No more container lifecycle and deployment hassles. Just real tests!

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q  -n %{name}-%{namedversion}

# Unsupported TestNG version
rm testng/core/src/test/java/org/jboss/arquillian/testng/*.java

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin build/pom.xml

%build
export MAVEN_OPTS="-Xms256m -Xmx768m -XX:PermSize=128m -XX:MaxPermSize=256m"
# JUnit test failures
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc license.txt apl.txt readme.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt apl.txt

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3_1jpp7
- fixed build with xmvn

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

