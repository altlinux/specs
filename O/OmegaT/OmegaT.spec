%filter_from_requires /^.usr.bin.run/d
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# TODO:
# - add subpackages for:
#       - OmegaT-LanguageTool-src_0.4-2.3.zip
#       - OmegaT-Scripting-src_0.5-2.5.0_03.zip
#       - OmegaT-tokenizers-src_0.4_2-2.1.zip
# - fix desktop-install warning
# - new logo
# - update l10n.es

# fixing #901660
%global debug_package  %{nil}

Name:           OmegaT
%global namer   omegat
Summary:        Computer Aid Translation tool
Version:        2.6.1
%global versionr 2.6.1_01_Beta
#Release:       1%{?dist}
Release:        alt1_0.9.Betajpp7
Source0:        http://downloads.sourceforge.net/omegat/%{name}_%{versionr}_Source.zip
Source2:        OmegaT-lib-mnemonics-build.xml
Source3:        OmegaT-build.xml
Url:            http://www.omegat.org/
Group:          Text tools

BuildRequires:  ant jpackage-utils
BuildRequires:  desktop-file-utils dos2unix
BuildRequires:  htmlparser vldocking >= 2.1.4
BuildRequires:  jna
BuildRequires:  ws-jaxme
BuildRequires:  swing-layout
BuildRequires:  hunspell <= 1.4.0

BuildRequires:  svnkit >= 1.7.5
BuildRequires:  jsch
BuildRequires:  sqljet >= 1.1.4
# OmegaT brings org.eclipse.jgit-1.2.0.201112221803-r.jar but Fedora is 1.1.0
BuildRequires:  jgit
BuildRequires:  antlr3-tool

Requires:       jpackage-utils
Requires:       vldocking >= 2.1.4
Requires:       htmlparser
Requires:       hunspell <= 1.4.0
Requires:       jna
Requires:       swing-layout
Requires:       ws-jaxme
Requires:       svnkit
Requires:       jsch
Requires:       sqljet
Requires:       jgit
Requires:       antlr3-java

License:        GPLv2+
# http://svn.debian.org/wsvn/pkg-java/trunk04-get-rid-of-MRJAdapter.patch
Patch1:         OmegaT-04-get-rid-of-MRJAdapter.patch
Patch2:         OmegaT-help-path.patch
# http://svn.debian.org/wsvn/pkg-java/trunk/omegat/debian/patches/05-remove-jmyspell-alternative.patch
Patch3:         OmegaT-05-remove-jmyspell-alternative.patch
Patch4:         OmegaT-06-use-system-hunspell.patch

# reported at http://sourceforge.net/mailarchive/forum.php?thread_name=CAARR2rZ2uT1KOrLLVF9wdS6Ybq_sU_o1u08U54BLzxqxZoyRUQ%40mail.gmail.com&forum_name=omegat-development
Patch5:         OmegaT-07-use-openjdk-swingworker.patch
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
%ifarch x86_64  # get rids the hardlink to hunspell 
sed -i -e "s|/usr/lib/libhunspell|/usr/lib64/libhunspell|g" src/org/omegat/util/OConsts.java
%endif

%patch5 -p1

# not needed outside Netbeans
rm nbproject/org-netbeans-modules-java-j2seproject-copylibstask.jar

# clean dependencies:
rm lib/svnkit-1.7.5.jar
rm lib/jsch-0.1.46.jar
rm lib/sqljet-1.1.3.jar
rm lib/org.eclipse.jgit-1.2.0.201112221803-r.jar
rm lib/antlr-runtime-3.4.jar

# is not really used??
rm lib/sjsxp-1.0.2.jar

# seems to be included in svnkit:
rm lib/sequence-library-1.0.2.jar 

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

# using the internal openjdk one:
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
rm -Rf %{buildroot}

#install our jar file
#make some install dirs
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/%{namer}/docs
mkdir -p %{buildroot}%{_datadir}/%{namer}/images

install -pm  0755 dist/OmegaT.jar %{buildroot}%{_javadir}/OmegaT-%{version}.jar
install -pm  0755 lib-mnemonics/dist/lib-mnemonics.jar %{buildroot}%{_javadir}/OmegaT-lib-mnemonics-%{version}.jar

pushd %{buildroot}%{_javadir}
        ln -s OmegaT-%{version}.jar %{buildroot}%{_javadir}/OmegaT.jar
        ln -s OmegaT-lib-mnemonics-%{version}.jar %{buildroot}%{_javadir}/lib-mnemonics.jar
popd

cp -pR release/index.html docs/ images/ %{buildroot}%{_datadir}/%{namer}/

%jpackage_script org.omegat.Main "" "" OmegaT:svnkit:jsch:sqljet:antlr3-runtime:jgit/jgit:htmlparser:vldocking:jna:lib-mnemonics:jaxme/jaxme2:jaxme/jaxme2-rt:jaxme/jaxmejs:jaxme/jaxmepm:jaxme/jaxmexs:swing-layout %{namer} true


#Menu entry
install -d -m755 %{buildroot}%{_datadir}/applications

cat > %{buildroot}%{_datadir}/applications/%{namer}.desktop <<EOF
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

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/applications/%{namer}.desktop

# fixing end of line making rpmlint happy
dos2unix -k -f release/*.txt
# hack to mark a package as an arch
mkdir -p %{buildroot}%{_jnidir}/
ln -s %_javadir/OmegaT.jar %{buildroot}%{_jnidir}/OmegaT.jar

mkdir -p %buildroot%_sysconfdir/java/
touch %buildroot%_sysconfdir/java/%{name}.conf

%files
%dir %{_datadir}/%{namer}
%{_datadir}/%{namer}/*
%{_bindir}/*
%{_javadir}/*
%{_datadir}/applications/*%{namer}.desktop

%doc ./release/changes.txt release/doc-license.txt release/license.txt release/readme*.txt release/join.html
%_jnidir/*
%_sysconfdir/java/%{name}.conf

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_0.9.Betajpp7
- new version

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0_06-alt1_6jpp7
- fixed maven1 dependency

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0_03-alt1_3jpp7
- new version

