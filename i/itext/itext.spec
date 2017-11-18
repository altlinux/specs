BuildRequires: javapackages-local
Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global alternate_name iText

Summary:          A Free Java-PDF library
Name:             itext
Version:          2.1.7
Release:          alt3_36jpp8
#src/toolbox/com/lowagie/toolbox/Versions.java is MPLv1.1 or MIT
#src/toolbox/com/lowagie/toolbox/plugins/XML2Bookmarks.java is MPLv1.1 or LGPLv2+
#src/rups/com/lowagie/rups/Rups.java is LGPLv2+
#src/rups/com/lowagie/rups/view/icons/ are under CC-BY
#src/core/com/lowagie/text/xml/XmlDomWriter.java is under ASL 2.0
#src/core/com/lowagie/text/pdf/LZWDecoder.java is under BSD
#src/core/com/lowagie/text/pdf/fonts/cmaps/CodespaceRange.java is under BSD
#src/core/com/lowagie/text/pdf/fonts are under APAFML
#src/core/com/lowagie/text/pdf/codec/TIFFConstants.java is under libtiff
License:          (LGPLv2+ or MPLv1.1) and ASL 2.0 and BSD and LGPLv2+ and (MPLv1.1 or MIT) and CC-BY and APAFML and libtiff
URL:              http://www.lowagie.com/iText/
Group:            Development/Other
# sh itext-create-tarball.sh 2.1.7
Source0:          %{name}-%{version}.tar.xz
Source2:          http://repo2.maven.org/maven2/com/lowagie/itext/%{version}/itext-%{version}.pom
Source3:          itext-rups.sh
Source4:          itext-rups.desktop
Source6:          itext-toolbox.desktop
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools checkout -r v2_1_7 org.eclipse.orbit/com.lowagie.text/META-INF/MANIFEST.MF
# tar cf export-manifest.tar org.eclipse.orbit/com.lowagie.text/META-INF/MANIFEST.MF
Source7:          export-manifest.tar
Source8:          http://repo2.maven.org/maven2/com/lowagie/itext-rtf/%{version}/itext-rtf-%{version}.pom
Source9:          http://repo2.maven.org/maven2/com/lowagie/itext-rups/%{version}/itext-rups-%{version}.pom
Source10:         itext-create-tarball.sh
Patch1:           itext-2.1.5-pdftk.patch

# The iText POM specifies that it requires bouncycastle's "jdk14" JARs
# but we have "jdk16".
#Patch2:           itext-2.1.7-fixpomforbc.patch
# Maven's Doxia plugin explicitly requires these XML output interfaces
# of iText.  They were removed in iText 1.4.4 [1].  iText versions prior
# to 1.5.x had questionable licensing [2] so rather than try to create
# an itext1 package, I have forward-ported these classes.  The doxia
# developers have told me on IRC on 2009-08-27 that the iText dependency
# will likely be deprecated meaning we won't have to keep these forever.
#
# I've opened a bug with iText:
#
# https://sourceforge.net/tracker/?func=detail&aid=2846427&group_id=15255&atid=365255
#
# and commented on the Doxia but related to this:
#
# http://jira.codehaus.org/browse/DOXIA-53
#
# -- Andrew Overholt, 2009-08-28
#
# [1]
# http://www.1t3xt.com/about/history.php?branch=history.10&node=14
# [2]
# https://bugzilla.redhat.com/show_bug.cgi?id=236309
Patch3:           itext-xmloutput.patch
# Use orbit manifest so the manifest exports packages properly.
Patch4:           itext-manifest.patch
Patch5:           itext-remove-unmappable.patch
# Port to bouncycastle 1.50 Thanks to Michal Srb
Patch6:           0001-Port-to-bouncycastle-1.50.patch
Patch7:           itext-2.1.7-bouncycastle1.52.patch

#1 Fix for transparency issue with setClip method in PdfGraphics2D
#2 Fix for transparency bleeding for Batik gradients
#3 Fix for stroke opacity state in the create() method of PdfGraphics2D
#4 Method to directly write AWT GlyphVectors to PDF for Indic scripts support
#5 No character spacing in justified lines with a single word
# Origin: other, http://jaspersoft.artifactoryonline.com/jaspersoft/third-party-ce-artifacts/com/lowagie/itext/2.1.7.js5/itext-2.1.7.js5-sources.jar
Patch8:           itext-2.1.7-tibco-changes.patch

BuildRequires:    ant
BuildRequires:    bouncycastle-mail >= 1.52
BuildRequires:    bouncycastle-pkix >= 1.52
BuildRequires:    desktop-file-utils
BuildRequires:    dom4j
BuildRequires:    ImageMagick
BuildRequires:    pdf-renderer
BuildRequires:    java-devel >= 1.7
BuildRequires:    jpackage-utils

BuildArch:        noarch

Provides:         %{alternate_name} == %{version}-%{release}
Requires:         %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
Source44: import.info

%description
iText is a library that allows you to generate PDF files on the fly. The iText
classes are very useful for people who need to generate read-only, platform
independent documents containing text, lists, tables and images. The library is
especially useful in combination with Java(TM) technology-based Servlets: The
look and feel of HTML is browser dependent; with iText and PDF you can control
exactly how your servlet's output will look.

%package core
Summary:          The core iText Java-PDF library
Group:            Development/Other
BuildArch:        noarch
Requires:         bouncycastle-mail >= 1.52
Requires:         bouncycastle-pkix >= 1.52
Requires:         jpackage-utils
Obsoletes:        itext < 2.1.7-12
Obsoletes: itext2 <= 2.1.7-alt1_9jpp6

%description core
The core package contains the main iText library and the related maven POM
files.

%package rtf
Summary:        Library to output Rich Text Files
Group:          Development/Other
BuildArch:      noarch
License:        MPLv1.1 or LGPLv2+
Requires:       %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

%description rtf
The RTF package is an extension of the iText library and allows iText to output
Rich Text Files in addition to PDF files. These files can then be viewed and
edited with RTF viewers such as OpenOffice.org Writer.

%package rups
Summary:        Reading/Updating PDF Syntax
Group:          Development/Java
BuildArch:      noarch
License:        LGPLv2+ and CC-BY
Requires:       %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
Requires:       dom4j
Requires:       pdf-renderer

%description rups
iText RUPS is a tool that combines SUN's PDF Renderer (to view PDF documents),
iText's PdfReader (to inspect the internal structure of a PDF file), and
iText's PdfStamper to manipulate a PDF file.

%package toolbox
Summary:        Some %{alternate_name} tools
Group:          Development/Java
BuildArch:      noarch
License:        MPLv1.1 or MIT
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description toolbox
iText is a free open source Java-PDF library released on SF under the MPL/LGPL;
iText comes with a simple GUI: the iText toolbox. The original developers of
iText want to publish this toolbox as a separate project under the more
permissive MIT license. This is a utility that allows you to use a number of
iText tools.

%package javadoc
Summary:        Javadoc for %{alternate_name}
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils

%description javadoc
API documentation for the %{alternate_name} package.


%prep
%setup -q -c -T -a 0
%patch1 -p1 -b .pdftk
%patch3 -p0 -b .xmloutput
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p1

sed -i.bcprov1.54 "s|algorithmidentifier.getObjectId().getId|algorithmidentifier.getAlgorithm().getId|" \
 src/core/com/lowagie/text/pdf/PdfPublicKeySecurityHandler.java

cp -pr %{SOURCE2} JPP-itext.pom
%pom_remove_dep bouncycastle:bcmail-jdk14 JPP-itext.pom
%pom_add_dep org.bouncycastle:bcmail-jdk15on JPP-itext.pom
%pom_remove_dep bouncycastle:bcprov-jdk14 JPP-itext.pom
%pom_add_dep org.bouncycastle:bcprov-jdk15on JPP-itext.pom
%pom_remove_dep bouncycastle:bctsp-jdk14 JPP-itext.pom
%pom_add_dep org.bouncycastle:bcpkix-jdk15on JPP-itext.pom

cp -pr %{SOURCE8} JPP-%{name}-rtf.pom
cp -pr %{SOURCE9} JPP-%{name}-rups.pom

for p in rtf rups ; do
%pom_remove_dep bouncycastle:bcmail-jdk14 JPP-%{name}-${p}.pom
%pom_add_dep org.bouncycastle:bcmail-jdk15on JPP-%{name}-${p}.pom
%pom_remove_dep bouncycastle:bcprov-jdk14 JPP-%{name}-${p}.pom
%pom_add_dep org.bouncycastle:bcprov-jdk15on JPP-%{name}-${p}.pom
%pom_remove_dep bouncycastle:bctsp-jdk14 JPP-%{name}-${p}.pom
%pom_add_dep org.bouncycastle:bcpkix-jdk15on JPP-%{name}-${p}.pom
done

# move manifest to build area
tar -xf %{SOURCE7}
mv org.eclipse.orbit/com.lowagie.text/META-INF/MANIFEST.MF src/ant

# Remove preshipped binaries
find . -name "*.jar" -exec rm {} \;

# Fix encoding issues
sed 's/\r//' src/rups/com/lowagie/rups/view/icons/copyright_notice.txt > tmpfile
touch -r src/rups/com/lowagie/rups/view/icons/copyright_notice.txt tmpfile
mv -f tmpfile src/rups/com/lowagie/rups/view/icons/copyright_notice.txt

mkdir lib
build-jar-repository -s -p lib bcprov bcmail bcpkix pdf-renderer dom4j

# Remove jdk & version numbers from classpath entries
for file in src/ant/{*,.ant*}; do
 for jarname in bcmail bcprov dom4j; do
  sed -i "s|$jarname-.*\.jar|$jarname.jar|" $file
 done
done
for file in src/ant/{*,.ant*}; do
 sed -i "s|bctsp-.*\.jar|bcpkix.jar|" $file
done

# Setting debug="on" on javac part of the build script.
sed -i 's|destdir|debug="on" destdir|g' src/ant/compile.xml
sed -i 's|debug="true"||g' src/ant/compile.xml

# Specify encoding, otherwise javadoc blows
sed -i 's|author|Encoding="ISO-8859-1" author|' src/ant/site.xml
# and set max memory higher or we run out
sed -i 's|maxmemory="128m"|maxmemory="512m"|' src/ant/site.xml

sed -i '/Class-Path/d' src/ant/compile.xml
sed -i 's,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301,' src/core/com/lowagie/text/lgpl.txt

%build
export CLASSPATH=$(build-classpath bcprov bcmail bcpkix pdf-renderer dom4j)
pushd src
 ant -Ditext.jdk.core=1.6 \
     -Ditext.jdk.rups=1.6 \
     -Ditext.jdk.toolbox=1.6 \
     jar jar.rups jar.rtf jar.toolbox javadoc
popd

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/iText.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p lib/iText-rtf.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-rtf.jar
cp -p lib/iText-rups.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-rups.jar
cp -p lib/iText-toolbox.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-toolbox.jar


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

# toolbox stuff
desktop-file-install \
      --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
      %{SOURCE6}
%jpackage_script com.lowagie.toolbox.Toolbox "" "" %{name}:%{name}-toolbox:bcmail:bcprov:bctsp %{name}-toolbox true

# rups stuff
install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-rups
desktop-file-install \
      --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
      %{SOURCE4}

# icon for rups and toolbox
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
convert -resize 128x128 src/toolbox/com/lowagie/toolbox/1t3xt.gif %{name}.png
cp -a %{name}.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}-rups.png
cp -a %{name}.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}-toolbox.png

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install the pom
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
cp -pr JPP-itext.pom $RPM_BUILD_ROOT%{_mavenpomdir}
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "itext:itext"

cp -pr JPP-%{name}-rtf.pom $RPM_BUILD_ROOT%{_mavenpomdir}
%add_maven_depmap JPP-%{name}-rtf.pom %{name}-rtf.jar -f rtf
cp -pr JPP-%{name}-rups.pom $RPM_BUILD_ROOT%{_mavenpomdir}
%add_maven_depmap JPP-%{name}-rups.pom %{name}-rups.jar  -f rups

%files
%doc build/bin/com/lowagie/text/{apache_license,lgpl,misc_licenses,MPL-1.1}.txt

%files core -f .mfiles
%doc build/bin/com/lowagie/text/{apache_license,lgpl,misc_licenses,MPL-1.1}.txt

%files rtf -f .mfiles-rtf
%doc build/bin/com/lowagie/text/{lgpl,misc_licenses,MPL-1.1}.txt

%files rups -f .mfiles-rups
%doc src/rups/com/lowagie/rups/view/icons/copyright_notice.txt
%{_bindir}/%{name}-rups
%{_datadir}/applications/%{name}-rups.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}-rups.png

%files toolbox 
%doc build/bin/com/lowagie/text/{misc_licenses,MPL-1.1}.txt
%doc src/toolbox/com/lowagie/toolbox/tools.txt
%{_javadir}/%{name}-toolbox.jar
%{_bindir}/%{name}-toolbox
%{_datadir}/applications/%{name}-toolbox.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}-toolbox.png

%files javadoc
%{_javadocdir}/%{name}
%doc build/bin/com/lowagie/text/{apache_license,lgpl,misc_licenses,MPL-1.1}.txt

# -----------------------------------------------------------------------------

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt3_36jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_36jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_33jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_31jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_29jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_21jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_19jpp7
- new release

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_15jpp7
- fixed build

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_14jpp7
- update to new release by jppimport

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt2_12jpp7
- added obsoletes for itext2

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.1.7-alt1_12jpp7
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_5jpp6
- fixed pom

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_3jpp5
- doungrade due to old maven-doxia; anyway current is 2.1

* Sat Sep 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.8-alt1_0.2jpp1.7
- converted from JPackage by jppimport script
- resurrected from orphaned

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt0.1
- new version 1.4.8 (with rpmrb script)

* Thu Feb 16 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt0.1
- new version

* Wed Oct 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt0.1
- new version

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt0.1
- first build for ALT Linux Sisyphus

* Thu Aug 26 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.3-1jpp
- Upgrade to 1.3
- Now one jar only

* Wed Aug 25 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.02b-2jpp
- Build with ant-1.6.2
- Relax some versioned dependencies

* Fri Feb 27 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.02b-1jpp
- First JPackage release
