Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.2.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common-tools
Version:          1.2.2
Release:          alt1_4jpp8
Summary:          JBossWS Common Tools
License:          LGPLv2+ and ASL 2.0
URL:              http://jbossws.jboss.org

Source0:          https://github.com/jbossws/jbossws-common-tools/archive/%{name}-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(gnu.getopt:java-getopt)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.jboss.ws:jbossws-api)
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
Source44: import.info

%description
JBoss Web Services - Common Tools.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

cp %{SOURCE1} .

%pom_xpath_set pom:properties/pom:log4j.version 12

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_6jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_5jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- update

