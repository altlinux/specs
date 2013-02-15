# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		OmegaT
%define namer	omegat
Summary:	Computer Aid Translation tool
Version:	2.3.0_06
#%define versionr	2.2.3_04_Beta
%define versionr	%{version}
Release:	alt1_6jpp7
#Release:	0.2.04_Beta%{?dist}
Source0:	http://downloads.sourceforge.net/omegat/%{name}_%{versionr}_Source.zip
Source2:	OmegaT-lib-mnemonics-build.xml
Source3:	OmegaT-build.xml
Source4:	OmegaT.sh
Url:		http://www.omegat.org/
Group:		Text tools

BuildRequires:	ant jpackage-utils
BuildRequires:	desktop-file-utils dos2unix
BuildRequires:	htmlparser vldocking >= 2.1.4
BuildRequires:	jna
BuildRequires:	ws-jaxme
BuildRequires:	swing-layout
BuildRequires:	hunspell <= 1.4.0

Requires:	jpackage-utils
Requires:	vldocking >= 2.1.4
Requires:	htmlparser
Requires:	hunspell <= 1.4.0
Requires:	jna
Requires:	swing-layout
Requires:	ws-jaxme

License:	GPLv2+
# http://svn.debian.org/wsvn/pkg-java/trunk04-get-rid-of-MRJAdapter.patch
Patch1:		OmegaT-04-get-rid-of-MRJAdapter.patch
Patch2:		OmegaT-help-path.patch
# http://svn.debian.org/wsvn/pkg-java/trunk/omegat/debian/patches/05-remove-jmyspell-alternative.patch
Patch3:		OmegaT-05-remove-jmyspell-alternative.patch
# based on http://svn.debian.org/wsvn/pkg-java/trunk/omegat/debian/patches/06-use-external-hunspell.patch
Patch4:		OmegaT-06-use-external-hunspell.patch
Patch5:		OmegaT-07-use-openjdk-swingworker.patch
Source44: import.info

%description
OmegaT is a free translation memory application written in Java.
It is a tool intended for professional translators. It does not
translate for you!

OmegaT has the following features:

 * Fuzzy matching
 * Match propagation
 * Simultaneous processing of multiple-file projects
 * Simultaneous use of multiple translation memories
 * External glossaries
 * Document file formats:
	XHTML and HTML
	Microsoft Office 2007 XML
	OpenOffice.org/StarOffice
	XLIFF (Okapi)
	MediaWiki (Wikipedia)
	Plain text
 * Unicode (UTF-8) support: can be used with non-Latin alphabets
 * Support for right-to-left languages
 * Compatible with other translation memory applications (TMX)

%prep
%setup -q -c -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%ifarch x86_64 # get rids the hardlink to hunspell 
sed -i -e "s|/usr/lib/libhunspell|/usr/lib64/libhunspell|g" src/org/omegat/util/OConsts.java
%endif

%patch5 -p1

# not needed outside Netbeans
rm nbproject/org-netbeans-modules-java-j2seproject-copylibstask.jar

# clean dependencies:
rm lib/vldocking_2.1.4.jar
rm lib/htmlparser.jar
rm lib/sources/htmlparser1_6_20060610.zip-source.zip
rm lib/jmyspell-core-1.0.0-beta-2.jar
rm lib/jna.jar
rm -r native/*
rm lib/swing-layout-1.0.jar

###  JAXB dependencies
rm lib/activation.jar
rm lib/jaxb-api.jar
rm lib/jaxb-impl.jar
rm lib/jsr173_1.0_api.jar 
rm lib/sources/JAXB/jsr173_1.0_src.jar

# not needed outside MacOSX:
rm lib/MRJAdapter.jar
rm lib/sources/MRJAdapter-source.zip

# not needed outside windows
rm -rf release/win32-specific/

# seems they are not really needed... 
rm -rf ./test/lib/junit-4.4.jar
rm -rf ./test/lib/xmlunit-1.1.jar

## gen/lib/jaxb-xjc.jar
rm -rf gen/lib/jaxb-xjc.jar

rm -rf lib/swing-worker-1.2.jar

%build

# cleaning:
sed -i '/class-path/I d' manifest-template.mf

pushd lib-mnemonics
cp %{SOURCE2} build.xml
ant dist
popd

cp %{SOURCE3} build.xml
ant dist

%install 
#make some install dirs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{namer}/docs
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{namer}/images

install -pm  0755 dist/OmegaT.jar $RPM_BUILD_ROOT%{_javadir}/OmegaT-%{version}.jar
install -pm  0755 lib-mnemonics/dist/lib-mnemonics.jar $RPM_BUILD_ROOT%{_javadir}/OmegaT-lib-mnemonics-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
	ln -s OmegaT-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/OmegaT.jar
	ln -s OmegaT-lib-mnemonics-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/lib-mnemonics.jar
popd

cp -pR release/index.html docs/ images/ $RPM_BUILD_ROOT%{_datadir}/%{namer}/

#create our launch wrapper script
install -pm  0755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{namer}

#make our launch wrapper executable
chmod +x $RPM_BUILD_ROOT%{_bindir}/*

#Menu entry
install -d -m755 %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/fedora-%{namer}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Exec=%{namer}
Icon=/usr/share/omegat/images/OmegaT.png
Comment=Computer Aid Translation tool
Comment[es]=Herramienta de asistencia a la traducción
Terminal=false
Type=Application
Categories=Translation;Java;Office;
X-AppInstall-Package=%{namer}
EOF

desktop-file-install  --vendor "fedora" --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/applications/fedora-%{namer}.desktop 

# fixing end of line making rpmlint happy
dos2unix -k -f release/*.txt
# hack to mark a package as an arch
mkdir -p %{buildroot}%{_jnidir}/
ln -s %_javadir/OmegaT.jar %{buildroot}%{_jnidir}/OmegaT.jar

%files
%dir %{_datadir}/%{namer}
%{_datadir}/%{namer}/*
%{_bindir}/*
%{_javadir}/*
%{_datadir}/applications/fedora-%{namer}.desktop

%doc ./release/changes.txt release/doc-license.txt release/license.txt release/readme*.txt release/join.html
%_jnidir/*


%changelog
* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0_06-alt1_6jpp7
- fixed maven1 dependency

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0_03-alt1_3jpp7
- new version

