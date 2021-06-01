Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with    itext
%bcond_with    fop

Name:           maven-doxia
Epoch:          0
Version:        1.9.1
Release:        alt1_3jpp11
Summary:        Content generation framework
License:        ASL 2.0

URL:            https://maven.apache.org/doxia/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip

# Build against iText 2.x
# https://issues.apache.org/jira/browse/DOXIA-53
Patch1:         0001-Fix-itext-dependency.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.xmlunit:xmlunit-core)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)

%if %{with fop}
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(log4j:log4j:1.2.12)
BuildRequires:  mvn(org.apache.xmlgraphics:fop)
%endif

%if %{with itext}
BuildRequires:  mvn(com.lowagie:itext)
%endif

Obsoletes:      maven-doxia-book < %{epoch}:%{version}-%{release}
Obsoletes:      maven-doxia-maven-plugin < %{epoch}:%{version}-%{release}
%if %{without fop}
Obsoletes:      maven-doxia-module-fo < %{epoch}:%{version}-%{release}
%endif
%if %{without itext}
Obsoletes:      maven-doxia-module-itext < %{epoch}:%{version}-%{release}
%endif
Obsoletes:      maven-doxia-module-markdown < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package core
Group: Development/Java
Summary: Core module for %{name}

%description core
This package provides %{summary}.

%package logging-api
Group: Development/Java
Summary: Logging-api module for %{name}

%description logging-api
This package provides %{summary}.

%package module-apt
Group: Development/Java
Summary: APT module for %{name}

%description module-apt
This package provides %{summary}.

%package module-confluence
Group: Development/Java
Summary: Confluence module for %{name}

%description module-confluence
This package provides %{summary}.

%package module-docbook-simple
Group: Development/Java
Summary: Simplified DocBook module for %{name}

%description module-docbook-simple
This package provides %{summary}.

%package module-fml
Group: Development/Java
Summary: FML module for %{name}

%description module-fml
This package provides %{summary}.

%if %{with fop}
%package module-fo
Group: Development/Java
Summary: FO module for %{name}

%description module-fo
This package provides %{summary}.
%endif

%if %{with itext}
%package module-itext
Group: Development/Java
Summary: iText module for %{name}

%description module-itext
This package provides %{summary}.
%endif

%package module-latex
Group: Development/Java
Summary: Latex module for %{name}

%description module-latex
This package provides %{summary}.

%package module-rtf
Group: Development/Java
Summary: RTF module for %{name}

%description module-rtf
This package provides %{summary}.

%package modules
Group: Development/Java
Summary: Doxia modules for several markup languages.

%description modules
This package provides %{summary}.

%package module-twiki
Group: Development/Java
Summary: TWiki module for %{name}

%description module-twiki
This package provides %{summary}.

%package module-xdoc
Group: Development/Java
Summary: XDoc module for %{name}

%description module-xdoc
This package provides %{summary}.

%package module-xhtml
Group: Development/Java
Summary: XHTML module for %{name}

%description module-xhtml
This package provides %{summary}.

%package module-xhtml5
Group: Development/Java
Summary: XHTML5 module for %{name}

%description module-xhtml5
This package provides %{summary}.

%package sink-api
Group: Development/Java
Summary: Sink-api module for %{name}

%description sink-api
This package provides %{summary}.

%package tests
Group: Development/Java
Summary: Tests for %{name}

%description tests
This package provides %{summary}.

%package test-docs
Group: Development/Java
Summary: Test-docs module for %{name}
BuildArch: noarch

%description test-docs
This package provides %{summary}.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n doxia-%{version}

find -name '*.java' -exec sed -i 's/\r//' {} +
find -name '*.xml' -exec sed -i 's/\r//' {} +
%patch1 -p1

# we don't have clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin pom.xml

# complains
%pom_remove_plugin :apache-rat-plugin

# use java 5 generics in modello plugin
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]"\
"/pom:executions/pom:execution/pom:configuration" \
"<useJava5>true</useJava5>" doxia-modules/doxia-module-fml/pom.xml

# requires network
rm doxia-core/src/test/java/org/apache/maven/doxia/util/XmlValidatorTest.java

%mvn_package :::tests: tests

%pom_disable_module doxia-module-markdown doxia-modules

%if %{without itext}
%pom_disable_module doxia-module-itext doxia-modules
%endif
%if %{without fop}
%pom_disable_module doxia-module-fo doxia-modules
%endif

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-doxia
%doc LICENSE NOTICE
%files core -f .mfiles-doxia-core
%files logging-api -f .mfiles-doxia-logging-api
%doc LICENSE NOTICE
%files module-apt -f .mfiles-doxia-module-apt
%files module-confluence -f .mfiles-doxia-module-confluence
%files module-docbook-simple -f .mfiles-doxia-module-docbook-simple
%files module-fml -f .mfiles-doxia-module-fml
%if %{with fop}
%files module-fo -f .mfiles-doxia-module-fo
%endif
%if %{with itext}
%files module-itext -f .mfiles-doxia-module-itext
%endif
%files module-latex -f .mfiles-doxia-module-latex
%files module-rtf -f .mfiles-doxia-module-rtf
%files modules -f .mfiles-doxia-modules
%files module-twiki -f .mfiles-doxia-module-twiki
%files module-xdoc -f .mfiles-doxia-module-xdoc
%files module-xhtml -f .mfiles-doxia-module-xhtml
%files module-xhtml5 -f .mfiles-doxia-module-xhtml5
%files sink-api -f .mfiles-doxia-sink-api
%files test-docs -f .mfiles-doxia-test-docs
%files tests -f .mfiles-tests
%doc LICENSE NOTICE
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

