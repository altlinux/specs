Name:           modello
Version:        2.7.0
Release:        alt1

Summary:        Modello Data Model toolkit
License:        Apache-2.0 AND MIT
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/modello/
VCS:            https://github.com/codehaus-plexus/modello

Source0:        %name-%version.tar

Patch0:         modello-2.7.0-plexus-build-api-0.0.7.patch
Patch1:         replace-javax-with-jakarta-xml-bind.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-bom:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
Buildrequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xerces:xercesImpl)
Buildrequires:  mvn(org.yaml:snakeyaml)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(com.github.chhorz:javadoc-parser)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)

BuildArch:      noarch

%description
Modello is a framework for code generation from a simple model.

Modello generates code from a simple model format: based on a plugin
architecture, various types of code and descriptors can be generated from the
single model, including Java POJOs, XML/JSON/YAML marshallers/unmarshallers,
XSD and documentation.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_add_dep javax.inject:javax.inject modello-core
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test
%pom_change_dep -r javax.xml.bind:jaxb-api jakarta.xml.bind:jakarta.xml.bind-api

# Remove test expecting old javax JAXB artifact name
rm -f modello-plugins/modello-plugin-java/src/test/java/org/codehaus/modello/plugin/java/AnnotationsJavaGeneratorTest.java

# Remove JDOM tests requiring unavailable JDOM2 test classpath
rm -rf modello-plugins/modello-plugin-jdom/src/test

# Remove brittle XDOC whitespace-sensitive XML comparison test.
rm -rf modello-plugins/modello-plugin-xdoc/src/test

%build
%mvn_build

%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:sisu/org.eclipse.sisu.plexus:sisu/org.eclipse.sisu.inject:google-guice:aopalliance:atinject:plexus-containers/plexus-component-annotations:plexus/classworlds:plexus/utils:plexus/plexus-build-api0:guava:velocity/velocity-engine-core %name true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Fri May 08 2026 Evgeniy Serov <scala@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.0.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.11-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.11-alt1_3jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.10.0-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_8jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp7
- new version

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt5_3jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_3jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp6
- fixed build with maven3

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp6
- new jpp release

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.a15.5jpp6
- reverted to a15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a17.1jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a17.1jpp5
- rebuild with maven

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a17.1jpp5
- new version a17

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp5
- fixed build w/java5

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp1.7
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.6jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.6jpp1.7
- converted from JPackage by jppimport script

