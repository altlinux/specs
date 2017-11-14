Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  markdown
%bcond_without  fop

%global parent maven-doxia
%global subproj sitetools

Name:           %{parent}-%{subproj}
Version:        1.7.4
Release:        alt1_4jpp8
Summary:        Doxia content generation framework
License:        ASL 2.0
URL:            http://maven.apache.org/doxia/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-%{subproj}-%{version}-source-release.zip

Patch0:         0001-Port-to-plexus-utils-3.0.24.patch
Patch1:         0002-Remove-dependency-on-velocity-tools.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-logging-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fml)
%if %{with fop}
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fo)
%endif
%if %{with markdown}
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-markdown)
%endif
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)

Provides:      maven-doxia-tools = %{version}-%{release}
Obsoletes:     maven-doxia-tools < 1.7
Source44: import.info

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n doxia-%{subproj}-%{version}
%patch0 -p1
%patch1 -p1

# complains
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_dep net.sourceforge.htmlunit:htmlunit doxia-site-renderer/pom.xml
%pom_remove_dep -r :velocity-tools

%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]/pom:configuration" \
    "<useJava5>true</useJava5>" doxia-decoration-model

# There are two backends for generating PDFs: one based on iText and
# one using FOP.  iText module is broken and only brings additional
# dependencies.  Besides that upstream admits that iText support will
# likely removed in future versions of Doxia.  In Fedora we remove
# iText backend sooner in order to fix dependency problems.
#
# See also: http://maven.apache.org/doxia/faq.html#How_to_export_in_PDF
# http://lists.fedoraproject.org/pipermail/java-devel/2013-April/004742.html
rm -rf $(find -type d -name itext)
%pom_remove_dep -r :doxia-module-itext

%if %{without markdown}
%pom_remove_dep -r :doxia-module-markdown
%endif
%if %{without fop}
%pom_remove_dep -r :doxia-module-fo
rm -r doxia-doc-renderer/src/main/java/org/apache/maven/doxia/docrenderer/pdf/fo
%endif

%mvn_alias :doxia-integration-tools org.apache.maven.shared:maven-doxia-tools

%build
# tests can't run because of missing deps
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_5jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

