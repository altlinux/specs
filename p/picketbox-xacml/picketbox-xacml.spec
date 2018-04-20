Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.8
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          picketbox-xacml
# Newer release are available here https://github.com/picketbox/security-xacml/tags
Version:       2.0.8
Release:       alt1_4jpp8
Summary:       JBoss XACML
# BSD: most of the code in ./jboss-sunxacml
# see ./jboss-sunxacml/src/main/java/org/jboss/security/xacml/sunxacml/AbstractPolicy.java as example
License:       BSD and LGPLv2+
URL:           http://picketbox.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-xacml/tags/2.0.8.Final/ picketbox-xacml-2.0.8.Final
# tar cafJ picketbox-xacml-2.0.8.Final.tar.xz picketbox-xacml-2.0.8.Final
Source0:       %{name}-%{namedversion}.tar.xz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.picketbox:picketbox-commons)
Source44: import.info

%description
JBoss XACML Library

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_disable_module assembly

%pom_change_dep -r :xml-apis xml-apis: jboss-sunxacml jboss-xacml

# https://issues.jboss.org/browse/SECURITY-949
cp -p jboss-sunxacml/src/main/resources/licenses/JBossORG-EULA.txt .
cp -p jboss-sunxacml/src/main/resources/licenses/sunxacml-license.txt .

rm .classpath

%mvn_file :jboss-xacml %{name}
%mvn_file :jboss-sunxacml picketbox-sunxacml
%mvn_alias :jboss-xacml org.jboss.security:jbossxacml
%mvn_package ::pom: __noinstall

%build
# Disabled tests because OpenDS is needed
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference JBossORG-EULA.txt 

%files javadoc -f .mfiles-javadoc
%doc --no-dereference JBossORG-EULA.txt sunxacml-license.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_10jpp8
- new version

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt3_5jpp7
- fixed build

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_3jpp7
- new version

