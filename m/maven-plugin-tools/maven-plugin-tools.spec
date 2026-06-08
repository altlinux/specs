Name:           maven-plugin-tools
Version:        3.9.0
Release:        alt3
Epoch:          0
Summary:        Maven Plugin Tools
License:        Apache-2.0
Group:          Development/Java
URL:            http://maven.apache.org/plugin-tools/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:         0001-Remove-dependency-on-jtidy.patch
Patch2:         0002-Disable-reporting.patch
Patch4:         0003-sisu-index-for-aven-plugin-tools-java.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: jpackage-default
BuildRequires: unzip
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(com.thoughtworks.qdox:qdox)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-repository-metadata)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-velocity)

Obsoletes: maven-plugin-tools-javadoc < 0:3.6.0-1
Obsoletes: maven-plugin-tools-ant < %{epoch}:%{version}-%{release}
Obsoletes: maven-script-ant < %{epoch}:%{version}-%{release}
Obsoletes: maven-plugin-tools-beanshell < %{epoch}:%{version}-%{release}
Obsoletes: maven-script-beanshell < %{epoch}:%{version}-%{release}

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Summary: Maven Plugin Java 5 Annotations
Group: Development/Java

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n maven-plugin-plugin
Summary: Maven Plugin Plugin
Group: Development/Java

%description -n maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package annotations
Summary: Maven Plugin Tool for Annotations
Group: Development/Java

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%package api
Summary: Maven Plugin Tools APIs
Group: Development/Java
Obsoletes: maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package generators
Summary: Maven Plugin Tools Generators
Group: Development/Java

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Summary: Maven Plugin Tool for Java
Group: Development/Java
Obsoletes: maven-shared-plugin-tools-java < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-java = 0:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

%{?javadoc_package}

%prep
%setup -q
%autopatch -p1

find -name '*.java' -exec sed -i 's/\r//' {} +

rm -r maven-plugin-tools-api/src/test/resources/javadoc

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%pom_xpath_remove "pom:execution[pom:id='generated-helpmojo']" maven-plugin-plugin

%pom_disable_module maven-script
%pom_disable_module maven-plugin-report-plugin

%pom_remove_dep -r :maven-reporting-impl
%pom_remove_dep -r :maven-reporting-api
%pom_remove_dep -r :velocity
%pom_remove_dep -r :jtidy
%pom_remove_plugin -r :spotless-maven-plugin

%pom_remove_dep org.junit:junit-bom
%pom_remove_dep :maven-plugin-tools-ant maven-plugin-plugin
%pom_remove_dep :maven-plugin-tools-beanshell maven-plugin-plugin

rm maven-plugin-tools-generators/src/main/java/org/apache/maven/tools/plugin/generator/PluginXdocGenerator.java

%build
%mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-maven-plugin-tools
%dir %{_javadir}/%{name}
%doc --no-dereference LICENSE NOTICE

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files -n maven-plugin-plugin -f .mfiles-maven-plugin-plugin

%files annotations -f .mfiles-maven-plugin-tools-annotations
%doc --no-dereference LICENSE NOTICE

%files api -f .mfiles-maven-plugin-tools-api
%doc --no-dereference LICENSE NOTICE

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%changelog
* Mon Jun 08 2026 Arseniy Kostevich <faux@altlinux.org> 0:3.9.0-alt3
- Canceled disabling of help MOJO generation.

* Tue Mar 24 2026 Ivan A. Melnikov <iv@altlinux.org> 0:3.9.0-alt2
- NMU: Fix building of legacy plugins that rely on MOJO metadata
  extraction from javadoc.

* Sat Jul 26 2025 Andrey Cherepanov <cas@altlinux.org> 0:3.9.0-alt1
- New version.

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

