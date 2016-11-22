Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-plugin-tools
Version:        3.4
Release:        alt1_4jpp8
Epoch:          0
Summary:        Maven Plugin Tools
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Avoid-duplicate-MOJO-parameters.patch
Patch1:         0002-Deal-with-nulls-from-getComment.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox) >= 2.0
BuildRequires:  mvn(net.sf.jtidy:jtidy)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-ant-factory)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-bsh-factory)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(xmlunit:xmlunit)
Source44: import.info

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Group: Development/Java
Summary:        Maven Plugin Java 5 Annotations
Obsoletes:      maven-plugin-annotations < 0:%{version}-%{release}

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

%package ant
Group: Development/Java
Summary:        Maven Plugin Tool for Ant
Obsoletes:      maven-shared-plugin-tools-ant < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-ant = 0:%{version}-%{release}

%description ant
Descriptor extractor for plugins written in Ant.

%package api
Group: Development/Java
Summary:        Maven Plugin Tools APIs
Obsoletes:      maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package beanshell
Group: Development/Java
Summary:        Maven Plugin Tool for Beanshell
Obsoletes:      maven-shared-plugin-tools-beanshell < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-beanshell = 0:%{version}-%{release}

%description beanshell
Descriptor extractor for plugins written in Beanshell.

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

# Note that this package contains code, not documentation.
# See comments about "javadocs" subpackage below.
%package javadoc
Group: Development/Java
Summary:        Maven Plugin Tools Javadoc
BuildArch: noarch

%description javadoc
The Maven Plugin Tools Javadoc provides several Javadoc taglets to be used when
generating Javadoc.

Java API documentation for %{name} is contained in
%{name}-javadocs package. This package does not contain it.

%package model
Group: Development/Java
Summary:        Maven Plugin Metadata Model
Obsoletes:      maven-shared-plugin-tools-model < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-model = 0:%{version}-%{release}

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

%package -n maven-script
Group: Development/Java
Summary:        Maven Script Mojo Support

%description -n maven-script
Maven Script Mojo Support lets developer write Maven plugins/goals
with scripting languages instead of compiled Java.

%package -n maven-script-ant
Group: Development/Java
Summary:        Maven Ant Mojo Support

%description -n maven-script-ant
This package provides %{summary}, which write Maven plugins with
Ant scripts.

%package -n maven-script-beanshell
Group: Development/Java
Summary:        Maven Beanshell Mojo Support

%description -n maven-script-beanshell
This package provides %{summary}, which write Maven plugins with
Beanshell scripts.

# This "javadocs" package violates packaging guidelines as of Sep 6 2012. The
# subpackage name "javadocs" instead of "javadoc" is intentional. There was a
# consensus that current naming scheme should be kept, even if it doesn't
# conform to the guidelines.  mizdebsk, September 2012
%package javadocs
Group: Development/Java
Summary:        Javadoc for %{name}

%description javadocs
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# For com.sun:tools use scope "compile" instead of "system"
%pom_remove_dep com.sun:tools maven-plugin-tools-javadoc
%pom_add_dep com.sun:tools maven-plugin-tools-javadoc

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope='test']"

# Use Maven 3.1.1 APIs
%pom_remove_dep :maven-project maven-plugin-plugin
%pom_remove_dep :maven-plugin-descriptor maven-plugin-plugin
%pom_remove_dep :maven-plugin-registry maven-plugin-plugin
%pom_remove_dep :maven-artifact-manager maven-plugin-plugin

%pom_change_dep :maven-project :maven-core maven-plugin-tools-annotations
%pom_change_dep :maven-plugin-descriptor :maven-compat maven-plugin-tools-annotations

%pom_remove_dep :maven-plugin-descriptor maven-script/maven-plugin-tools-ant
%pom_change_dep :maven-project :maven-core maven-script/maven-plugin-tools-ant

%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-api
%pom_change_dep :maven-project :maven-core maven-plugin-tools-api

%pom_remove_dep :maven-plugin-descriptor maven-script/maven-plugin-tools-beanshell

%pom_remove_dep :maven-project maven-plugin-tools-generators
%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-generators

%pom_change_dep :maven-project :maven-core maven-plugin-tools-java
%pom_remove_dep :maven-plugin-descriptor maven-plugin-tools-java

%pom_change_dep :maven-plugin-descriptor :maven-plugin-api maven-script/maven-plugin-tools-model

%pom_remove_dep :maven-project maven-script/maven-script-ant
%pom_remove_dep :maven-plugin-descriptor maven-script/maven-script-ant

%pom_remove_dep :maven-project
%pom_remove_dep :maven-plugin-descriptor
%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build -s -f

%install
%mvn_install


%files -f .mfiles-maven-plugin-tools
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files -n maven-plugin-plugin -f .mfiles-maven-plugin-plugin

%files annotations -f .mfiles-maven-plugin-tools-annotations

%files ant -f .mfiles-maven-plugin-tools-ant

%files api -f .mfiles-maven-plugin-tools-api

%files beanshell -f .mfiles-maven-plugin-tools-beanshell

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%files javadoc -f .mfiles-maven-plugin-tools-javadoc

%files model -f .mfiles-maven-plugin-tools-model

%files -n maven-script -f .mfiles-maven-script

%files -n maven-script-ant -f .mfiles-maven-script-ant

%files -n maven-script-beanshell -f .mfiles-maven-script-beanshell

%files javadocs -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
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

