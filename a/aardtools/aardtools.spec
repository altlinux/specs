Name: aardtools
Version: 0.9.0
Release: alt1.git.4.g831482e
Summary: Tools to create dictionaries in aarddict format

Packager: Ildar Mulyukov <ildar@altlinux.ru>

BuildArch: noarch
Group: Development/Other
Url: http://aarddict.org
License: GPL3

Source: %name.tar
Patch1: %name-alt-disable-mw.patch

# Automatically added by buildreq on Mon Apr 01 2013
BuildRequires: python-module-distribute python-module-icu python-module-mwlib

#Requires: python-module-mwlib >= 0.14.1

%description
`Aard Tools` "out of the box" comes with support for the following input types:

xdxf
    Dictionaries in XDXF_ format (only `XDXF-visual`_ is supported).

wiki
    Wikipedia articles and templates :abbr:`CDB (Constant Database)`
    built with :command:`mw-buildcdb` from Wikipedia XML dump.

aard
    Dictionaries in aar format. This is useful for updating dictionary metadata
    and changing the way it is split into volumes. Multiple input files can
    be combined into one single or multi volume dictionary.

wordnet
   WordNet_

%prep
%setup -n %name
%patch1 -p1

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir --record=INSTALLED_FILES
subst '/^mwlib/d' %buildroot%python_sitelibdir/%{name}*egg-info/requires.txt

%files
%_bindir/aard*
%python_sitelibdir/%{name}*
%doc doc/*

%changelog
* Sun Dec 07 2014 Ildar Mulyukov <ildar@altlinux.ru> 0.9.0-alt1.git.4.g831482e
- new version

* Sun Apr 07 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.8.3-alt3.git.73.g5d4b4c4
- new snapshot

* Tue Apr 02 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.8.3-alt2.git.72.ga609acb
- add %name-alt-disable-mw.patch to disable mwlib part due to bug #28776

* Mon Apr 01 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.8.3-alt1.git.72.ga609acb
- initial build for ALT Linux Sisyphus
