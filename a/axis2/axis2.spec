Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          axis2
Version:       1.7.7
Release:       alt1_1jpp8
Summary:       Java-based Web Services / SOAP / WSDL engine
License:       ASL 2.0
URL:           http://axis.apache.org/axis2/java/core/
Source0:       http://archive.apache.org/dist/axis/axis2/java/core/%{version}/axis2-%{version}-src.zip

Patch0: axiom-ContentType.patch
Patch1: axiom-detach-api.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-fileupload:commons-fileupload)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-xjc)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(com.sun.xml.ws:jaxws-tools)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(javax.ws.rs:jsr311-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(log4j:log4j:1.2.15)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-saaj_1.3_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.archetype:archetype-packaging)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-descriptor)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-archetype-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.neethi:neethi)
BuildRequires:  mvn(org.apache.woden:woden-core)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-api)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-dom)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-impl)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-jaxb)
#BuildRequires:  mvn(org.apache.ws.xmlschema:xmlschema-core)
# I: two provides: ws-xmlschema and XmlSchema
BuildRequires: ws-xmlschema
BuildRequires:  mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(wsdl4j:wsdl4j)
Source44: import.info

%description
Apache Axis2 is a Web Services / SOAP / WSDL engine, the successor
to the widely used Apache Axis SOAP stack. There are two
implementations of the Apache Axis2 Web services engine - Apache 
Axis2/Java and Apache Axis2/C.  This is Axis2/Java.

%package maven
Group: Development/Java
Summary: Axis2 quickstart archetypes and maven plugins

%description maven
Maven plugins and archetypes for creating Axis2 web services.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -R -p1
%patch1 -R -p1

# Disable plugins unnecessary for RPM builds
# 1) We don't need animal-sniffer or enforcer because we can guarantee java >= 8
# 2) Fedora doesn't ship source jars
%pom_remove_plugin ":animal-sniffer-maven-plugin"
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin ":maven-source-plugin"

# These are used for some test resource generation, but we currently don't run tests
%pom_remove_plugin ":maven-dependency-plugin" modules/transport/mail
%pom_remove_plugin ":maven-antrun-plugin" modules/transport/tcp

# Let xmvn aggregate javadocs
%pom_disable_module apidocs

# No need to build the distributable zip or sample projects in RPM build
%pom_disable_module modules/distribution
%pom_disable_module modules/samples/version
%pom_disable_module modules/samples

# Missing dep "alta-maven-plugin" is used to get the path of a list of dependencies for the surefire bootclasspath
%pom_remove_plugin -r ":alta-maven-plugin"

# Missing jalopy dependency
%pom_remove_dep -r "jalopy:jalopy"

# Disable modules whose dependencies are not in Fedora.
%pom_disable_module modules/adb-tests
%pom_disable_module modules/addressing
%pom_disable_module modules/integration
%pom_disable_module modules/jibx
%pom_disable_module modules/mex
%pom_disable_module modules/mtompolicy-mar
%pom_disable_module modules/ping
%pom_disable_module modules/soapmonitor/servlet
%pom_disable_module modules/soapmonitor/module
%pom_disable_module modules/spring
%pom_disable_module modules/testutils
%pom_disable_module modules/tool/axis2-aar-maven-plugin
%pom_disable_module modules/tool/axis2-ant-plugin
%pom_disable_module modules/tool/axis2-eclipse-codegen-plugin
%pom_disable_module modules/tool/axis2-eclipse-service-plugin
%pom_disable_module modules/tool/axis2-idea-plugin
%pom_disable_module modules/tool/axis2-mar-maven-plugin
%pom_disable_module modules/webapp
%pom_disable_module modules/scripting
%pom_disable_module modules/metadata
%pom_disable_module modules/jaxws
%pom_disable_module modules/jaxws-mar
%pom_disable_module modules/jaxws-integration
%pom_disable_module modules/clustering
%pom_disable_module modules/corba
%pom_disable_module modules/osgi
%pom_disable_module modules/osgi-tests
%pom_disable_module modules/transport/jms
%pom_disable_module modules/transport/testkit
%pom_disable_module modules/transport/xmpp
%pom_disable_module systests

# 1) Remove JSR deps which are now built into openjdk
# 2) Fix javamail dep
%pom_remove_dep -r ":geronimo-activation_1.1_spec"
%pom_remove_dep -r ":geronimo-ws-metadata_2.0_spec"
%pom_change_dep -r ":geronimo-javamail_1.4_spec" "javax.mail:mail"

# Use modern servlet api
%pom_xpath_set "pom:properties/pom:servlet.api.version" 3.1.0

sed -i -e 's/\r//g' NOTICE.txt

# Put maven stuff in a sub-package
%mvn_package "org.apache.axis2.archetype:" maven
%mvn_package ":*-maven-plugin" maven

%build
# Tests currently use an auto-generated ant build xml file which
# fails due to incorrect setting of JAVA_HOME (to JRE instead of JDK home)
# I have not yet determined the fix for this.
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTE.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files maven -f .mfiles-maven

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.7-alt1_1jpp8
- new version
- note: built with ws-xmlschema, not XmlSchema
- TODO: build with XmlSchema and remove ws-xmlschema from Sisyphus

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_21jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_20jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_17jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_16jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_15jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_7jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_4jpp7
- new version

