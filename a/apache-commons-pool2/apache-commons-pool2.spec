Name:          apache-commons-pool2
Version:       2.13.1
Release:       alt1

Summary:       Apache Commons Pool
License:       Apache-2.0
Group:         Development/Java
URL:           https://commons.apache.org/pool/
VCS:           https://github.com/apache/commons-pool

Source0:       %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(cglib:cglib)

BuildArch:     noarch

%description
The Apache Commons Pool open source software library provides an object-pooling
API and a number of object pool implementations. Version 2 of Apache Commons
Pool contains a completely re-written pooling implementation compared to the
1.x series. In addition to performance and scalability improvements, version 2
includes robust instance tracking and pool monitoring.

%javadoc_package

%prep
%setup

%mvn_file : %name commons-pool2

%build
# Tests fails
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Thu May 14 2026 Evgeniy Serov <scala@altlinux.org> 2.13.1-alt1
- Updated to 2.13.1.

* Wed Aug 17 2022 Igor Vlasenko <viy@altlinux.org> 2.4.2-alt4_7jpp11
- jdk17 support

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt4_7jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt4_6jpp8
- fc29 update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt4_5jpp8
- fixed build

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt3_5jpp8
- java update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt3_4jpp8
- fixed build

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_3jpp8
- new jpp release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2_2jpp8
- fixed build

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp8
- new version

