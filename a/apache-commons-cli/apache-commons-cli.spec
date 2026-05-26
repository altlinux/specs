Name:           apache-commons-cli
Version:        1.11.0
Release:        alt1

Summary:        Apache Commons CLI
License:        Apache-2.0
Group:          Development/Java
URL:            http://commons.apache.org/cli/
VCS:            https://github.com/apache/commons-cli

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
Apache Commons CLI provides a simple API for presenting, processing, and
validating a Command Line Interface.

%javadoc_package

%prep
%setup

%mvn_alias : org.apache.commons:commons-cli
%mvn_file : commons-cli %name

%build
# Tests disabled due missing dep junit-pioneer (gradle)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Wed May 13 2026 Evgeniy Serov <scala@altlinux.org> 1.11.0-alt1
- Updated to 1.11.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.5.0-alt1_3jpp11
- new version

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:1.4-alt1_14jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.4-alt1_11jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp8
- java update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp8
- new jpp release

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_7jpp7
- fc update

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_6jpp6
- add obsoletes

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp6
- fixed repolib

