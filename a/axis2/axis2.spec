Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          axis2
Version:       1.6.1
Release:       alt2_17jpp8
Summary:       Java-based Web Services / SOAP / WSDL engine
License:       ASL 2.0
URL:           http://axis.apache.org/axis2/java/core/
Source0:       http://mirror.metrocast.net/apache//axis/axis2/java/core/1.6.1/axis2-1.6.1-src.zip
# wrap generated headers with ifndef/define/endif
Patch0:        %{name}-AXIS2-5349.patch

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-clean-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: geronimo-jta
BuildRequires: geronimo-saaj
BuildRequires: geronimo-parent-poms
BuildRequires: XmlSchema
BuildRequires: apache-commons-logging
BuildRequires: axiom
BuildRequires: neethi
BuildRequires: jsr-311
BuildRequires: woden
BuildRequires: javamail
BuildRequires: dos2unix
BuildRequires: maven-remote-resources-plugin
BuildRequires: apache-commons-fileupload
BuildRequires: glassfish-servlet-api
BuildRequires: geronimo-saaj
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-antrun-plugin

Requires:      log4j12
Requires:      xerces-j2
Requires:      javamail
Requires:      glassfish-servlet-api
Source44: import.info

%description
Apache Axis2 is a Web Services / SOAP / WSDL engine, the successor
to the widely used Apache Axis SOAP stack. There are two
implementations of the Apache Axis2 Web services engine - Apache 
Axis2/Java and Apache Axis2/C.  This is Axis2/Java.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

# Disable modules whose dependencies are not in Fedora.
%pom_disable_module modules/addressing
%pom_disable_module modules/fastinfoset
%pom_disable_module modules/integration
%pom_disable_module modules/jibx
%pom_disable_module modules/json
%pom_disable_module modules/mex
%pom_disable_module modules/mtompolicy
%pom_disable_module modules/mtompolicy-mar
%pom_disable_module modules/ping
%pom_disable_module modules/samples/version
%pom_disable_module modules/soapmonitor/servlet
%pom_disable_module modules/soapmonitor/module
%pom_disable_module modules/spring
%pom_disable_module modules/testutils
%pom_disable_module modules/tool/axis2-aar-maven-plugin
%pom_disable_module modules/tool/axis2-ant-plugin
%pom_disable_module modules/tool/axis2-eclipse-codegen-plugin
%pom_disable_module modules/tool/axis2-eclipse-service-plugin
%pom_disable_module modules/tool/axis2-idea-plugin
%pom_disable_module modules/tool/axis2-java2wsdl-maven-plugin
%pom_disable_module modules/tool/axis2-mar-maven-plugin
%pom_disable_module modules/tool/axis2-repo-maven-plugin
%pom_disable_module modules/tool/axis2-wsdl2code-maven-plugin
%pom_disable_module modules/webapp
%pom_disable_module modules/xmlbeans
%pom_disable_module modules/scripting
%pom_disable_module modules/jaxbri
%pom_disable_module modules/metadata
%pom_disable_module modules/jaxws
%pom_disable_module modules/jaxws-mar
%pom_disable_module modules/jaxws-integration
%pom_disable_module modules/clustering
%pom_disable_module modules/corba
%pom_disable_module modules/osgi
#%% pom_disable_module modules/transport/local
#%% pom_disable_module modules/transport/http
#%% pom_disable_module modules/java2wsdl

# Remove non standard apidocs final subdir
%pom_xpath_remove "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:configuration/pom:destDir"

# 1) Remove JSR deps which are now built into openjdk
# 2) Fix javamail dep
# 3) Remove gmaven code
%pom_remove_dep :geronimo-activation_1.1_spec modules/adb
%pom_remove_dep :geronimo-javamail_1.4_spec modules/java2wsdl
%pom_add_dep javax.mail:mail modules/java2wsdl
%pom_remove_plugin :gmaven-plugin modules/java2wsdl
%pom_remove_dep :geronimo-ws-metadata_2.0_spec modules/kernel

%patch0 -p0

%pom_xpath_set "pom:properties/pom:servlet.api.version" 3.1.0 modules/parent
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.servlet']/pom:artifactId" javax.servlet-api modules/parent modules/kernel
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId = 'javax.servlet']" "<version>1.6.2</version>" modules/kernel

# reference to Parameter is ambiguous both class java.lang.reflect.Parameter in
# java.lang.reflect and class org.apache.axis2.description.Parameter in org.apache.axis2.description match
sed -i "s|Parameter sortAtt|org.apache.axis2.description.Parameter sortAtt|" \
 modules/kernel/src/org/apache/axis2/description/java2wsdl/DefaultSchemaGenerator.java
sed -i "s|Parameter generateWrappedArrayTypes|org.apache.axis2.description.Parameter generateWrappedArrayTypes|" \
 modules/kernel/src/org/apache/axis2/description/java2wsdl/DefaultSchemaGenerator.java
sed -i "s|Parameter extraClassesParam|org.apache.axis2.description.Parameter extraClassesParam|" \
 modules/kernel/src/org/apache/axis2/description/java2wsdl/DefaultSchemaGenerator.java

%build
# Tests currently use an auto-generated ant build xml file which
# fails due to incorrect setting of JAVA_HOME (to JRE instead of JDK home)
# I have not yet determined the fix for this.
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8
dos2unix NOTICE.txt

%install
%mvn_install

%files -f .mfiles
%doc README.txt release-notes.html
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

