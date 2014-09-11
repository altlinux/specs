Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-tools
Version:        3.1
Release:        alt4_14jpp7
Epoch:          0
Summary:        Maven Plugin Tools

License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

# Fix NullPointerException in MojoClassVisitor.visit()
# See: rhbz#920042, http://jira.codehaus.org/browse/MPLUGIN-242
Patch0:         %{name}-rhbz-920042.patch

BuildRequires:  maven-local
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(asm:asm-commons)
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(net.sf.jtidy:jtidy)
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-descriptor)
BuildRequires:  mvn(org.apache.maven:maven-plugin-registry)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.plexus:plexus-ant-factory)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-bsh-factory)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
Source44: import.info


%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Group: Development/Java
Summary:        Maven Plugin Java 5 Annotations
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-plugin-annotations < 0:%{version}-%{release}

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n maven-plugin-plugin
Group: Development/Java
Summary:        Maven Plugin Plugin
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven2-plugin-plugin < 0:%{version}-%{release}
Provides:       maven2-plugin-plugin = 0:%{version}-%{release}

%description -n maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package annotations
Group: Development/Java
Summary:        Maven Plugin Tool for Annotations
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%package ant
Group: Development/Java
Summary:        Maven Plugin Tool for Ant
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-shared-plugin-tools-ant < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-ant = 0:%{version}-%{release}

%description ant
Descriptor extractor for plugins written in Ant.

%package api
Group: Development/Java
Summary:        Maven Plugin Tools APIs
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package beanshell
Group: Development/Java
Summary:        Maven Plugin Tool for Beanshell
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-shared-plugin-tools-beanshell < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-beanshell = 0:%{version}-%{release}

%description beanshell
Descriptor extractor for plugins written in Beanshell.

%package generators
Group: Development/Java
Summary:        Maven Plugin Tools Generators
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Group: Development/Java
Summary:        Maven Plugin Tool for Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-shared-plugin-tools-java < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-java = 0:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

# Note that this package contains code, not documentation.
# See comments about "javadocs" subpackage below.
%package javadoc
Group: Development/Java
Summary:        Maven Plugin Tools Javadoc
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
The Maven Plugin Tools Javadoc provides several Javadoc taglets to be used when
generating Javadoc.

Java API documentation for %{name} is contained in
%{name}-javadocs package. This package does not contain it.

%package model
Group: Development/Java
Summary:        Maven Plugin Metadata Model
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      maven-shared-plugin-tools-model < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-model = 0:%{version}-%{release}

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

%package -n maven-script
Group: Development/Java
Summary:        Maven Script Mojo Support
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n maven-script
Maven Script Mojo Support lets developer write Maven plugins/goals
with scripting languages instead of compiled Java.

%package -n maven-script-ant
Group: Development/Java
Summary:        Maven Ant Mojo Support
Requires:       maven-script = %{epoch}:%{version}-%{release}

%description -n maven-script-ant
This package provides %{summary}, which write Maven plugins with
Ant scripts.

%package -n maven-script-beanshell
Group: Development/Java
Summary:        Maven Beanshell Mojo Support
Requires:       maven-script = %{epoch}:%{version}-%{release}

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

# For easier installation
ln -s maven-script/maven-script-{ant,beanshell} .

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Disable resolution of test artifacts (tests are skipped anyways).
%mvn_config buildSettings/skipTests true

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

