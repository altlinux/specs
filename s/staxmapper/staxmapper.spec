Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name staxmapper
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             staxmapper
Version:          1.1.0
Release:          alt2_10jpp8
Summary:          StAX Mapper
License:          LGPLv2+
URL:              https://github.com/jbossas/staxmapper

# git clone git://github.com/jbossas/staxmapper.git
# cd staxmapper/ && git archive --format=tar --prefix=staxmapper-1.1.0.Final/ 1.1.0.Final | xz > staxmapper-1.1.0.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    jboss-parent
Source44: import.info

%description
This package contains the StAX Mapper.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_4jpp7
- new version

