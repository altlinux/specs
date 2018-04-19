Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-distribution-remote-resources
Version:        1.1
Release:        alt3_14jpp8
Summary:        Jetty toolchain artifact for distribution remote resources

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  jetty-toolchain

Requires:       jpackage-utils
Requires:       maven
Requires:       maven-remote-resources-plugin
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/LICENSE*

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

