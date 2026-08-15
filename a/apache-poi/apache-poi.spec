%def_without bootstrap
%global reldate 20250401

Name: apache-poi
Version: 5.4.1
Release: alt2
Summary: The Java API for Microsoft Documents
License: Apache-2.0 and MIT
Group: Development/Java
URL: http://poi.apache.org/

ExclusiveArch: x86_64 aarch64 loongarch64

Source0: https://dlcdn.apache.org/poi/release/src/%{name}-src-%{version}-%{?reldate}.tar.gz
Source1: gradle-cache.tar

# Supported Java version 
Patch0: apache-poi-alt-java-version.patch
# Remove version from pom filenames
Patch1: apache-poi-alt-remove-version-from-pom-filename.patch

BuildArch: noarch

BuildRequires: gcc-c++ rpm-build-java swig unzip
BuildRequires: java-21-openjdk-devel
BuildRequires: gradle
BuildRequires: maven-local
BuildRequires: pom2metadata

#Fonts for testing
BuildRequires: fontconfig fonts-ttf-liberation fonts-ttf-liberation

%description
The Apache POI Project's mission is to create and maintain Java APIs for
manipulating various file formats based upon the Office Open XML standards
(OOXML) and Microsoft's OLE 2 Compound Document format (OLE2). In short, you
can read and write MS Excel files using Java. In addition, you can read and
write MS Word and MS PowerPoint files using Java. Apache POI is your Java
Excel solution (for Excel 97-2008). We have a complete API for porting other
OOXML and OLE2 formats and welcome others to participate.

OLE2 files include most Microsoft Office files such as XLS, DOC, and PPT as
well as MFC serialization API based file formats. The project provides APIs
for the OLE2 Filesystem (POIFS) and OLE2 Document Properties (HPSF).

Office OpenXML Format is the new standards based XML file format found in
Microsoft Office 2007 and 2008. This includes XLSX, DOCX and PPTX. The
project provides a low level API to support the Open Packaging Conventions
using openxml4j.

For each MS Office application there exists a component module that attempts
to provide a common high level Java API to both OLE2 and OOXML document
formats. This is most developed for Excel workbooks (SS=HSSF+XSSF). Work is
progressing for Word documents (HWPF+XWPF) and PowerPoint presentations
(HSLF+XSLF).

The project has recently added support for Outlook (HSMF). Microsoft opened
the specifications to this format in October 2007. We would welcome
contributions.

There are also projects for Visio (HDGF) and Publisher (HPBF).

%prep
%setup -n %{name}-src-%{version}-%{?reldate}
test -d ~/.gradle && rm -rf ~/.gradle
%if_without bootstrap
tar xf %SOURCE1 -C ~
%endif
%patch0 -p1
%patch1 -p2

%build
%global gradle_target srcDistTar generatePomFileForPOIPublication
%if_without bootstrap
gradle --no-daemon --offline %gradle_target
gradle --no-daemon --offline poi-ooxml:generatePomFileForPOIPublication
%else
gradle --no-daemon %gradle_target
gradle --no-daemon poi-ooxml:generatePomFileForPOIPublication
%endif
find build/dist -name \*sources.\* -delete
# Generate metadata for maven-metadata
mkdir maven-metadata
for i in build/dist/maven/*/*.pom;do 
	d="$(dirname $i)"
	n="$(basename $d)"
	pom2metadata $i maven-metadata/$n.xml poi
done

%install
mkdir -p %buildroot%_javadir/poi
find build/dist -name \*.jar | grep -Ev 'tests\.jar' | while read i; do n="$(basename $i)";cp "$i" "%buildroot%_javadir/poi/${n/-%version/}";done
mkdir -p %buildroot%_mavenpomdir
find build/dist -name \*.pom -exec cp '{}' %buildroot%_mavenpomdir ';'
mkdir -p %buildroot%_datadir/maven-metadata
cp maven-metadata/*.xml %buildroot%_datadir/maven-metadata

%files
%doc README.rst KEYS
%_javadir/poi/*
%_mavenpomdir/*
%_datadir/maven-metadata/*.xml

%changelog
* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Packaged xmvn metainfo files.

* Sun Jul 06 2025 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- new version
- build with java 21

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_2jpp8
- fc29 update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.17-alt1_1jpp8
- java update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.15-alt1_2jpp8
- java update

* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.15-alt1_1jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.14-alt1_4jpp8
- new version

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_2jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt2_4jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt2_3jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_3jpp7
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp6
- new version

