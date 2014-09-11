Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jetty-build-support
Version:        1.1
Release:        alt3_8jpp7
Summary:        Jetty build support files

Group:          Development/Java
# licensing bug upstream
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=362646
# - commit stating the license is already there
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
#Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-enforcer-api
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  jetty-toolchain
BuildRequires:  junit4

Requires:       maven
Requires:       maven-project
Requires:       maven-enforcer
Requires:       jpackage-utils
Requires:       jetty-toolchain
Requires:       maven-enforcer-api
Requires:       plexus-containers-container-default
Source44: import.info

%description
Build Support for Jetty. Contains enforcer rules, PMD rulesets, etc.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%doc jetty-distribution-remote-resources/src/main/resources/*

%files javadoc -f %{name}/.mfiles-javadoc
%doc jetty-distribution-remote-resources/src/main/resources/*

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_2jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_2jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp7
- new version

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp6
- new jpp release

