Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0
%global oversion %{version}M10

Name:           woden
Version:        1.0
Release:        alt2_0.20.M10jpp8
Summary:        Web Service Description Language (WSDL) validating parser
License:        ASL 2.0
URL:            http://ws.apache.org/woden/
Source0:        http://archive.apache.org/dist/ws/woden/%{oversion}/woden-%{oversion}-src.zip
BuildArch:      noarch
  
BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.15)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.ws.xmlschema:xmlschema-core)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(wsdl4j:wsdl4j)

# For xsltproc command
BuildRequires:  libxslt xsltproc
Source44: import.info

Provides: ws-commons-%name = %version-%release
Conflicts:  ws-commons-%name <= 1.0-alt3_0.5.M9jpp7
Obsoletes:  ws-commons-%name <= 1.0-alt3_0.5.M9jpp7


%description
The Woden project is a sub-project of the Apache Web Services Project
to develop a Java class library for reading, manipulating, creating
and writing WSDL documents, initially to support WSDL 2.0 but with the
longer term aim of supporting past, present and future versions of WSDL.

%package parent
Group: Development/Java
Summary: Parent pom of %{name} project

%description parent
Parent pom of %{name} project.

%package tool
Group: Development/Java
Summary: Command line tool for converting WSDL documents
# Explicit requires for javapackages-tools since woden-tool script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description tool
Command line tool for converting WSDL documents.

%package ant
Group: Development/Java
Summary: Ant plug-in for converting WSDL documents

%description ant
Ant plug-in for converting WSDL documents.

%package maven-plugin
Group: Development/Java
Summary: Maven plug-in for converting WSDL documents

%description maven-plugin
Maven plug-in for converting WSDL documents.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n woden-%{oversion}

# Using ws-parent doesn't add anything, may as well use apache-parent
%pom_set_parent "org.apache:apache:17"

# org.codehaus.mojo:xslt-maven-plugin is not available so use command line tool instead
%pom_remove_plugin org.codehaus.mojo:xslt-maven-plugin woden-tool
%pom_add_plugin "org.codehaus.mojo:exec-maven-plugin:1.6.0" woden-tool "
  <executions>
    <execution>
      <goals><goal>exec</goal></goals>
      <phase>compile</phase>
    </execution>
  </executions>
  <configuration>
    <executable>xsltproc</executable>
    <arguments>
      <argument>-o</argument>
      <argument>\${project.build.outputDirectory}/wsdl-viewer-modules.xsl</argument>
      <argument>all-in-one.xsl</argument>
      <argument>src/main/xslt/wsdl-viewer-modules.xsl</argument>
    </arguments>
  </configuration>"

# Avoid use of deprecated plexus-maven-plugin
%pom_remove_plugin ":plexus-maven-plugin" woden-converter-maven-plugin

# These module contain only testdata and according to upstream, should not be deployed
%pom_disable_module woden-tests
%pom_disable_module w3c-tests

# Disable unnecessary plugin for RPM builds, Fedora doesn't ship source jars
%pom_remove_plugin :maven-source-plugin

# Don't need to build the dist assembly for RPM builds
%pom_disable_module woden-dist

# Compatibility aliases
%mvn_alias :woden-core :woden-api :woden-impl-commons :woden-impl-dom

%build
%mvn_build -s

# Fix encoding
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.utf8
mv LICENSE.utf8 LICENSE

%install
%mvn_install

%jpackage_script "org.apache.woden.tool.converter.Convert" "" "" "woden:XmlSchema:wsdl4j:commons-logging" "woden-tool" true

%files -f .mfiles-woden-core
%doc README RELEASE-NOTE
%doc --no-dereference LICENSE NOTICE

%files parent -f .mfiles-woden
%doc --no-dereference LICENSE NOTICE

%files tool -f .mfiles-woden-tool
%{_bindir}/woden-tool

%files ant -f .mfiles-woden-ant

%files maven-plugin -f .mfiles-woden-converter-maven-plugin

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.20.M10jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.17.M10jpp8
- java fc28+ update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.14.M9jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.14.M9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.13.M9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.12.M9jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.M9jpp8
- java 8 mass update

