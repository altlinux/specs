# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Epoch:          2

Name:		jeuclid
Version:	3.1.9
Release:	alt2_2jpp6
Summary:	MathML rendering solution
Group:		Development/Java
License:	ASL 2.0 and SPL
URL:		http://jeuclid.sourceforge.net/index.html
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-parent-%{version}-src.tar.gz
#fedora specific build script based on debian
Source1:	build.xml
Source2:	jeuclid-mathviewer.desktop
Source3:	jeuclid-mathviewer.sh
Source4:	jeuclid-cli.sh

#removes FreeHep support as per the build README, optional feature (not upstream)
Patch0:		jeuclid-core-FreeHep.patch
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
BuildRequires:	batik >= 1.10
BuildRequires:	apache-commons-logging
BuildRequires:	jcip-annotations
BuildRequires:	xml-commons-apis
BuildRequires:	xmlgraphics-commons >= 1.3
#BuildRequires:	fop > 2.5
BuildRequires:	apache-commons-cli >= 1.1
BuildRequires:	apache-commons-lang
BuildRequires:	desktop-file-utils

Requires:	javapackages-tools
Requires:	java >= 1.6.0
Requires:	apache-commons-logging
Requires:	batik >= 1.10
Requires:	xmlgraphics-commons >= 1.3
Requires:	jcip-annotations
Source44: import.info
Source45: fop.jar

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
Requires:	fop > 2.5

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
build-jar-repository -s -p lib jcip-annotations commons-logging xmlgraphics-commons batik-all commons-cli commons-lang xml-commons-apis xalan-j2
cp -a %{SOURCE45} lib/fop.jar

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
mkdir -p %{buildroot}%{_javadir}
cp -p target/%{name}-core.jar \
%{buildroot}%{_javadir}/%{name}-core.jar
cp -p target/%{name}-fop.jar \
%{buildroot}%{_javadir}/%{name}-fop.jar
cp -p target/%{name}-mathviewer.jar \
%{buildroot}%{_javadir}/%{name}-mathviewer.jar
cp -p target/%{name}-cli.jar \
%{buildroot}%{_javadir}/%{name}-cli.jar

install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE3} %{buildroot}%{_bindir}/jeuclid-mathviewer
install -pm 755 %{SOURCE4} %{buildroot}%{_bindir}/jeuclid-cli

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
cp -p src/icons/jeuclid_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
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
* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 2:3.1.9-alt2_2jpp6
- build with fop 2.6

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 2:3.1.9-alt1_2jpp6
- use jvm_run
- set source/target 1.6

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2:3.1.9-alt1_2
- fixed build

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
