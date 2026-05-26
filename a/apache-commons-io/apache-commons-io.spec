Name:           apache-commons-io
Epoch:          1
Version:        2.22.0
Release:        alt1

Summary:        Apache Commons IO
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/io
VCS:            https://github.com/apache/commons-io

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
The Apache Commons IO library contains utility classes, stream implementations,
file filters, file comparators, endian transformation classes, and much more.

%javadoc_package

%prep
%setup

%mvn_file  : commons-io %name
%mvn_alias : org.apache.commons:

%build
# Tests disabled due missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt *.md

%changelog
* Sat May 16 2026 Evgeniy Serov <scala@altlinux.org> 1:2.22.0-alt1
- Updated to 2.22.0.

* Mon Jul 07 2025 Andrey Cherepanov <cas@altlinux.org> 1:2.19.0-alt1
- new version

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 1:2.11.0-alt1_2jpp11
- update

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1:2.8.0-alt1_5jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:2.8.0-alt1_3jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_6jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.6-alt1_1jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_3jpp8
- fc27 update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt2_2jpp8
- fixed build with new testng

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.5-alt1_2jpp8
- new version

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt6_15jpp8
- fixed build

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_15jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt5_14jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt1_2jpp7
- new release

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp6
- added osgi manifest

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp6
- added compat mapping

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp6
- renamed

