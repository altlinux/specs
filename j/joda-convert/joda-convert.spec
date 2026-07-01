Name:           joda-convert
Version:        2.2.4
Release:        alt2

Summary:        Java library for conversion to and from standard string formats
License:        Apache-2.0
Group:          Development/Java
URL:            https://www.joda.org/joda-convert/
VCS:            https://github.com/JodaOrg/joda-convert

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.threeten:threetenbp)

BuildArch:      noarch

%description
Java library to enable conversion to and from standard string formats.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt *.md

%changelog
* Mon Jun 29 2026 Evgeniy Serov <scala@altlinux.org> 2.2.4-alt2
- Fixed FTBFS: fix build with JDK 17.

* Thu Mar 12 2026 Evgeniy Serov <scala@altlinux.org> 2.2.4-alt1
- Updated to 2.2.4.
- Returned to Sisyphus.

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_6jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_3jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1_1jpp8
- new version

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_1jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp8
- unbootsrap build

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

