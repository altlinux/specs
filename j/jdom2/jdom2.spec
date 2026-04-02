Name:           jdom2
Version:        2.0.6.1
Release:        alt1.1

Summary:        Java manipulation of XML made easy
License:        Saxpath
Group:          Development/Java
URL:            http://www.jdom.org/
VCS:            https://github.com/hunterhacker/jdom

Source0:        %name-%version.tar
Source3:        bnd.properties
# Remove bundled jars that might not have clear licensing
Source4:        generate-tarball.sh

Patch0:         0001-Adapt-build.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  ant
BuildRequires:  ant-junit

BuildArch:      noarch

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%prep
%setup
%autopatch -p1

sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

%build
%ant -Dversion=%version -Dcompile.source=1.8 -Dcompile.target=1.8 maven

%install
%mvn_artifact build/maven/core/%name-%version.pom build/package/jdom-%version.jar
%mvn_install

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt LICENSE.txt

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.0.6.1-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 2.0.6.1-alt1
- Updated to 2.0.6.1.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_27jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_23jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_21jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.0.6-alt1_19jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_15jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_13jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_5jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_4jpp8
- new version

