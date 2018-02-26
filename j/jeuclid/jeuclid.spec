Name: jeuclid
Version: 3.1.6
Release: alt1
Summary: MathML rendering solution
Group: Development/Java
License: ASL 2.0 and SPL
Url: http://jeuclid.sourceforge.net/index.html
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://downloads.sourceforge.net/%name/%name-parent-%version-src.zip
#fedora specific build script based on debian
Source1: build.xml
Source2: jeuclid-mathviewer.desktop
Source3: jeuclid-mathviewer.sh
Source4: jeuclid-cli.sh

#Allows for compiling code that uses Apple EAWT without the lib
Patch1: AppleJavaExtensions.patch
#removes OSX dep for the viewer
Patch2: MacOSX.patch

BuildArch: noarch
BuildRequires(pre): unzip rpm-build-java desktop-file-utils

# Automatically added by buildreq on Thu Sep 10 2009
BuildRequires: ant jakarta-commons-cli jakarta-commons-lang jcip-annotations tzdata unzip xmlgraphics-fop

%description
Core module containing basic JEuclid rendering and document handling classes.

%package mathviewer
Summary: Viewer for MathML files
Group: Publishing
Requires: %name = %version-%release

%description mathviewer
The %name-mathviewer package contains the Swing MathViewer application.

%package fop
Summary: JEuclid plug-in for FOP
Group: Publishing
Requires: %name = %version-%release
Requires: xmlgraphics-fop

%description fop
The %name-fop package is a jeuclid plug-in for FOP.

%package cli
Summary: Command line interface for Jeuclid
Group: Publishing
Requires: %name = %version-%release
Requires: jakarta-commons-cli
Requires: jakarta-commons-lang
Requires: jakarta-commons-io

%description cli
The %name-cli package provides a command line interface for jeuclid

%prep
%setup -q -n %name-parent-%version
cp %SOURCE1 %_builddir/%name-parent-%version/
#fix line endings
sed 's/\r//' NOTICE > NOTICE.unix
touch -r NOTICE NOTICE.unix;
mv NOTICE.unix NOTICE

mkdir lib
build-jar-repository -s -p lib jcip-annotations commons-logging xmlgraphics-commons batik-all fop commons-cli commons-lang

%patch1 -p1
%patch2 -p1

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

#removes the FreeHep support from the build per the build README
rm -f %name-core/src/main/java/net/sourceforge/jeuclid/converter/FreeHep*;

%build
ant compile-core compile-mathviewer compile-cli compile-fop -verbose

%install
mkdir -p %buildroot%_javadir
cp -p target/%name-core.jar \
%buildroot%_javadir/%name-core-%version.jar
cp -p target/%name-fop.jar \
%buildroot%_javadir/%name-fop-%version.jar
cp -p target/%name-mathviewer.jar \
%buildroot%_javadir/%name-mathviewer-%version.jar
cp -p target/%name-cli.jar \
%buildroot%_javadir/%name-cli-%version.jar

(cd %buildroot%_javadir && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%version||g"`; done)

install -dm 755 %buildroot%_bindir
install -pm 755 %SOURCE3 %buildroot%_bindir/jeuclid-mathviewer
install -pm 755 %SOURCE4 %buildroot%_bindir/jeuclid-cli

mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps/
cp -p src/icons/jeuclid_48x48.png %buildroot%_iconsdir/hicolor/48x48/apps/

mkdir -p %buildroot%_desktopdir
desktop-file-install --dir=%buildroot%_desktopdir \
%SOURCE2

%files
%doc NOTICE LICENSE.txt README.Release
%_javadir/%name-core-%version.jar
%_javadir/%name-core.jar

%files mathviewer
%_javadir/%name-mathviewer-%version.jar
%_javadir/%name-mathviewer.jar
%_bindir/jeuclid-mathviewer
%_iconsdir/hicolor/48x48/apps/jeuclid_48x48.png
%_desktopdir/jeuclid-mathviewer.desktop

%files fop
%_javadir/%name-fop-%version.jar
%_javadir/%name-fop.jar

%files cli
%_javadir/%name-cli-%version.jar
%_javadir/%name-cli.jar
%_bindir/jeuclid-cli

%changelog
* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.6-alt1
- 3.1.6

* Thu Sep 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.3-alt2
- Fix BuildRequires (ALT #21515)

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.3-alt1
- Intial from Fedora

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-9
- Re-imported SRPM, cvs failed to bring in jecuclid-cli.sh

* Tue Dec 9 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-9
- Added missing hicolor-icon-theme build require
- Fixed timestamp issue
- Added GTK icon scriplets

* Fri Nov 27 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-8
- Added cli package
- Fixed build script so subpackages dont all package into one jar
- Added desktop file and java wrapper scripts

* Thu Nov 26 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-7
- Fixed BuildRequires
- Fixed Requires
- Added mathviewer and fop
- mathviewer patch includes SPL code. SPL added to license field
- New build file to manage core mathviewer and fop

* Wed Nov 26 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-6
- Fixed package name
- Added system links to jar files

* Wed Nov 26 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-5
- Fixed trailing white space
- Fixed patch comments
- Fixed search for jar file

* Wed Nov 26 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-4
- Fixed source URL
- Added verbose to ant

* Wed Nov 26 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-3
- Fixed end-of-line-encoding in NOTICE

* Tue Nov 25 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-2
- Added comments to patches
- Removed java-devel from BuildRequires for java-1.6.0-openjdk-devel
- Made arch noarch

* Mon Nov 24 2008 Brennan Ashton <bashton at, brennanashton.com> 3.1.3-1
- Created spec file
