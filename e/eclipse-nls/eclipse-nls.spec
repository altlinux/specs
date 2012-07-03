BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# required for prep
BuildRequires: unzip
%define eclipse_data %{_datadir}/eclipse
# Disable repacking of jars, since it takes forever for all the little jars, 
# and we don't need multilib anyway:
%define __jar_repack %{nil}

%define debug_package %{nil}

Name: eclipse-nls 
Summary: Babel language packs for the Eclipse platform and various plug-ins
# note: try to keep this group the same as eclipse's rpm:
Group: Editors
License: EPL
URL: http://www.eclipse.org/babel/

Version: 3.6.0.v20100814043401
Release: alt1_5jpp6
## The source for this package is taken from
# http://download.eclipse.org/technology/babel/babel_language_packs/R0.8.0/helios.php
# usage: FROM=http://download.eclipse.org/technology/babel/babel_language_packs/R0.8.0/helios.php ./fetch-babel.sh
Source0: BabelLanguagePack-%{version}.tar.bz2

BuildArch:  noarch
Requires:   eclipse-platform >= 3.6
Source44: import.info

# It tekes too long for osgi to complete :(
%add_findreq_skiplist /usr/share/*
%add_findprov_skiplist /usr/share/*

%description
Babel language packs include translations for the Eclipse platform and other 
Eclipse-related packages.

%files
%dir %{eclipse_data}/dropins/babel
%dir %{eclipse_data}/dropins/babel/eclipse
#% {eclipse_data}/dropins/babel/eclipse/artifacts.jar
#% {eclipse_data}/dropins/babel/eclipse/content.jar
#% dir %{eclipse_data}/dropins/babel/eclipse/features
%dir %{eclipse_data}/dropins/babel/eclipse/plugins


# %1 subpackage id (ie Linux locale id)
# %2 Java locale id (mostly the same as Linux)
# %3 language name
%define lang_meta_pkg() \
%package %1 \
Summary:    Eclipse/Babel language pack for %3 \
Group:      System/Internationalization \
Provides: eclipse-i18n-%1 \
Requires:   eclipse-nls = %{version}-%{release} \
Obsoletes:  eclipse-sdk-nls-%1 < 3.2.1-4 \
Provides:   eclipse-sdk-nls-%1 = %{version}-%{release} \
\
%description %1 \
This language pack for %3 \
contains user-contributed translations of the \
strings in all Eclipse projects. Please see the http://babel.eclipse.org/ \
Babel project web pages for a full how-to-use explanation of these \
translations as well as how you can contribute to \
the translations of this and future versions of Eclipse. \
Note that English text will be displayed if Babel doesn't \
have a translation for a given string. \
\
%files %1 \
%defattr(-,root,root,-) \
#% {eclipse_data}/dropins/babel/eclipse/features/org.eclipse.babel.nls_*_%{2}_%{version} \
%doc eclipse/features/*_%{2}_%{version} \
%{eclipse_data}/dropins/babel/eclipse/plugins/*.nl_%{2}_%{version}.jar

%define spc() %(echo -n ' ')

%lang_meta_pkg ar ar Arabic
%lang_meta_pkg bg bg Bulgarian
%lang_meta_pkg ca ca Catalan
%lang_meta_pkg zh zh Chinese%{spc}(Simplified)
%lang_meta_pkg zh_TW zh_TW Chinese%{spc}(Traditional)
%lang_meta_pkg cs cs Czech
%lang_meta_pkg da da Danish
%lang_meta_pkg nl nl Dutch
%lang_meta_pkg en_AU en_AU English%{spc}(Australian)
%lang_meta_pkg et et Estonian
%lang_meta_pkg fa fa Farsi
%lang_meta_pkg fi fi Finnish
%lang_meta_pkg fr fr French
%lang_meta_pkg de de German
%lang_meta_pkg el el Greek
# NB 'he' is 'iw' as far as Java is concerned.
# similarly, yi -> ji, id -> in
%lang_meta_pkg he iw Hebrew
%lang_meta_pkg hi hi Hindi
%lang_meta_pkg hu hu Hungarian
%lang_meta_pkg id id Indonesian
%lang_meta_pkg it it Italian
%lang_meta_pkg ja ja Japanese
# tl should be Tagalog.  Klingon has < 1% coverage at present in Babel.  Tagalog is unsupported.
#% lang_meta_pkg tlh tl Klingon
%lang_meta_pkg ko ko Korean
%lang_meta_pkg mn mn Mongolian
%lang_meta_pkg no no Norwegian
%lang_meta_pkg pl pl Polish
%lang_meta_pkg pt pt Portuguese
%lang_meta_pkg pt_BR pt_BR Portuguese%{spc}(Brazilian)
%lang_meta_pkg ro ro Romanian
%lang_meta_pkg ru ru Russian
%lang_meta_pkg es es Spanish
%lang_meta_pkg sv sv Swedish
%lang_meta_pkg tr tr Turkish
%lang_meta_pkg uk uk Ukrainian
%lang_meta_pkg en_AA en_AA Pseudo%{spc}Translations

%prep
# extract langpack zips from tarball
%setup -q -n %{name}
#mkdir -p eclipse/features
mkdir -p eclipse/plugins
# remove unsupported langpacks (currently Klingon)
unsupported="tl"
for locale in $unsupported; do
   rm -f Babel*-${locale}_%{version}.zip
done
# extract remaining zips - to eclipse/{features,plugins}
for f in Babel*.zip; do
   unzip -qq $f
   rm $f
done
#mv artifacts.jar content.jar eclipse
# also ignore site.xml for now

%build
# nothing to build

%install

mkdir -p $RPM_BUILD_ROOT%{eclipse_data}/dropins/babel/eclipse/
mv eclipse/plugins $RPM_BUILD_ROOT%{eclipse_data}/dropins/babel/eclipse
find eclipse/features -type f -exec chmod 644 {} \;

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 3.6.0.v20100814043401-alt1_5jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 3.6.0.v20100814043401-alt1_2jpp6
- new version

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.5.0.v20090620043401-alt1_2jpp6
- converted from JPackage by jppimport script

* Wed Jan 14 2009 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_0.5.20080807snapjpp6
- added eclipse-i18n-* provides.

* Sat Jan 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_0.5.20080807snapjpp6
- new version

