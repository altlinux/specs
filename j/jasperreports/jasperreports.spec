Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:          jasperreports
# the JR newest release requires
# xmlbeans >= 2.5.0
# castor-xml modules see also https://bugzilla.redhat.com/show_bug.cgi?id=820676
Version:       4.0.2
Release:       alt2_15jpp8
Summary:       Report-generating tool
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

Patch7:        %{name}-%{version}-ecj4.patch

Patch8:        %{name}-%{version}-batik1.8.patch
Patch9:        %{name}-%{version}-doclint.patch

BuildRequires: javapackages-tools rpm-build-java

BuildRequires: ant
BuildRequires: antlr-tool
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
BuildRequires: ecj >= 1:3.4.2
BuildRequires: geronimo-saaj
BuildRequires: hibernate3
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hsqldb1
%if %{?fedora} > 20
BuildRequires: groovy18
BuildRequires: log4j12
BuildRequires: objectweb-asm3
%else
BuildRequires: groovy
BuildRequires: log4j
BuildRequires: objectweb-asm
%endif
BuildRequires: itext-core
BuildRequires: jaxen
BuildRequires: jcommon
BuildRequires: jexcelapi
BuildRequires: jfreechart
BuildRequires: rhino
BuildRequires: springframework
BuildRequires: springframework-beans
BuildRequires: glassfish-servlet-api
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
Requires:      ecj >= 1:3.4.2
Requires:      geronimo-saaj
Requires:      hsqldb1
Requires:      itext-core
Requires:      jcommon
Requires:      jfreechart
Requires:      springframework
Requires:      springframework-beans
Requires:      glassfish-servlet-api

Requires: javapackages-tools rpm-build-java
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
%patch8 -p0
%patch9 -p0


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
%if %{?fedora} > 17
ln -sf $(build-classpath hibernate3/hibernate-core-3) lib/hibernate3.jar
%else
ln -sf $(build-classpath hibernate3/hibernate-core) lib/hibernate3.jar
%endif
ln -sf $(build-classpath hibernate-jpa-2.0-api) lib/jpa.jar
ln -sf $(build-classpath springframework/spring-beans) lib/spring-beans-2.5.5.jar
ln -sf $(build-classpath springframework/spring-core) lib/spring-core-2.5.5.jar
%if %{?fedora} > 19
ln -sf $(build-classpath hsqldb1-1) lib/hsqldb-1.8.0-10.jar
%else
ln -sf $(build-classpath hsqldb) lib/hsqldb-1.8.0-10.jar
%endif
ln -sf $(build-classpath itext) lib/iText-2.1.7.jar
ln -sf $(build-classpath jaxen) lib/jaxen-1.1.1.jar
ln -sf $(build-classpath jcommon) lib/jcommon-1.0.15.jar
ln -sf $(build-classpath jfreechart/jfreechart) lib/jfreechart-1.0.12.jar
ln -sf $(build-classpath jxl) lib/jxl-2.6.10.jar
%if %{?fedora} > 21
ln -sf $(build-classpath log4j12-1.2.17) lib/log4j-1.2.15.jar
ln -sf $(build-classpath groovy18-1.8) lib/groovy-all-1.7.5.jar
ln -sf $(build-classpath objectweb-asm3/asm-distroshaded) lib/asm.jar
sed -i "s|org.objectweb.asm|org.objectweb.distroshaded.asm|" src/net/sf/jasperreports/compilers/JRGroovyCompiler.java
%else
ln -sf $(build-classpath log4j) lib/log4j-1.2.15.jar
ln -sf $(build-classpath groovy) lib/groovy-all-1.7.5.jar
ln -sf $(build-classpath objectweb-asm/asm) lib/asm.jar
%endif
ln -sf $(build-classpath poi/apache-poi) lib/poi-3.6.jar
ln -sf $(build-classpath rhino) lib/rhino-1.7R1.jar
ln -sf $(build-classpath geronimo-saaj) lib/saaj-api-1.3.jar
ln -sf $(build-classpath glassfish-servlet-api) lib/servlet.jar
ln -sf $(build-classpath xalan-j2) lib/xalan-2.7.1.jar
ln -sf $(build-classpath xalan-j2-serializer) lib/serializer.jar
ln -sf $(build-classpath xerces-j2) lib/xercesImpl-2.7.0.jar
ln -sf $(build-classpath xml-commons-apis) lib/xml-apis.jar
ln -sf $(build-classpath xml-commons-apis-ext) lib/xml-apis-ext.jar

# remove. cause: unwanted
rm -rf src/org/w3c/tools/codec/Base64*

# remove. cause: unavailable build deps
rm -rf src/net/sf/jasperreports/data/mondrian/* \
  src/net/sf/jasperreports/olap/* \
  src/net/sf/jasperreports/components/barcode4j/* \
  src/net/sf/jasperreports/components/barbecue/*

sed -i 's|deprecation="true"|deprecation="false"|' build.xml

sed -i 's|target="1.5" source="1.5"|target="1.6" source="1.6"|' build.xml

%pom_remove_dep net.sf.barcode4j:barcode4j
%pom_remove_dep net.sourceforge.barbecue:barbecue
%pom_remove_dep mondrian:mondrian
%pom_remove_dep com.keypoint:png-encoder

%pom_add_dep commons-codec:commons-codec::compile

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'bsh']/pom:groupId" bsh
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'bsh']/pom:version" 1.3.0

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'eclipse']/pom:groupId" org.eclipse.jdt
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jdtcore']/pom:artifactId" core

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:version" 1.8.9

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jcommon']/pom:groupId" org.jfree
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'jfreechart']/pom:groupId" org.jfree

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']/pom:artifactId" hibernate-core
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.hibernate']/pom:version" 3

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'commons-javaflow']/pom:groupId" org.apache.commons

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.persistence']/pom:groupId" org.hibernate.javax.persistence
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'persistence-api']/pom:artifactId" hibernate-jpa-2.0-api

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.xml.soap']/pom:groupId" org.apache.geronimo.specs
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'saaj-api']/pom:artifactId" geronimo-saaj_1.3_spec

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'rhino']/pom:groupId" org.mozilla
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'js']/pom:artifactId" rhino

# Force usage of servlet 3.1
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.servlet']/pom:version" 3.1.0
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.servlet']/pom:artifactId" javax.servlet-api

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

%files -f .mfiles
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-applet.jar
%{_javadir}/%{name}/%{name}-javaflow.jar
%doc changes.txt readme.txt
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%files manual
%doc dist/docs/*
%doc license.txt

%changelog
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

