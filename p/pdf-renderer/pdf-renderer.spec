# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global alternate_name PDFRenderer
%global svn_date 20110310
%global svn_version 128svn

Summary:        A 100% Java PDF renderer and viewer
Name:           pdf-renderer
Version:        0
Release:        alt3_0.14.128svn.20110310jpp8
#src/com/sun/pdfview/decode/CCITTFaxDecoder.java under a BSD-alike License
#src/com/sun/pdfview/font/ttf/resource/glyphlist.txt and src/com/sun/pdfview/font/ttf/AdobeGlyphList.java
#are under Adobe Glyph List License
License:        LGPLv2+ and MIT and BSD
URL:            https://pdf-renderer.dev.java.net/
Group:          Development/Java
Source0:        %{name}-%{svn_version}-%{svn_date}.tar.bz2
# To fetch the source code
Source1:        %{name}-snapshot.sh
BuildRequires:  ant
BuildRequires:  ant-apache-regexp
BuildRequires:  jpackage-utils
BuildRequires:  urw-fonts
BuildArch:      noarch
Requires:       jpackage-utils >= 1.5
Requires:       urw-fonts
Provides:       %{alternate_name} == %{version}-%{release}
Source44: import.info

%description
The PDF Renderer is just what the name implies: an open source,
all Java library which renders PDF documents to the screen using 
Java2D. Typically this means drawing into a Swing panel, but it 
could also draw to other Graphics2D implementations. It could be 
used to draw on top of PDFs, share them over a network, convert 
PDFs to PNG images, or maybe even project PDFs into a 3D scene.

%package javadoc
Summary:        Javadoc for %{alternate_name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for the %{alternate_name} package.

%prep
%setup -q -n %{name}-%{svn_version}-%{svn_date}

# Remove preshipped binaries
find . -name "*.jar" -exec rm {} \;

# Fix encoding issues
find . -name "*.java" -exec native2ascii {} {} \;

# Remove preshipped fonts and ...
find . -name "*.pfb" -exec rm {} \;

# ... tell the program to use system-fonts instead.
# Script provided by Mamoru Tasaka:
# https://bugzilla.redhat.com/show_bug.cgi?id=466394#c4
# -------------------------------------------------------------
pushd src/com/sun/pdfview/font/res/
INPUT=BaseFonts.properties
OUTPUT=BaseFonts.properties.1
FONTDIR=%{_datadir}/fonts/default/Type1

rm -f $OUTPUT
cat $INPUT | while read line
 do
 newline=$line
 if echo $newline | grep -q 'file=.*pfb'
  then
  pfbname=$(echo $newline | sed -e 's|^.*file=||')
  newline=$(echo $newline | sed -e "s|file=|file=${FONTDIR}/|")
 elif echo $newline | grep -q 'length='
  then
  size=$(ls -al ${FONTDIR}/$pfbname | awk '{print $5}')
  newline=$(echo $newline | sed -e "s|length=.*|length=$size|")
 fi
 echo $newline >> $OUTPUT
done
mv -f $OUTPUT $INPUT
popd
# -------------------------------------------------------------

%build
%ant ||:

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{alternate_name}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# compat symlink (requected by @REAL); just let it be (but use pdf-renderer.jar, please!)
pushd %buildroot%_javadir
ln -s pdf-renderer.jar PDFRenderer.jar

%files
%doc demos
%{_javadir}/%{name}.jar
%_javadir/PDFRenderer.jar

%files javadoc
%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.14.128svn.20110310jpp8
- fixed build with javadoc 8

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.14.128svn.20110310jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.13.128svn.20110310jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.10.128svn.20110310jpp7
- fc update

* Mon May 25 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt3_0.5.20090405cvsjpp5
- added symlink for another jar name (PDFRenderer)

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.5.20090405cvsjpp5
- noarch javadoc

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.5.20090405cvsjpp5
- new version

