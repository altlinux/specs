Name:           maven-doxia
Version:        2.0.0
Release:        alt1

Summary:        Apache Maven Doxia base
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/doxia/
VCS:            https://github.com/apache/maven-doxia

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-abbreviation)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-definition)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-escaped-character)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-footnotes)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-gfm-strikethrough)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-tables)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-typographic)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-wikilink)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-yaml-front-matter)
BuildRequires:  mvn(org.jetbrains:annotations)

BuildArch:      noarch

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%javadoc_package

%package        core
Summary:        Doxia core classes and interfaces
Group:          Development/Java

%description    core
%summary.

%package        modules
Summary:        Doxia modules for several markup languages
Group:          Development/Java

%description    modules
%summary.

%package        module-apt
Summary:        Doxia APT Module
Group:          Development/Java

%description    module-apt
A Doxia module for Almost Plain Text source documents.
APT format is supported both as source and target formats.

%package        module-fml
Summary:        Doxia FML Module
Group:          Development/Java

%description    module-fml
A Doxia module for FML source documents.
FML format is only supported as source format.

%package        module-markdown
Summary:        Doxia Markdown Module
Group:          Development/Java

%description    module-markdown
A Doxia module for Markdown source documents.

%package        module-xdoc
Summary:        Doxia XDoc Module
Group:          Development/Java

%description    module-xdoc
A Doxia module for Xdoc source documents.
Xdoc format is supported both as source and target formats.

%package        module-xhtml5
Summary:        Doxia XHTML5 Module
Group:          Development/Java

%description    module-xhtml5
A Doxia module for Xhtml5 source documents.
Xhtml5 format is supported both as source and target formats.

%package        sink-api
Summary:        Doxia Sink API
Group:          Development/Java

%description    sink-api
%summary.

%package        test-docs
Summary:        Doxia Test Documents
Group:          Development/Java

%description    test-docs
Several test documents to check syntax structures under Doxia.

%prep
%setup

%pom_remove_parent

# requires network
rm doxia-core/src/test/java/org/apache/maven/doxia/util/XmlValidatorTest.java

%pom_remove_plugin :maven-install-plugin doxia-modules/doxia-module-markdown

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles-doxia
%doc README.md

%files core -f .mfiles-doxia-core
%files module-apt -f .mfiles-doxia-module-apt
%files module-fml -f .mfiles-doxia-module-fml
%files module-markdown -f .mfiles-doxia-module-markdown
%files modules -f .mfiles-doxia-modules
%files module-xdoc -f .mfiles-doxia-module-xdoc
%files module-xhtml5 -f .mfiles-doxia-module-xhtml5
%files sink-api -f .mfiles-doxia-sink-api
%files test-docs -f .mfiles-doxia-test-docs

%changelog
* Thu Mar 19 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt1
- Udated to 2.0.0.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.1-alt1_3jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9-alt1_4jpp8
- new version

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_10jpp8
- build w/o tests - support for fop 2.4

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_10jpp8
- new version

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_5jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_5jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp8
- java8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp7
- fixed build

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp7
- use fc geronimo

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

