# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Epoch:          2

Name:		jeuclid
Version:	3.1.9
Release:	alt1_0
Summary:	MathML rendering solution
Group:		Development/Java
License:	ASL 2.0 and SPL
URL:		http://jeuclid.sourceforge.net/index.html
#Source0:	http://downloads.sourceforge.net/%{name}/%{name}-parent-%{version}-src.zip
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-parent-%{version}-src.tar.gz
#fedora specific build script based on debian
Source1:	build.xml
Source2:	jeuclid-mathviewer.desktop
Source3:	jeuclid-mathviewer.sh
Source4:	jeuclid-cli.sh

#removes FreeHep support as per the build README, optional feature (not upstream)
#Patch0:		jeuclid-core-FreeHep.patch
#Allows for compiling code that uses Apple EAWT without the lib
Patch1:		AppleJavaExtensions.patch
#removes OSX dep for the viewer
Patch2:		MacOSX.patch
Patch3:		jeuclid-cli-name.diff
Patch4:		cast-issue.diff
Patch5:		batik-compatibility.patch

BuildArch:	noarch

BuildRequires:	javapackages-tools
BuildRequires:	java-devel-default /proc
BuildRequires:	ant
BuildRequires:	batik >= 1.7 
BuildRequires:	apache-commons-logging
BuildRequires:	jcip-annotations
BuildRequires:	xmlgraphics-commons >= 1.3
BuildRequires:	fop >= 0.95
BuildRequires:	apache-commons-cli >= 1.1
BuildRequires:	apache-commons-lang
BuildRequires:	desktop-file-utils

Requires:	javapackages-tools
Requires:	java >= 1.6.0
Requires:	apache-commons-logging
Requires:	batik >= 1.7
Requires:	xmlgraphics-commons >= 1.3	
Requires:	jcip-annotations
Source44: import.info

%description
Core module containing basic JEuclid rendering and document handling classes.

%package	mathviewer
Summary:	Viewer for MathML files
Group:		Development/Java
Requires:	%{name} = %epoch:%{version}-%{release}
Requires:	icon-theme-hicolor

%description	mathviewer
The %{name}-mathviewer package contains the Swing MathViewer application.

%package	fop
Summary:	JEuclid plug-in for FOP
Group:	 	Development/Java
Requires:	%{name} = %epoch:%{version}-%{release}
Requires:	fop >= 0.95

%description	fop
The %{name}-fop package is a jeuclid plug-in for FOP.

%package	cli
Summary:	Command line interface for Jeuclid
Group:		Development/Java
Requires:	%{name} = %epoch:%{version}-%{release}
Requires:	apache-commons-cli >= 1.1
Requires:	apache-commons-lang
Requires:	apache-commons-io

%description	cli
The %{name}-cli package provides a command line interface for jeuclid

%prep
%setup -q -n %{name}-parent-%{version}
cp %{SOURCE1} %{_builddir}/%{name}-parent-%{version}/ 
#fix line endings
sed 's/\r//' NOTICE > NOTICE.unix
touch -r NOTICE NOTICE.unix;
mv NOTICE.unix NOTICE

mkdir lib
build-jar-repository -s -p lib jcip-annotations commons-logging xmlgraphics-commons batik-all fop commons-cli commons-lang xml-commons-apis xalan-j2

#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

#removes the FreeHep support from the build per the build README
rm -f %{name}-core/src/main/java/net/sourceforge/jeuclid/converter/FreeHep*;

%build
ant compile-core compile-mathviewer compile-cli compile-fop -verbose 

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-core.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar
cp -p target/%{name}-fop.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-fop.jar
cp -p target/%{name}-mathviewer.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-mathviewer.jar
cp -p target/%{name}-cli.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-cli.jar

install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/jeuclid-mathviewer
install -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/jeuclid-cli

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
cp -p src/icons/jeuclid_48x48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
desktop-file-install --dir=$RPM_BUILD_ROOT/%{_datadir}/applications \
%{SOURCE2}

%files
%doc NOTICE LICENSE.txt README.Release
%{_javadir}/%{name}-core.jar

%files mathviewer
%{_javadir}/%{name}-mathviewer.jar
%{_bindir}/jeuclid-mathviewer
%{_datadir}/icons/hicolor/48x48/apps/jeuclid_48x48.png
%{_datadir}/applications/jeuclid-mathviewer.desktop

%files fop
%{_javadir}/%{name}-fop.jar

%files cli 
%{_javadir}/%{name}-cli.jar
%{_bindir}/jeuclid-cli




%changelog
* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 2:3.1.9-alt1_0
- new version 3.1.9
- fixed build (closes: #35932)
- merged debian patches

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2:3.1.3-alt1_22
- NMU: fixed build, downgraded version to 3.1.3

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
