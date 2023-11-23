Epoch: 0
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jfreechart
Version:        1.5.4
Release:        alt1_2jpp11
Summary:        A 2D chart library for Java applications (JavaFX, Swing or server-side)
License:        LGPLv2+
URL:            https://www.jfree.org/jfreechart
BuildArch:      noarch

Source0:        https://github.com/jfree/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:servlet-api)
# need apiguardian-api until Fedora releases junit >= 5.8.0 (1)
# link:
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#deprecations-and-breaking-changes
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#new-features-and-improvements
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
Source44: import.info

%description
JFreeChart is a comprehensive free chart library for the Java platform that can
be used on the client-side (JavaFX and Swing) or the server side (with export to
multiple formats including SVG, PNG and PDF).

%{?javadoc_package}

%prep
%setup -q


# (1)
%pom_add_dep org.apiguardian:apiguardian-api:1.1.1

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference licence-LGPL.txt
%doc README.md

%changelog
* Thu Nov 23 2023 Igor Vlasenko <viy@altlinux.org> 0:1.5.4-alt1_2jpp11
-new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.5.3-alt1_3jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 0:1.0.19-alt1_19jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:1.0.19-alt1_18jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.0.19-alt1_16jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_13jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_11jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_6jpp8
- new jpp release

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_4jpp8
- fixed build

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.19-alt1_3jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_3jpp7
- new fc release

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_2jpp7
- added jpp compat symlink

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt2_2jpp7
- added jfreechart:jfreechart depmap

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt1_2jpp7
- new version

* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt3_3jpp6
- fixed repolib dep on jcommon

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_3jpp6
- new jpp relase

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_2jpp6
- fixed jcommon version in repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_4jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
