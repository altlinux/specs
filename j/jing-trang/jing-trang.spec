%define _unpackaged_files_terminate_build 1

Name: jing-trang
Version: 20241231
Release: alt1

Summary: Schema validation and conversion based on RELAX NG
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/relaxng/jing-trang
VCS: https://github.com/relaxng/jing-trang.git

Source0: %name-%version.tar
Source1: jing.pom
Source2: trang.pom
Source3: relaxng-site.tar
Patch0: %name-tests.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: zip
BuildRequires: git
BuildRequires: java-21-openjdk-devel
BuildRequires: java-javadoc
BuildRequires: javapackages-local
BuildRequires: javacc
BuildRequires: testng
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: xalan-j2
BuildRequires: mvn(isorelax:isorelax)
BuildRequires: mvn(net.sf.saxon:Saxon-HE)
BuildRequires: xerces-j2
BuildRequires: xml-commons-resolver

%description
%summary.

%package -n jing
Summary: RELAX NG validator in Java
Group: Development/Java

%description -n jing
Jing is a RELAX NG validator written in Java. It implements the RELAX
NG 1.0 Specification, RELAX NG Compact Syntax, and parts of RELAX NG
DTD Compatibility, specifically checking of ID/IDREF/IDREFS. It also
has experimental support for schema languages other than RELAX NG;
specifically W3C XML Schema, Schematron 1.5, and Namespace Routing
Language.

%package -n jing-javadoc
Summary: Javadoc API documentation for Jing
Group: Development/Java
BuildArch: noarch

%description -n jing-javadoc
Javadoc API documentation for Jing.

%package -n trang
Summary: Multi-format schema converter based on RELAX NG
Group: Text tools

%description -n trang
Trang converts between different schema languages for XML. It supports
RELAX NG XML and compact syntax, XML 1.0 DTDs, and W3C XML Schema output.

%package -n dtdinst
Summary: XML DTD to XML instance format converter
Group: Text tools

%description -n dtdinst
DTDinst converts XML DTDs into an XML instance format.

%prep
%setup -a3
%autopatch -p1
%mvn_file org.relaxng:jing jing
%mvn_file org.relaxng:trang trang
%mvn_package org.relaxng:jing jing
%mvn_package org.relaxng:trang trang
mkdir -p rpm-metadata/jing rpm-metadata/trang
cp %SOURCE1 rpm-metadata/jing/pom.xml
cp %SOURCE2 rpm-metadata/trang/pom.xml
# Launchers and upstream modules use these system libraries directly.
%pom_add_dep xml-resolver:xml-resolver:1.2 rpm-metadata/jing
%pom_add_dep xerces:xercesImpl:2.11.0 rpm-metadata/jing
%pom_add_dep xml-resolver:xml-resolver:1.2 rpm-metadata/trang
%pom_add_dep xerces:xercesImpl:2.11.0 rpm-metadata/trang
rm -rf gcj
find . -name '*.jar' -type f -delete
mkdir -p .system-libs
for lib in ant ant-launcher javacc xalan xercesImpl resolver isorelax \
    saxon9 testng; do
    case "$lib" in
        ant) jar=%_javadir/ant.jar ;;
        ant-launcher) jar=%_javadir/ant-launcher.jar ;;
        javacc) package=javacc ;;
        xalan) package=xalan-j2 ;;
        xercesImpl) package=xerces-j2 ;;
        resolver) package=xml-commons-resolver ;;
        isorelax) package=isorelax ;;
        saxon9) package=saxon ;;
        testng) package=testng ;;
    esac
    if [ -n "${package-}" ]; then
        jar=$(build-classpath "$package")
        unset package
    fi
    jar=${jar%%:*}
    if [ "$lib" = testng ]; then
        # ALT TestNG advertises an absent optional YAML suite parser.
        # These XML suites use TestNG's built-in SuiteXmlParser.
        cp --remove-destination "$jar" ".system-libs/$lib.jar"
        zip -qd ".system-libs/$lib.jar" META-INF/services/org.testng.xml.ISuiteParser
    else
        ln -s "$jar" ".system-libs/$lib.jar"
    fi
    ln -s "../.system-libs/$lib.jar" "lib/$lib.jar"
done

%build
classpath=$(build-classpath xalan-j2 saxon)
# Modern Saxon uses XML Resolver; stock Saxon 9 does not.
if resolver=$(build-classpath xmlresolver 2>/dev/null); then
    classpath=$classpath:$resolver
fi
export CLASSPATH=$classpath:%_javadir/serializer.jar
%ant -Dlib.dir=%_builddir/%name-%version/lib \
    -Dbuild.sysclasspath=last ant-jar ant-javadoc
%mvn_artifact rpm-metadata/jing/pom.xml build/jing.jar
%mvn_artifact rpm-metadata/trang/pom.xml build/trang.jar

%install
rm -rf %buildroot
mkdir -p %buildroot%_javadir %buildroot%_javadocdir

%mvn_install
cp -a build/api %buildroot%_javadocdir/jing
# This RPM macro requires all arguments on one physical line.
%define jing_cp jing:isorelax:saxon:xml-commons-resolver:xerces-j2
%define trang_cp trang:xml-commons-resolver:xerces-j2
%define trang_main com.thaiopensource.relaxng.translate.Driver
%define dtdinst_main com.thaiopensource.xml.dtd.app.Driver
%jpackage_script com.thaiopensource.relaxng.util.Driver "" "" %jing_cp jing true
# Saxon 13 needs XML Resolver; older Saxon can run without it.
sed -i '/^set_classpath /i\
if /usr/bin/build-classpath xmlresolver >/dev/null 2>\&1; then\
    BASE_JARS="$BASE_JARS xmlresolver"\
fi' %buildroot%_bindir/jing
%jpackage_script %trang_main "" "" %trang_cp trang true

install -pm 644 build/dtdinst.jar %buildroot%_javadir
%jpackage_script %dtdinst_main "" "" dtdinst dtdinst true

install -Dm644 copying.html alt-package-licenses/jing/copying.html
install -Dm644 copying.txt alt-package-licenses/jing/copying.txt
install -Dm644 lib/isorelax.copying.txt \
    alt-package-licenses/isorelax/copying.txt
install -Dm644 lib/xerces.copying.txt alt-package-licenses/xerces/copying.txt
install -Dm644 trang/copying.txt alt-package-licenses/trang/copying.txt
install -Dm644 dtdinst/copying.txt alt-package-licenses/dtdinst/copying.txt

%check
classpath=$(build-classpath xalan-j2 saxon beust-jcommander/jcommander slf4j/api)
if resolver=$(build-classpath xmlresolver 2>/dev/null); then
    classpath=$classpath:$resolver
fi
export CLASSPATH=$classpath:%_javadir/serializer.jar
%ant -f modbuild.xml -Dlib.dir=%_builddir/%name-%version/lib \
    -Dbuild.sysclasspath=last test

%files -n jing -f .mfiles-jing
%doc alt-package-licenses
%_bindir/jing

%files -n jing-javadoc
%_javadocdir/jing/

%files -n trang -f .mfiles-trang
%doc trang/doc/*.html
%_bindir/trang

%files -n dtdinst
%doc dtdinst/*.html dtdinst/*.xsl
%doc dtdinst/dtdinst.rnc dtdinst/teixml.dtd dtdinst/example
%_bindir/dtdinst
%_javadir/dtdinst.jar

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 20241231-alt1
- New version.

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 0:20151127-alt4_8jpp8
- added BR: unzip

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0:20151127-alt3_8jpp8
- build with compat relaxngDatatype

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:20151127-alt2_8jpp8
- use jvm_run

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:20151127-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:20151127-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:20151127-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:20151127-alt1_2jpp8
- new version

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:20131210-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:20131210-alt1_6jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:20131210-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:20091111-alt3_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:20091111-alt3_12jpp7
- new release

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:20091111-alt3_11jpp7
- build with ant-junit

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0:20091111-alt2_11jpp7
- fc update

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:20091111-alt1_11jpp7
- initial build

