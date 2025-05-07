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

%bcond_with bootstrap

Name:           maven-plugin-tools
Version:        3.6.4
Release:        alt1

Summary:        Maven Plugin Tools
License:        Apache-2.0
URL:            http://maven.apache.org/plugin-tools/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:         0001-Disable-help-MOJO-generation.patch
Patch2:         0002-Remove-dependency-on-jtidy.patch
Patch3:         0003-Disable-reporting.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Group: Development/Java
Summary:        Maven Plugin Java 5 Annotations
#Obsoletes:      maven-plugin-annotations < 0:%{version}-%{release}

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n maven-plugin-plugin
Group: Development/Java
Summary:        Maven Plugin Plugin

%description -n maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package annotations
Group: Development/Java
Summary:        Maven Plugin Tool for Annotations

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%package api
Group: Development/Java
Summary:        Maven Plugin Tools APIs
Obsoletes:      maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package generators
Group: Development/Java
Summary:        Maven Plugin Tools Generators

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Group: Development/Java
Summary:        Maven Plugin Tool for Java
Obsoletes:      maven-shared-plugin-tools-java < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-java = 0:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

# Obsoletes can be removed in Fedora 40 -- maven-plugin-tools-javadocs

# was renamed to maven-plugin-tools-javadoc in Fedora 38.

Obsoletes:      %{name}-javadocs < 3.6.4

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_xpath_remove "pom:execution[pom:id='generated-helpmojo']" maven-plugin-plugin

%pom_disable_module maven-script

%pom_remove_dep -r :maven-reporting-impl
%pom_remove_dep -r :maven-reporting-api
%pom_remove_dep -r :plexus-velocity
%pom_remove_dep -r :velocity
%pom_remove_dep -r :jtidy
%pom_remove_dep -r :doxia-sink-api
%pom_remove_dep -r :doxia-site-renderer
%pom_remove_dep :maven-plugin-tools-ant maven-plugin-plugin
%pom_remove_dep :maven-plugin-tools-beanshell maven-plugin-plugin

rm maven-plugin-tools-generators/src/main/java/org/apache/maven/tools/plugin/generator/Plugin{Help,Xdoc}Generator.java
rm maven-plugin-plugin/src/main/java/org/apache/maven/plugin/plugin/PluginReport.java

%build
%mvn_build -s -f

%install
%mvn_install


%files -f .mfiles-maven-plugin-tools
%doc --no-dereference LICENSE NOTICE

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations
%doc --no-dereference LICENSE NOTICE

%files -n maven-plugin-plugin -f .mfiles-maven-plugin-plugin

%files annotations -f .mfiles-maven-plugin-tools-annotations
%doc --no-dereference LICENSE NOTICE

%files api -f .mfiles-maven-plugin-tools-api
%doc --no-dereference LICENSE NOTICE

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed May 07 2025 Anton Meleshnikov <alton@altlinux.org> 3.6.4-alt1
- New version 3.6.4 (thanks fedora for the spec).

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.6.0-alt1_7jpp11
- new version

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt2_7jpp8
- fixed build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_7jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_5jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_4jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_14jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_5jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt3_5jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

