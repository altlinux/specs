Name:           plexus-pom
Version:        25
Release:        alt1.1

Summary:        Root Plexus Projects POM
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-pom/
VCS:            https://github.com/codehaus-plexus/plexus-pom

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:      noarch

%description
The Plexus project provides a full software stack for creating and
executing software projects. This package provides parent POM for
Plexus packages.

%prep
%setup

%pom_xpath_remove pom:extensions

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :spotless-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 25-alt1.1
- Cosmetic fixes.

* Tue Feb 17 2026 Evgeniy Serov <scala@altlinux.org> 25-alt1
- Updated to 25.

* Thu Aug 21 2025 Ilya Muhamadeev <nicourced@altlinux.org> 23-alt1
- New version.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 7-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 7-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 6.4-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 5.1-alt1_2jpp8
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_6jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_5jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt1_4jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp7
- new version

