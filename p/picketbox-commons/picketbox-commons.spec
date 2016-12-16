Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name picketbox-commons
%define version 1.0.0
%global namedreltag .final
%global namedversion %{version}%{?namedreltag}

Name:           picketbox-commons
Version:        1.0.0
Release:        alt2_13jpp8
Summary:        Common classes for security projects
License:        LGPLv2+
URL:            http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/picketbox/commons/tags/1.0.0.final/picketbox-commons/ picketbox-commons-1.0.0.final
# tar cJf picketbox-commons-1.0.0.final.tar.xz picketbox-commons-1.0.0.final
Source0:        %{name}-%{namedversion}.tar.xz

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Common classes for security projects.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new version

