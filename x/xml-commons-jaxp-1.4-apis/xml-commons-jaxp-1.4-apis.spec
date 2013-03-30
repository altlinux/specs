%define oldname xml-commons-apis
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xml-commons-jaxp-1.4-apis
Version:       1.4.01
Release:       alt1_8jpp7
Summary:       APIs for DOM, SAX, and JAXP
Group:         Development/Java
License:       ASL 2.0 and W3C and Public Domain
URL:           http://xml.apache.org/commons/

# From source control because the published tarball doesn't include some docs:
#   svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_4_01/java/external/
#   tar czf xml-commons-external-1.4.01-src.tar.gz external
Source0:       xml-commons-external-%{version}-src.tar.gz
Source1:       %{oldname}-MANIFEST.MF
Source2:       %{oldname}-ext-MANIFEST.MF
Source3:       http://repo1.maven.org/maven2/xml-apis/xml-apis/2.0.2/xml-apis-2.0.2.pom
Source4:       http://repo1.maven.org/maven2/xml-apis/xml-apis-ext/1.3.04/xml-apis-ext-1.3.04.pom

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: zip
Requires:      jpackage-utils
Requires(post):    jpackage-utils
Requires(postun):  jpackage-utils

#Obsoletes:     xml-commons < %{version}-%{release}
#Provides:      xml-commons = %{version}-%{release}

Provides:      xml-commons-apis = %{version}-%{release}

%description
xml-commons-apis is designed to organize and have common packaging for
the various externally-defined standard interfaces for XML. This
includes the DOM, SAX, and JAXP.

%package manual
Summary:       Manual for %{oldname}
Group:         Development/Java
BuildArch: noarch

%description manual
%{summary}.

%package javadoc
Summary:       Javadoc for %{oldname}
Group:         Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n external
# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Fix file encodings
iconv -f iso8859-1 -t utf-8 LICENSE.dom-documentation.txt > \
  LICENSE.dom-doc.temp && mv -f LICENSE.dom-doc.temp LICENSE.dom-documentation.txt
iconv -f iso8859-1 -t utf-8 LICENSE.dom-software.txt > \
  LICENSE.dom-sof.temp && mv -f LICENSE.dom-sof.temp LICENSE.dom-software.txt

# remove bogus section from poms
cp %{SOURCE3} %{SOURCE4} .
sed -i '/distributionManagement/,/\/distributionManagement/ {d}' *.pom

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/xml-apis.jar META-INF/MANIFEST.MF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/xml-apis-ext.jar META-INF/MANIFEST.MF

# Jars
install -pD -T build/xml-apis.jar %{buildroot}%{_javadir}/%{name}.jar
install -pDm 644 xml-apis-[0-9]*.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap xml-apis xml-apis %{version} JPP %{name}

install -pD -T build/xml-apis-ext.jar %{buildroot}%{_javadir}/%{name}-ext.jar
install -pDm 644 xml-apis-ext*.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}-ext.pom
%add_to_maven_depmap xml-apis xml-apis-ext %{version} JPP %{name}-ext

# for better interoperability with the jpp apis packages
#ln -sf %{name}.jar %{buildroot}%{_javadir}/jaxp13.jar
#ln -sf %{name}.jar %{buildroot}%{_javadir}/jaxp.jar
#ln -sf %{name}.jar %{buildroot}%{_javadir}/xml-commons-jaxp-1.3-apis.jar

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# prevent apis javadoc from being included in doc
rm -rf build/docs/javadoc

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis_%{name}<<EOF
%{_javadir}/xml-commons-apis.jar	%{_javadir}/%{name}.jar	10400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_%{name}<<EOF
%{_javadir}/jaxp.jar	%{_javadir}/%{name}.jar	10400
EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/dom_xml-%{name}<<EOF
#%{_javadir}/dom.jar	%{_javadir}/%{name}.jar	10400
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax2_xml-%{name}<<EOF
#%{_javadir}/sax2.jar	%{_javadir}/%{name}.jar	10400
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/sax_xml-%{name}<<EOF
#%{_javadir}/sax.jar	%{_javadir}/%{name}.jar	10400
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xslt_%{name}<<EOF
#%{_javadir}/xslt.jar	%{_javadir}/%{name}.jar	10400
#EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xml-commons-apis-javadoc_%{name}-javadoc<<EOF
%{_javadocdir}/xml-commons-apis	%{_javadocdir}/%{name}/	10400
EOF

%files
%doc LICENSE NOTICE
%doc LICENSE.dom-documentation.txt README.dom.txt
%doc LICENSE.dom-software.txt LICENSE.sac.html
%doc LICENSE.sax.txt README-sax  README.sax.txt
%{_javadir}/*
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-ext.pom
%_altdir/xml-commons-apis_%{name}
%_altdir/jaxp_%{name}

%files manual
%doc build/docs/*

%files javadoc
%{_javadocdir}/*
%_altdir/xml-commons-apis-javadoc_%{name}-javadoc

%changelog
* Sat Mar 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt1_8jpp7
- new version

