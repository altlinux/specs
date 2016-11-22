Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox
%define version 4.0.21
%global namedreltag .Beta1
%global namedversion %{version}%{?namedreltag}

Name:             picketbox
Version:          4.0.21
Release:          alt1_0.3.Beta1jpp8
Summary:          Security framework for Java Applications
License:          LGPLv2+
URL:              http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/picketbox/tags/4.0.20.Final/ picketbox-4.0.20.Final
# tar cafJ picketbox-4.0.20.Final.tar.xz picketbox-4.0.20.Final
Source0:          https://github.com/picketbox/picketbox/archive/%{namedversion}.tar.gz
Source1:          picketbox-%{namedversion}-pom.xml

Patch0:           picketbox-%{namedversion}-assembly.patch

BuildArch:        noarch

BuildRequires:    concurrent
BuildRequires:    hibernate-jpa-2.0-api >= 1.0.1
BuildRequires:    hibernate3
BuildRequires:    hibernate3-entitymanager
BuildRequires:    hibernate-commons-annotations
BuildRequires:    hsqldb
BuildRequires:    infinispan
BuildRequires:    javacc-maven-plugin
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-jacc-1.5-api
BuildRequires:    jboss-jaspi-1.1-api
BuildRequires:    jboss-parent
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    geronimo-jpa
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    maven-local
BuildRequires:    jboss-logging-tools
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    picketbox-commons
BuildRequires:    picketbox-xacml
BuildRequires:    rhq-plugin-annotations
Source44: import.info

%description
Java Security Framework that provides Java developers the following
functionality:

- Authentication Support
- Authorization Support
- Audit Support
- Security Mapping Support
- An Oasis XACML v2.0 compliant engine

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n picketbox-%{namedversion}

%patch0 -p1

# Change hibernate version
sed -i 's|3.6.6.Final|3|g' security-jboss-sx/acl/pom.xml

%pom_remove_dep "org.hibernate:hibernate-annotations" security-jboss-sx/acl/pom.xml

%build
%mvn_build -f

%install
%mvn_install

# Assembly jar
install -pm 644  assembly/target/picketbox-%{namedversion}-bin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.21-alt1_0.3.Beta1jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.21-alt1_0.2.Beta1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.18-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.6-alt1_7jpp7
- new version

