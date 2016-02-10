Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             cxf-xjc-utils
Version:          2.6.2
Release:          alt1_3jpp8
Summary:          Apache CXF XJC-Utils
License:          ASL 2.0
URL:              http://cxf.apache.org/xjc-utils.html

# svn export http://svn.apache.org/repos/asf/cxf/xjc-utils/tags/xjc-utils-2.6.2/ cxf-xjc-utils-2.6.2
# tar cafJ cxf-xjc-utils-2.6.2.tar.xz cxf-xjc-utils-2.6.2

Source0:          cxf-xjc-utils-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    cxf-build-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    apache-commons-lang
BuildRequires:    glassfish-jaxb
BuildRequires:    glassfish-jaxb-api
BuildRequires:    junit
BuildRequires:    jvnet-parent
BuildRequires:    maven-project
BuildRequires:    maven-shared-downloader
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    ws-jaxme
BuildRequires:    wsdl4j
Source44: import.info

%description
The Apache CXF XJC-Utils provides a bunch of utilities for working
with JAXB to generate better or more usable code.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_disable_module bug671

# maven-checkstyle-plugin:2.12:checkstyle (validate) on project cxf-xjc-plugin:
# An error has occurred in Checkstyle report generation.
# Failed during checkstyle configuration: cannot initialize module TreeWalker
# - Unable to instantiate JUnitTestCase: Unable to instantiate JUnitTestCaseCheck -> [Help 1]
%pom_remove_plugin -r :maven-checkstyle-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.2-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_3jpp7
- new version

