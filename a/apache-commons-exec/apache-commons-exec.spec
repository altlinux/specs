Name:           apache-commons-exec
Version:        1.6.0
Release:        alt1

Summary:        Apache Commons Exec
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/exec/
VCS:            https://github.com/apache/commons-exec

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
Apache Commons Exec is a library that reliably executes external processes from
within the JVM.

%javadoc_package

%prep
%setup

%build
# Tests disabled due missing dep (gradle)
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Thu May 14 2026 Evgeniy Serov <scala@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt1_22jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt1_17jpp11
- update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_13jpp8
- fc update

* Thu Jul 18 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_11jpp8
- new version

* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_8jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_7jpp8
- fixed build

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp8
- new fc release; disabled tests due to network dependency

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp8
- java8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp7
- new version

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp7
- new version

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_6jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_6jpp6
- renamed; new jpp version

