Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          glassfish-jaxws
Version:       2.2.10
Release:       alt1_4jpp8
Summary:       JAX-WS Reference Implementation (RI) Project
# ASL 2.0
# tools/wscompile/src/com/sun/tools/ws/ant/AnnotationProcessingTask.java
# tools/wscompile/src/com/sun/tools/ws/wsdl/parser/NamespaceContextImpl.java
# Public Domain rt/src/com/sun/xml/ws/util/NamespaceSupport.java
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0 and Public Domain
Url:           http://jax-ws.java.net/
# git clone git://java.net/jax-ws~git
# (cd jax-ws~git/ && git archive --format=tar --prefix=glassfish-jaxws-2.2.10/ JAXWS_2_2_10_FCS | xz > ../glassfish-jaxws-2.2.10.tar.xz)
Source0:       %{name}-%{version}.tar.xz
# build fix for glassfish-gmbal 3.2.0-b003
Patch0:        glassfish-jaxws-2.2.10-gmbal.patch
# use system xml-resolver
Patch1:        glassfish-jaxws-2.2.10-resolver.patch
# use system asm
Patch2:        glassfish-jaxws-2.2.10-asm.patch
# remove unavailable com.sun.tools.xjc.api.util.ToolsJarNotFoundException
Patch3:        glassfish-jaxws-2.2.10-jaxb-xjc.patch

Patch4:        glassfish-jaxws-2.2.10-deps.patch

Patch5:        glassfish-jaxws-2.2.10-javadoclinksdir.patch

BuildRequires: maven-local
BuildRequires: mvn(com.sun.istack:import-properties-plugin)
BuildRequires: mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires: mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires: mvn(com.sun.xml.messaging.saaj:saaj-impl)
BuildRequires: mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires: mvn(com.sun.xml.ws:policy)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.glassfish.gmbal:gmbal-api-only)
BuildRequires: mvn(org.glassfish.ha:ha-api)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-bom:pom:)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-core)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-jxc)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.glassfish.pfl:pfl-tf)
BuildRequires: mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.xml.soap:jboss-saaj-api_1.3_spec)
BuildRequires: mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
BuildRequires: mvn(org.jvnet.mimepull:mimepull)
BuildRequires: mvn(org.jvnet.staxex:stax-ex)
BuildRequires: mvn(xml-resolver:xml-resolver)
BuildRequires: objectweb-asm3

BuildRequires: glassfish-jaxb-api-javadoc
BuildRequires: java-javadoc
BuildRequires: jboss-jaxws-2.2-api-javadoc

BuildArch:     noarch
Source44: import.info

%description
This project provides the core of Metro project,
inside GlassFish community. This project develops and
evolves the code base for the reference implementation of
the Java API for XML Web Services (JAX-WS) specification.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
Obsoletes:     %{name}-tools-javadoc
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package tools
Group: Development/Java
Summary:       JAX-WS Reference Implementation Tools

%description tools
Open source Reference Implementation of
JSR-224: Java API for XML Web Services.

%package transports
Group: Development/Java
Summary:       JAX-WS RI Transports Implementation

%description transports
This package provides Implementation of:
- Async-Client-Transport.
- Local-Transport (used mainly in tests)
for JAX-WS RI.

%prep
%setup -q -n %{name}-%{version}
mv jaxws-ri/* .
rm -rf jaxws-ri
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

# clean up
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete
find . -name "*.zip" -print -delete

%pom_disable_module docs
%pom_disable_module tests
%pom_disable_module jaxws-ri-src bundles


%pom_disable_module ../eclipselink_jaxb extras
%pom_disable_module ../eclipselink_sdo extras
%pom_remove_dep :jaxws-eclipselink-plugin bundles/jaxws-ri
%pom_remove_dep :sdo-eclipselink-plugin bundles/jaxws-ri
%pom_remove_dep :jaxws-eclipselink-plugin boms/bom
%pom_remove_dep :sdo-eclipselink-plugin boms/bom

%pom_remove_plugin com.sun.wts.tools.ant:package-rename-task
%pom_remove_plugin org.glassfish.build:gfnexus-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin com.sun.wts.tools.ant:package-rename-task rt
%pom_remove_plugin :maven-dependency-plugin rt
%pom_remove_plugin :maven-dependency-plugin bundles/jaxws-rt
%pom_remove_plugin :maven-antrun-plugin bundles/jaxws-rt
%pom_remove_plugin :maven-assembly-plugin bundles/jaxws-rt
%pom_remove_plugin :maven-dependency-plugin bundles/jaxws-ri
%pom_remove_plugin :maven-antrun-plugin bundles/jaxws-ri
%pom_remove_plugin :maven-assembly-plugin bundles/jaxws-ri
%pom_remove_plugin :maven-dependency-plugin bundles/jaxws-tools
%pom_remove_plugin :maven-antrun-plugin bundles/jaxws-tools
%pom_remove_plugin :maven-assembly-plugin bundles/jaxws-tools

%pom_remove_plugin org.glassfish.metro:harness-maven-plugin tests
%pom_remove_plugin org.glassfish.metro:harness-maven-plugin tests/unit

%pom_xpath_remove "pom:dependencies/pom:dependency[pom:classifier='sources']" boms/bom
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:classifier='sources']" boms/bom-ext
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:type='zip']" boms/bom
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:type='zip']" bundles/jaxws-ri

%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='rt']" '<version>${project.version}</version>' tools/wscompile

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-dependency-plugin']/pom:executions/pom:execution/pom:configuration/pom:artifactItems/pom:artifactItem[pom:artifactId='jsr181-api']" tools/wscompile
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:systemPropertyVariables/pom:jsr181-api.version" tools/wscompile

%pom_xpath_remove "pom:profiles/pom:profile/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package" transports/local
%pom_xpath_inject "pom:profiles/pom:profile/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" '
<Import-Package>
  com.oracle.webservices.api.message;version=${jaxws.osgiVersion},
  com.sun.xml.ws.api;version=${jaxws.osgiVersion},
  com.sun.xml.ws.api.message;version=${jaxws.osgiVersion},
  com.sun.xml.ws.api.pipe;version=${jaxws.osgiVersion},
  com.sun.xml.ws.api.pipe.helper;version=${jaxws.osgiVersion},
  com.sun.xml.ws.api.server;version=${jaxws.osgiVersion},
  com.sun.xml.ws.client;version=${jaxws.osgiVersion},
  com.sun.xml.ws.transport.http;version=${jaxws.osgiVersion},
  com.sun.xml.ws.util;version=${jaxws.osgiVersion},
  org.jvnet.ws.message,
  javax.xml.namespace,
  javax.xml.ws;version=${jaxws-api.osgiVersion},
  javax.xml.ws.handler;version=${jaxws-api.osgiVersion}
</Import-Package>' transports/local

%pom_xpath_remove pom:build/pom:finalName transports/local
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:3.0.1 transports/local '
 <executions>
  <execution>
   <id>default-jar</id>
   <phase>skip</phase>
  </execution>
 </executions>
<configuration>
  <finalName>${project.artifactId}</finalName>
  <archive>
    <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>'

%pom_xpath_inject "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "
<excludePackageNames>*.message.*</excludePackageNames>
<excludePackageNames>com.sun.xml.ws</excludePackageNames>"

%pom_remove_dep javax.jws:jsr181-api
%pom_remove_dep javax.jws:jsr181-api boms/bom
%pom_remove_dep javax.jws:jsr181-api bundles/jaxws-rt
%pom_remove_dep :ant-nodeps tools/wscompile

%pom_xpath_set "pom:phase[text()='prepare-package']" package transports/async-client-transport

for d in CDDL+GPLv2.html CDDL-1.0-license.txt README.md ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

# these tests fails
rm -r tools/wscompile/src/test/java/com/sun/tools/ws/ant/* \
 eclipselink_jaxb/src/test/java/com/sun/xml/ws/cts/dl_swa/SwaMimeAttachmentTest.java
find -name SAAJMessageTest.java -delete
find -name SAAJMessageWrapperTest.java -delete



%mvn_package ":jaxws-*-transport" transports
%mvn_package :extras transports
%mvn_package :wscompile tools
%mvn_alias :rt :jaxws-ri:jar: :jaxws-rt:jar:
%mvn_alias :wscompile :jaxws-tools:jar:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc CDDL+GPLv2.html CDDL-1.0-license.txt

%files tools  -f .mfiles-tools
%doc CDDL+GPLv2.html CDDL-1.0-license.txt

%files transports  -f .mfiles-transports
%doc CDDL+GPLv2.html CDDL-1.0-license.txt

%files javadoc -f .mfiles-javadoc
%doc CDDL+GPLv2.html CDDL-1.0-license.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.10-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.10-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.10-alt1_2jpp8
- java 8 mass update

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.7-alt1_2jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_8jpp6
- build with new boss

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_8jpp6
- build with glassfish-jaxb21

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_8jpp6
- fixed components-info
- hack: added saaj-api/impl.jar though jaxws is built w/o them,
  for jbossas compatibility

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_8jpp6
- new version

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_4jpp5
- fixed components-info

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_4jpp5
- fixed repocop warnings

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5.1
- NMU (by repocop): the following fixes applied:
 * windows-thumbnail-database-in-package for glassfish-jaxws-javadoc

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

