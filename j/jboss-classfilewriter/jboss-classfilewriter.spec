Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-classfilewriter
%define version 1.1.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-classfilewriter
Version:          1.1.2
Release:          alt1_1jpp8
Summary:          JBoss Class File Writer
License:          ASL 2.0
URL:              https://github.com/jbossas/jboss-classfilewriter
Source0:          https://github.com/jbossas/jboss-classfilewriter/archive/%{namedversion}.tar.gz
# https://github.com/jbossas/jboss-classfilewriter/issues/11
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
This package contains JBoss Class File Writer

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1jpp7
- new version

