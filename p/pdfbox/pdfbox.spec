Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
Name:           pdfbox
Version:        1.7.0
Release:        alt3_4jpp7
Summary:        Java library for working with PDF documents

Group:          Development/Java
License:        ASL 2.0
URL:            http://pdfbox.apache.org/
Source0:        http://www.apache.org/dist/pdfbox/%{version}/%{name}-%{version}-src.zip
#Don't download anything
Patch0:         %{name}-nodownload.patch
#Use sysytem bitream-vera-sans-fonts instead of bundled fonts
Patch1:         %{name}-1.2.0-bitstream.patch
Patch2:         %{name}-lucene.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-deploy-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-war-plugin
BuildRequires:  apache-commons-logging
BuildRequires:  apache-rat-plugin
BuildRequires:  fonts-ttf-vera
BuildRequires:  bouncycastle-mail
BuildRequires:  fontconfig
BuildRequires:  icu4j
BuildRequires:  junit4
%if 0%{?fedora} >= 18
BuildRequires:  lucene
%else
BuildRequires:  lucene-demo >= 2.4.1
%endif
BuildRequires:  pcfi

BuildArch:      noarch

Requires:       jpackage-utils
Requires:       fonts-ttf-vera
Requires:       bouncycastle-mail
Requires:       fontbox
Requires:       icu4j
Requires:       apache-commons-logging
Requires:       jempbox

Obsoletes:      %{name}-app <= 1.6.0-4
Provides:       %{name}-app = %{version}-%{release}
Source44: import.info

%description
Apache PDFBox is an open source Java PDF library for working with PDF
documents. This project allows creation of new PDF documents, manipulation of
existing documents and the ability to extract content from documents. Apache
PDFBox also includes several command line utilities. Apache PDFBox is
published under the Apache License v2.0.


%package examples
Summary:        Examples for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description examples
This package contains examples for %{name}.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Provides:       fontbox-javadoc = %{version}-%{release}
Obsoletes:      fontbox-javadoc < %{version}-%{release}
Provides:       jempbox-javadoc = %{version}-%{release}
Obsoletes:      jempbox-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%package ant
Summary:        Apache PDFBox for Ant
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       ant

%description ant
%{summary}.


%package -n fontbox
Summary:        Apache FontBox
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       junit

%description -n fontbox
FontBox is a Java library used to obtain low level information from font
files. FontBox is a subproject of Apache PDFBox.


%package -n jempbox
Summary:        Apache JempBox
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       junit

%description -n jempbox
JempBox is an open source Java library that implements Adobe's XMP(TM)
specification. JempBox is a subproject of Apache PDFBox.


# Not compatible with lucene 3.6
%if 0%{?fedora} < 18
%package lucene
Summary:        Apache PDFBox for Lucene
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
%if 0%{?fedora} >= 18
Requires:       lucene
%else
Requires:       lucene-demo >= 2.4.1
%endif

%description lucene
%{summary}.
%endif


%prep
%setup -q
%patch0 -p1 -b .nodownload
%patch1 -p1 -b .bitstream
%patch2 -p1 -b .lucene
#Use jdk16 version of bcprov
sed -i -e s/jdk15/jdk16/g */pom.xml
# Don't build app (it's just a bundle of everything)
sed -i -e /app/d pom.xml
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
#Fix line endings
sed -i -e 's|\r||' RELEASE-NOTES.txt
#Remove META-INF file that does not exist
sed -i -e '/META-INF/d' pdfbox/pom.xml
#Remove included fonts
rm -r pdfbox/src/main/resources/org/apache/pdfbox/resources/ttf


%build
mvn-rpmbuild -Dadobefiles.jar=%{_javadir}/pcfi.jar install javadoc:aggregate


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}

for jar in */target/*.jar
do
  dir=$(dirname $jar)
  target=$(dirname $dir)
  jarname=$target
  [ -f ${dir}/%{name}-${target}-%{version}.jar ] && jarname=%{name}-${target}

  cp -p ${dir}/${jarname}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/${jarname}.jar

  cp -p ${target}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-${jarname}.pom
  %add_maven_depmap JPP-${jarname}.pom ${jarname}.jar
done

# Javadocs
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}

#Parent
cp -p parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-pdfbox-parent.pom
%add_maven_depmap JPP-pdfbox-parent.pom

#TODO - install/ship war


%files
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}

%files examples
%doc LICENSE.txt
%{_javadir}/%{name}-examples.jar
%{_mavenpomdir}/JPP-%{name}-examples.pom

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files ant
%doc LICENSE.txt
%{_javadir}/%{name}-ant.jar
%{_mavenpomdir}/JPP-%{name}-ant.pom

%files -n fontbox
%doc LICENSE.txt
%{_javadir}/fontbox.jar
%{_mavenpomdir}/JPP-fontbox.pom

%files -n jempbox
%doc LICENSE.txt
%{_javadir}/jempbox.jar
%{_mavenpomdir}/JPP-jempbox.pom

# Not compatible with lucene 3.6
%if 0%{?fedora} < 18
%files lucene
%doc LICENSE.txt
%{_javadir}/%{name}-lucene.jar
%{_mavenpomdir}/JPP-%{name}-lucene.pom
%endif


%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt3_4jpp7
- rebuild with maven-local

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt2_4jpp7
- new fc release

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt2_1jpp7
- fixed build with lucene3

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.0-alt1_1jpp7
- new release

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_3jpp6
- new jpp relase

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt2_1jpp5
- rebuild with new lucene

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7.3-alt1_1jpp5
- new jpackage release

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

