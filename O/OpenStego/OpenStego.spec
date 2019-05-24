Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global         gituser         syvaidya
%global         gitname         openstego
# Release 0.7.3 - 2018-04-15
%global         commit          df7e186646f3cde69ead1a8be3de3290489aa2e4
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           OpenStego
Version:        0.7.3
Release:        alt1_3jpp8
Summary:        Free Steganography solution
Summary(fr):    Solution libre pour la steganographie

License:        GPLv2
#               https://github.com/syvaidya/openstego/releases 
URL:            http://openstego.sourceforge.net/index.html
# Source0:      http://downloads.sourceforge.net/project/openstego/openstego/openstego-%{version}/openstego-src-%{version}.zip
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{gitname}-%{version}.tar.gz
Source1:        openstego.desktop
# Patch the ant build script to build only the binary package out of java sources
Patch0:         %{name}-antbuild.patch

BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  desktop-file-utils
Requires:       jpackage-utils
Source44: import.info


%description
OpenStego is a tool implemented in Java for generic steganography,
with support for password-based encryption of the data. It supports
plugins for various steganographic algorithms.

%description -l fr
OpenStego est un outil implanté en Java pour la steganographie générique,
avec le support de l'encryption des données basé sur mot de passe. Il
supporte les plugins pour des algorithmes steganographiques variés.


%package javadoc
Group: Development/Java
BuildArch: noarch
Requires:  jpackage-utils
Summary:   Javadoc generated documentation for Openstego
Summary(fr):    Documentation javadoc générée pour Openstego

%description javadoc
Javadoc generated documentation for Openstego.

%description javadoc -l fr
Documentation javadoc générée pour Openstego


%prep
%setup -q -n %{gitname}-%{gitname}-%{version}
%patch0 -p 1 -b .antbuild
find . -name *.class -delete
find . -name *.jar -delete
# Delete file for Windows :
rm -f openstego.bat


%build
ant package doc


%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_javadocdir}/openstego
cp -p ./lib/openstego.jar %{buildroot}%{_javadir}/openstego.jar
cp -p ./src/image/ImagesVectorSource.svg %{buildroot}%{_datadir}/pixmaps/openstego.svg
cp -pr ./doc/api/* %{buildroot}%{_javadocdir}/openstego
%jpackage_script com.openstego.desktop.OpenStego "" "" openstego.jar openstego true
# Install openstego.desktop :
desktop-file-install                       \
--dir=%{buildroot}%{_datadir}/applications \
%{SOURCE1}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf


%files
%doc README LICENSE
%{_bindir}/openstego
%{_javadir}/openstego.jar
%{_datadir}/pixmaps/openstego.svg
%{_datadir}/applications/openstego.desktop
%config(noreplace,missingok) /etc/java/%name.conf

%files javadoc
%doc LICENSE
%{_javadocdir}/openstego/


%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_3jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1_1jpp8
- java update

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_11jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_10jpp7
- new fc release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2_9jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_9jpp7
- new version

