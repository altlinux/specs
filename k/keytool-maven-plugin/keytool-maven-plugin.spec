%define _unpackaged_files_terminate_build 1

Name: keytool-maven-plugin
Version: 2.0.2
Release: alt1

Summary: A plugin that wraps the keytool program and allows to manipulate keystores
Group: Development/Other
License: Apache-2.0
Url: https://www.mojohaus.org/keytool/
Vcs: https://github.com/mojohaus/keytool

Source0: %{name}-%{version}.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mojo-parent
BuildRequires: maven-plugin-plugin
BuildRequires: bouncycastle-pkix
BuildRequires: slf4j
BuildRequires: atinject
BuildRequires: sisu-mojos
BuildRequires: maven-plugin-plugin
BuildRequires: maven-invoker-plugin

%description
A plugin that wraps the keytool program bundled with Sun's Java SDK.
It provides the capability to manipulate keys and keystores
with the goals "keytool:genkey" and "keytool:clean".

%package javadoc
Summary: API documentation for %{name}
Group: Development/Java

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup

%build
# To run the tests correctly, you need to update maven to version 3.9.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jun 08 2026 Arseniy Kostevich <faux@altlinux.org> 2.0.2-alt1
- New version (Closes: #59468).

* Sun Nov 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0-alt9_18jpp11
- Fix FTBFS.

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt8_18jpp11
- fixed build

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt7_18jpp8
- fixed build with new maven-reporting-impl

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6_18jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_18jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_12jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5_7jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_7jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_7jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

