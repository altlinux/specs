BuildRequires: apache-parent
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jasperreports
Version:       6.2.2
Release:       alt2_3jpp8
Summary:       Report-generating tool
License:       LGPLv3+
URL:           http://jasperforge.org/projects/jasperreports/
# wget http://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%%206.2.2/jasperreports-6.2.2-project.tar.gz
# tar xf jasperreports-6.2.2-project.tar.gz
# find jasperreports-6.2.2 -name '*.class' -print -delete
# find jasperreports-6.2.2 -name '*.jar' -print -delete
# find jasperreports-6.2.2 -name 'PieChartReport.bak' -print -delete
# rm -rf jasperreports-6.2.2/lib/* jasperreports-6.2.2/dist/docs/api
# tar czf jasperreports-6.2.2-clean.tar.gz jasperreports-6.2.2
Source0:       %{name}-%{version}-clean.tar.gz

# Exclude Mondrian modules
Patch0:        %{name}-%{version}-remove-mondrian-support.patch
# Exclude OLAP4j modules
Patch1:        %{name}-%{version}-remove-olap4j-support.patch
# Exclude Barcode4J and Barbecue modules
Patch2:        %{name}-%{version}-remove-barbecue-barcode4j-support.patch
# Use commons-codec instead of non-free W3C Base64 implementation
Patch3:        %{name}-%{version}-use-commons-codec.patch

Patch4:        %{name}-%{version}-port-to-lucene-5.5.0.patch

# Tanks to Michael Simacek <msimacek@redhat.com>
Patch5:        %{name}-%{version}-port-to-poi-3.14.patch

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(bsh:bsh)
BuildRequires: mvn(com.adobe.xmp:xmpcore)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.zxing:core)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(com.lowagie:itext)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(javax.persistence:persistence-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.xml.soap:saaj-api)
BuildRequires: mvn(jaxen:jaxen)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sourceforge.jexcelapi:jxl)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.commons:commons-javaflow)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires: mvn(org.apache.lucene:lucene-core)
BuildRequires: mvn(org.apache.lucene:lucene-queryparser)
BuildRequires: mvn(org.apache.poi:poi)
BuildRequires: mvn(org.apache.poi:poi-ooxml)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.apache.xmlgraphics:batik-bridge)
BuildRequires: mvn(org.apache.xmlgraphics:batik-svggen)
BuildRequires: mvn(org.codehaus.castor:castor-xml)
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj)
BuildRequires: mvn(org.hibernate:hibernate-core:3)
BuildRequires: mvn(org.jfree:jcommon)
BuildRequires: mvn(org.jfree:jfreechart)
BuildRequires: mvn(org.mozilla:rhino)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(xalan:xalan)

BuildArch:     noarch
Source44: import.info

%description
JasperReports is a powerful open source
report-generating tool that has the ability
to deliver rich content onto the screen, to
the printer or into PDF, HTML, XLS, CSV and
XML files. It is entirely written in Java
and can be used in a variety of Java enabled
applications, including J2EE or Web
Its main purpose is to help creating page
oriented, ready to print documents in a
simple and flexible manner.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package manual
Group: Development/Java
Summary:       Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1
%pom_remove_dep :mondrian
rm -r src/net/sf/jasperreports/olap/mondrian \
 src/net/sf/jasperreports/data/mondrian

%patch1 -p1
%pom_remove_dep :olap4j
rm -r src/net/sf/jasperreports/olap

%patch2 -p1
%pom_remove_dep :barbecue
rm -r src/net/sf/jasperreports/components/barbecue
%pom_remove_dep :barcode4j
rm -r src/net/sf/jasperreports/components/barcode4j

%patch3 -p1
rm -r src/org
%pom_add_dep commons-codec:commons-codec:1.10:compile

%patch4 -p1
%patch5 -p1


%pom_remove_plugin :clirr-maven-plugin

%pom_change_dep :hibernate-core ::3
%pom_change_dep javax.servlet:servlet-api javax.servlet:javax.servlet-api:3.1.0
%pom_change_dep :bsh bsh::1.3.0
%pom_change_dep :log4j ::1.2.17

%pom_change_dep :commons-javaflow org.apache.commons:


# Disable circular dependecy cycle
%pom_remove_dep org.springframework:
 
# Test dep (NOT available)
%pom_remove_dep :jasperreports-fonts

# Remove packaged manifest files
rm -r src/META-INF
%pom_remove_plugin :maven-jar-plugin
# Add OSGi support
%pom_xpath_set "pom:project/pom:packaging" bundle
%pom_add_plugin org.apache.felix:maven-bundle-plugin:3.0.1 . "
<extensions>true</extensions>
<configuration>
   <excludeDependencies>true</excludeDependencies>
   <instructions>
     <Bundle-Name>JasperReports Library</Bundle-Name>
     <Bundle-SymbolicName>net.sf.jasperreports.engine</Bundle-SymbolicName>
     <Bundle-Vendor>TIBCO Software Inc.</Bundle-Vendor>
     <Bundle-Version>\${project.version}</Bundle-Version>
     <DynamicImport-Package>*</DynamicImport-Package>
     <Implementation-Title>net.sf.jasperreports.engine</Implementation-Title>
     <Implementation-Vendor>TIBCO Software Inc.</Implementation-Vendor>
     <Implementation-Version>\${project.version}</Implementation-Version>
     <Specification-Title>JasperReports Library</Specification-Title>
     <Specification-Vendor>TIBCO Software Inc.</Specification-Vendor>
     <Specification-Version>\${project.version}</Specification-Version>
   </instructions>
</configuration>
<executions>
   <execution>
     <id>bundle-manifest</id>
     <phase>process-classes</phase>
     <goals>
       <goal>manifest</goal>
     </goals>
   </execution>
</executions>"

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>"

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' changes.txt
touch -r changes.txt.orig changes.txt
rm changes.txt.orig

%mvn_alias :%{name} %{name}:%{name}

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc changes.txt readme.txt
%doc license.txt ThirdPartySoftwareNotices.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt ThirdPartySoftwareNotices.txt

%files manual
%doc dist/docs/*
%doc license.txt ThirdPartySoftwareNotices.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.2.2-alt2_3jpp8
- added BR: apache-parent for javapackages 5

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.2.2-alt1_3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_15jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_14jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt1_3jpp7
- new version

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

