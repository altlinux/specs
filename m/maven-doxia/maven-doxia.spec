Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%if 0%{?fedora}
%bcond_without itext
%bcond_without markdown
%endif

Name:           maven-doxia
Version:        1.6
Release:        alt1_5jpp8
Epoch:          0
Summary:        Content generation framework
License:        ASL 2.0
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip

# Build against iText 2.x
# https://issues.apache.org/jira/browse/DOXIA-53
Patch1:         0001-Fix-itext-dependency.patch

# Forwarded upstream: DOXIA-504
Patch2:         0002-Update-to-Plexus-Container-1.5.5.patch

# Accepted upstream: DOXIA-505
Patch3:         0003-Update-to-Commons-Collections-1.10.patch

# Don't run bad tests which rely on ordering in set (they fail with Java 8)
Patch4:         0004-Disable-tests-which-rely-on-ordering-in-set.patch

# Not upstreamable due to higher Java version of fop's dependencies
Patch5:         0005-Port-to-fop-2.0.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core::tests:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-logging-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-modules:pom:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia:pom:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-test-docs)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.xmlgraphics:fop)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xmlunit:xmlunit)
%if %{with itext}
BuildRequires:  mvn(com.lowagie:itext)
%endif
%if %{with markdown}
BuildRequires:  mvn(org.pegdown:pegdown)
%endif

Obsoletes:      maven-doxia-book < %{epoch}:%{version}-%{release}
Obsoletes:      maven-doxia-maven-plugin < %{epoch}:%{version}-%{release}
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

%package module-fo
Group: Development/Java
Summary: FO module for %{name}

%description module-fo
This package provides %{summary}.

%if %{with itext}
%package module-itext
Group: Development/Java
Summary: iText module for %{name}

%description module-itext
This package provides %{summary}.
%endif

%if %{with markdown}
%package module-markdown
Group: Development/Java
Summary: Markdown module for %{name}

%description module-markdown
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# we don't have clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin pom.xml

# use java 5 generics in modello plugin
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]"\
"/pom:executions/pom:execution/pom:configuration" \
"<useJava5>true</useJava5>" doxia-modules/doxia-module-fml/pom.xml

%mvn_package :::tests: tests

%if %{without itext}
%pom_disable_module doxia-module-itext doxia-modules
%endif
%if %{without markdown}
%pom_disable_module doxia-module-markdown doxia-modules
%endif

%build
%mvn_build -s

%install
%mvn_install


%files -f .mfiles-doxia
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE
%files core -f .mfiles-doxia-core
%files logging-api -f .mfiles-doxia-logging-api
%doc LICENSE NOTICE
%files module-apt -f .mfiles-doxia-module-apt
%files module-confluence -f .mfiles-doxia-module-confluence
%files module-docbook-simple -f .mfiles-doxia-module-docbook-simple
%files module-fml -f .mfiles-doxia-module-fml
%files module-fo -f .mfiles-doxia-module-fo
%if %{with itext}
%files module-itext -f .mfiles-doxia-module-itext
%endif
%if %{with markdown}
%files module-markdown -f .mfiles-doxia-module-markdown
%endif
%files module-latex -f .mfiles-doxia-module-latex
%files module-rtf -f .mfiles-doxia-module-rtf
%files modules -f .mfiles-doxia-modules
%files module-twiki -f .mfiles-doxia-module-twiki
%files module-xdoc -f .mfiles-doxia-module-xdoc
%files module-xhtml -f .mfiles-doxia-module-xhtml
%files sink-api -f .mfiles-doxia-sink-api
%files test-docs -f .mfiles-doxia-test-docs
%files tests -f .mfiles-tests
%doc LICENSE NOTICE
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
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

