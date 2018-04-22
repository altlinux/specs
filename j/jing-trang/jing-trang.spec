Epoch: 0
Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: zip
# END SourceDeps(oneline)
%filter_from_requires /.etc.java.jing-trang.conf/d
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# TODO:
# - Install dtdinst's schemas, XSL etc as non-doc and to system catalogs?
# - Drop isorelax and xerces license texts and references to them because
#   our package does not actually contain them?

%if 0%{?fedora} || 0%{?rhel} >= 7
%global headless -headless
%endif

Name:           jing-trang
Version:        20151127
Release:        alt1_3jpp8
Summary:        Schema validation and conversion based on RELAX NG

License:        BSD
URL:            https://github.com/relaxng/jing-trang
Source0:        https://github.com/relaxng/jing-trang/archive/V%{version}.tar.gz
# Applicable parts submitted upstream:
# https://github.com/relaxng/jing-trang/pull/215
# https://github.com/relaxng/jing-trang/pull/216
Patch0:         0001-Various-build-fixes.patch
# Saxon "HE" doesn't work for this, no old Saxon available, details in #655601
Patch1:         0002-Use-Xalan-instead-of-Saxon-for-the-build-655601.patch
Patch2:         %{name}-20091111-datatype-sample.patch
BuildArch:      noarch

%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  ant-trax
%else
BuildRequires:  ant >= 1.8.2
%endif
BuildRequires:  bsh
BuildRequires:  isorelax
BuildRequires:  java-devel-openjdk >= 1.6.0
BuildRequires:  java-javadoc
BuildRequires:  javacc
BuildRequires:  jpackage-utils
BuildRequires:  qdox
BuildRequires:  relaxngDatatype
BuildRequires:  relaxngDatatype-javadoc
BuildRequires:  saxon >= 9.3
BuildRequires:  testng
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-resolver
Source44: import.info

%description
%{summary}.

%package     -n jing
Summary:        RELAX NG validator in Java
Group:          Text tools
Requires:       jpackage-utils
Requires:       java%{?headless} >= 1.5.0
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-resolver

%description -n jing
Jing is a RELAX NG validator written in Java.  It implements the RELAX
NG 1.0 Specification, RELAX NG Compact Syntax, and parts of RELAX NG
DTD Compatibility, specifically checking of ID/IDREF/IDREFS.  It also
has experimental support for schema languages other than RELAX NG;
specifically W3C XML Schema, Schematron 1.5, and Namespace Routing
Language.

%package     -n jing-javadoc
Summary:        Javadoc API documentation for Jing
Group:          Development/Java
Requires:       java-javadoc
Requires:       relaxngDatatype-javadoc
BuildArch: noarch

%description -n jing-javadoc
Javadoc API documentation for Jing.

%package     -n trang
Summary:        Multi-format schema converter based on RELAX NG
Group:          Text tools
Requires:       jpackage-utils
Requires:       java%{?headless} >= 1.5.0
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-resolver

%description -n trang
Trang converts between different schema languages for XML.  It
supports the following languages: RELAX NG (both XML and compact
syntax), XML 1.0 DTDs, W3C XML Schema.  A schema written in any of the
supported schema languages can be converted into any of the other
supported schema languages, except that W3C XML Schema is supported
for output only, not for input.

%package     -n dtdinst
Summary:        XML DTD to XML instance format converter
Group:          Text tools
Requires:       jpackage-utils
Requires:       java%{?headless} >= 1.5.0

%description -n dtdinst
DTDinst is a program for converting XML DTDs into an XML instance
format.


%prep
%setup -q
rm -r gcj mod/datatype/src/main/org $(find . -name "*.jar")
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i -e 's/\r//g' lib/isorelax.copying.txt
find . -name "OldSaxon*.java" -delete # No "old" saxon available in Fedora
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/dtdinst/\1"|' \
    dtdinst/index.html
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/trang/\1"|' \
    trang/doc/trang.html trang/doc/trang-manual.html


%build
CLASSPATH=$(build-classpath \
    beust-jcommander xalan-j2 xalan-j2-serializer saxon) \
%ant -Dlib.dir=%{_javadir} -Dbuild.sysclasspath=last dist


%install
rm -rf $RPM_BUILD_ROOT *-%{version}

install -dm 755 $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}}

unzip build/dist/jing-%{version}.zip
install -Dpm 644 jing-%{version}/bin/jing.jar $RPM_BUILD_ROOT%{_javadir}
mv jing-%{version}/doc/api $RPM_BUILD_ROOT%{_javadocdir}/jing
ln -s %{_javadocdir}/jing jing-%{version}/doc/api
rm -f jing-%{version}/sample/datatype/datatype-sample.jar
%jpackage_script com.thaiopensource.relaxng.util.Driver "" "" jing:relaxngDatatype:xml-commons-resolver:xerces-j2 jing true
mkdir -p jing-%{version}/_licenses
mv jing-%{version}/doc/*copying.* jing-%{version}/_licenses

unzip build/dist/trang-%{version}.zip
install -pm 644 trang-%{version}/trang.jar $RPM_BUILD_ROOT%{_javadir}
%jpackage_script com.thaiopensource.relaxng.translate.Driver "" "" trang:relaxngDatatype:xml-commons-resolver:xerces-j2 trang true

unzip build/dist/dtdinst-%{version}.zip
install -pm 644 dtdinst-%{version}/dtdinst.jar $RPM_BUILD_ROOT%{_javadir}
%jpackage_script com.thaiopensource.xml.dtd.app.Driver "" "" dtdinst dtdinst true


%files -n jing
%doc --no-dereference jing-%{version}/_licenses/*
%doc --no-dereference jing-%{version}/readme.html
%doc --no-dereference jing-%{version}/doc
%doc --no-dereference jing-%{version}/sample
%{_bindir}/jing
%{_javadir}/jing.jar

%files -n jing-javadoc
%doc --no-dereference jing-%{version}/_licenses/*
%{_javadocdir}/jing/

%files -n trang
%doc --no-dereference trang-%{version}/copying.txt
%doc trang-%{version}/*.html
%{_bindir}/trang
%{_javadir}/trang.jar

%files -n dtdinst
%doc --no-dereference dtdinst-%{version}/copying.txt
%doc dtdinst-%{version}/*.html
%doc dtdinst-%{version}/*.rng
%doc dtdinst-%{version}/*.xsl
%doc dtdinst-%{version}/dtdinst.rnc.txt
%doc dtdinst-%{version}/teixml.dtd.txt
%doc dtdinst-%{version}/example
%{_bindir}/dtdinst
%{_javadir}/dtdinst.jar


%changelog
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

