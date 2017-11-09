Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xml-commons-apis
Version:       1.4.01
Release:       alt3_24jpp8
Summary:       APIs for DOM, SAX, and JAXP
License:       ASL 2.0 and W3C and Public Domain
URL:           http://xml.apache.org/commons/
BuildArch:     noarch

# From source control because the published tarball doesn't include some docs:
#   svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_4_01/java/external/
#   tar czf xml-commons-external-1.4.01-src.tar.gz external
Source0:       xml-commons-external-%{version}-src.tar.gz
Source1:       %{name}-MANIFEST.MF
Source2:       %{name}-ext-MANIFEST.MF
Source3:       http://repo1.maven.org/maven2/xml-apis/xml-apis/2.0.2/xml-apis-2.0.2.pom
Source4:       http://repo1.maven.org/maven2/xml-apis/xml-apis-ext/1.3.04/xml-apis-ext-1.3.04.pom

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: apache-parent

Provides:      xml-commons = %{version}-%{release}

# TODO: Ugh, this next line should be dropped since it actually provides JAXP 1.4 now...
Provides:      xml-commons-jaxp-1.3-apis = %{version}-%{release}
Source44: import.info
# jpackage deprecations
Conflicts: xml-commons-apis12 < 0:1.2.05
Obsoletes: xml-commons-apis12 < 0:1.2.05
Conflicts: xml-commons-jaxp-1.1-apis < 0:1.3.05
Obsoletes: xml-commons-jaxp-1.1-apis < 0:1.3.05
Conflicts: xml-commons-jaxp-1.2-apis < 0:1.3.05
Obsoletes: xml-commons-jaxp-1.2-apis < 0:1.3.05
Conflicts: xml-commons-jaxp-1.3-apis < 0:1.3.05
Obsoletes: xml-commons-jaxp-1.3-apis < 0:1.3.05
Conflicts: xml-commons-jaxp-1.4-apis < %version-%release
Obsoletes: xml-commons-jaxp-1.4-apis < %version-%release


%description
xml-commons-apis is designed to organize and have common packaging for
the various externally-defined standard interfaces for XML. This
includes the DOM, SAX, and JAXP.

%package manual
Group: Development/Java
Summary:       Manual for %{name}
BuildArch: noarch

%description manual
%{summary}.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
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

%mvn_file :xml-apis xml-commons-apis jaxp13 jaxp xml-commons-jaxp-1.3-apis
%mvn_file :xml-apis-ext xml-commons-apis-ext
%mvn_alias :xml-apis-ext xerces:dom3-xml-apis

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc

# inject OSGi manifests
jar ufm build/xml-apis.jar %{SOURCE1}
jar ufm build/xml-apis-ext.jar %{SOURCE2}

%mvn_artifact xml-apis-[0-9]*.pom build/xml-apis.jar
%mvn_artifact xml-apis-ext*.pom build/xml-apis-ext.jar

%install
%mvn_install -J build/docs/javadoc

# prevent apis javadoc from being included in doc
rm -rf build/docs/javadoc

%files -f .mfiles
%doc LICENSE NOTICE
%doc LICENSE.dom-documentation.txt README.dom.txt
%doc LICENSE.dom-software.txt LICENSE.sac.html
%doc LICENSE.sax.txt README-sax  README.sax.txt
%{_javadir}/*

%files manual
%doc build/docs/*

%files javadoc
%{_javadocdir}/*

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt3_24jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt3_22jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt3_20jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt3_19jpp8
- new version

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt1_14jpp7
- xml-commons replacement

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

