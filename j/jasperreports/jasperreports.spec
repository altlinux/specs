Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jasperreports
# the JR newest release requires
# xmlbeans >= 2.5.0
# castor-xml modules see also https://bugzilla.redhat.com/show_bug.cgi?id=820676
Version:       4.0.2
Release:       alt2_3jpp7
Summary:       Report-generating tool
Group:         Development/Java
License:       LGPLv3+
URL:           http://jasperforge.org/projects/jasperreports/
# wget http://sourceforge.net/projects/jasperreports/files/jasperreports/JasperReports%204.0.2/jasperreports-4.0.2-project.tar.gz
# tar xf jasperreports-4.0.2-project.tar.gz
# find jasperreports-4.0.2 -name '*.class' -delete
# find jasperreports-4.0.2 -name '*.jar' -delete
# rm -rf lib/*
# tar czf jasperreports-4.0.2-clean.tar.gz jasperreports-4.0.2
Source0:       %{name}-%{version}-clean.tar.gz
# remove groovy-all.jar references
Patch0:        %{name}-%{version}-use_system_asm.patch
# configure javaflow ant task
# build fix for commons-javaflow 1.0
Patch1:        %{name}-%{version}-configure_javaflow.patch
# exclude Barcode4J and Barbecue modules
Patch2:        %{name}-%{version}-exclude_barcode4j_and_barbecue.patch
# remove Xmx128m to javadoc task
Patch3:        %{name}-%{version}-no_maxmemory_for_javadoc.patch
# use commons-codec instead of unavailable (non free) W3C Base64 decode/encode
Patch4:        %{name}-%{version}-use_commons-codec.patch
# don't build -font.jar
Patch5:        %{name}-%{version}-disable_fonts.patch
# disable build of sampleref
Patch6:        %{name}-%{version}-disable_sampleref.patch
# add
#     asm
#     commons-codec
# change
#     artifactId groovy-all in groovy
#     eclipse jdtcore in org.eclipse.jdt core
#     commons-javaflow version 20060411 >> 1.0
#     org.beanshell bsh 2.0b4 in  bsh bsh 1.3.0
# remove unavailable build deps
#     com.keypoint png-encoder 1.5
#     mondrian mondrian 3.1.1.12687
#     net.sf.barcode4j barcode4j 2.0
#     net.sourceforge.barbecue barbecue 1.5-beta1
Patch7:       %{name}-%{version}-pom.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: antlr
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-javaflow
BuildRequires: apache-commons-logging
BuildRequires: apache-poi
BuildRequires: batik
BuildRequires: bcel
BuildRequires: bsh
BuildRequires: dom4j
BuildRequires: ecj >= 1:3.4.2-13
BuildRequires: geronimo-saaj
BuildRequires: groovy
BuildRequires: hibernate3
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hsqldb
BuildRequires: iText
BuildRequires: jaxen
BuildRequires: jcommon
BuildRequires: jexcelapi
BuildRequires: jfreechart
BuildRequires: log4j
BuildRequires: objectweb-asm
BuildRequires: rhino
BuildRequires: springframework
BuildRequires: springframework-beans
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires:      apache-commons-beanutils
Requires:      apache-commons-codec
Requires:      apache-commons-collections
Requires:      apache-commons-digester
Requires:      apache-commons-javaflow
Requires:      apache-commons-logging
Requires:      batik
Requires:      bcel
Requires:      ecj >= 1:3.4.2-13
Requires:      geronimo-saaj
Requires:      hsqldb
Requires:      iText
Requires:      jcommon
Requires:      jfreechart
Requires:      springframework
Requires:      springframework-beans
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
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
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package manual
Group:         Development/Java
Summary:       Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q
find . -name 'PieChartReport.bak' -delete
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0

sed -i 's/\r//' changes.txt

ln -sf $(build-classpath ant) lib/ant-1.7.1.jar
ln -sf $(build-classpath antlr) lib/antlr-2.7.5.jar
ln -sf $(build-classpath batik-all) lib/
ln -sf $(build-classpath bcel) lib/bcel-5.2.jar
ln -sf $(build-classpath bsh) lib/bsh-2.0b4.jar
ln -sf $(build-classpath commons-beanutils) lib/commons-beanutils-1.8.0.jar
ln -sf $(build-classpath commons-codec) lib/
ln -sf $(build-classpath commons-collections) lib/commons-collections-2.1.1.jar
ln -sf $(build-classpath commons-digester) lib/commons-digester-1.7.jar
ln -sf $(build-classpath commons-javaflow) lib/commons-javaflow-20060411.jar
ln -sf $(build-classpath commons-logging) lib/commons-logging-1.0.4.jar
ln -sf $(build-classpath dom4j) lib/dom4j-1.6.1.jar
ln -sf $(build-classpath ecj) lib/jdt-compiler-3.1.1.jar
ln -sf $(build-classpath hibernate3/hibernate-core) lib/hibernate3.jar
ln -sf $(build-classpath hibernate/hibernate-jpa-2.0-api) lib/jpa.jar
ln -sf $(build-classpath springframework/spring-beans) lib/spring-beans-2.5.5.jar
ln -sf $(build-classpath springframework/spring-core) lib/spring-core-2.5.5.jar
ln -sf $(build-classpath groovy) lib/groovy-all-1.7.5.jar
ln -sf $(build-classpath hsqldb) lib/hsqldb-1.8.0-10.jar
ln -sf $(build-classpath itext) lib/iText-2.1.7.jar
ln -sf $(build-classpath jaxen) lib/jaxen-1.1.1.jar
ln -sf $(build-classpath jcommon) lib/jcommon-1.0.15.jar
ln -sf $(build-classpath jfreechart/jfreechart) lib/jfreechart-1.0.12.jar
ln -sf $(build-classpath jxl) lib/jxl-2.6.10.jar
ln -sf $(build-classpath log4j) lib/log4j-1.2.15.jar
ln -sf $(build-classpath objectweb-asm/asm) lib/
ln -sf $(build-classpath poi/apache-poi) lib/poi-3.6.jar
ln -sf $(build-classpath rhino) lib/rhino-1.7R1.jar
ln -sf $(build-classpath geronimo-saaj) lib/saaj-api-1.3.jar
ln -sf $(build-classpath tomcat-servlet-3.0-api) lib/servlet.jar
ln -sf $(build-classpath xalan-j2) lib/xalan-2.7.1.jar
ln -sf $(build-classpath xalan-j2-serializer) lib/serializer.jar
ln -sf $(build-classpath xerces-j2) lib/xercesImpl-2.7.0.jar
ln -sf $(build-classpath xml-commons-apis) lib/xml-apis.jar
ln -sf $(build-classpath xml-commons-apis-ext) lib/xml-apis-ext.jar

# remove. cause: unwanted
rm -rf src/org/w3c/tools/codec/Base64*

# remove. cause: unavailable build deps
rm -rf src/net/sf/jasperreports/data/mondrian/* \
  src/net/sf/jasperreports/olap/*

sed -i 's|deprecation="true"|deprecation="false"|' build.xml

%build
# DO NOT USE maven for build
%ant jar docs

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -m 644 dist/%{name}-applet-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-applet.jar
install -m 644 dist/%{name}-javaflow-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-javaflow.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar -a "%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
rm -rf dist/docs/api

%files
%{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc *.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%files manual
%doc dist/docs/*
%doc license.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt1_3jpp7
- new version

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

