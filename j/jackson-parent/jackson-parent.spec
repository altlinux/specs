Name:          jackson-parent
Version:       2.22
Release:       alt1

Summary:       Parent pom for all Jackson components
License:       Apache-2.0
Group:         Development/Java
URL:           https://github.com/FasterXML/jackson-parent
VCS:           https://github.com/FasterXML/jackson-parent

Source0:       %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)

BuildArch:     noarch

%description
This project is the ultimate parent pom for Jackson 2.x components: for most
indirectly via jackson-base.

It defines some defaults but much of this has been moved to above-mentioned
jackson-base (and jackson-bom) over 2.x release schedule; this project will
not be used at all with Jackson 3.x.

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/VERSION

%changelog
* Fri Aug 07 2026 Evgeniy Serov <scala@altlinux.org> 2.22-alt1
- Updated to 2.22.

* Thu Apr 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.20-alt1
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11-alt1_2jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10-alt1_2jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.1.2-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_3jpp8
- fc29 update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_3.1jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_2.1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_1.1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.2-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

