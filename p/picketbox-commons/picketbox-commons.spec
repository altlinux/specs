# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
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
Release:        alt2_11jpp8
Summary:        Common classes for security projects
Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jboss.org/picketbox

# svn export http://anonsvn.jboss.org/repos/picketbox/commons/tags/1.0.0.final/picketbox-commons/ picketbox-commons-1.0.0.final
# tar cJf picketbox-commons-1.0.0.final.tar.xz picketbox-commons-1.0.0.final
Source0:        %{name}-%{namedversion}.tar.xz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local

Requires:       jpackage-utils
Source44: import.info

%description
Common classes for security projects.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
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
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

