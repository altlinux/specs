Name: aardtools
Version: 0.8.3
Release: alt1.git.72.ga609acb
Summary: Tools to create dictionaries in aarddict format

Packager: Ildar Mulyukov <ildar@altlinux.ru>

BuildArch: noarch
Source: %name.tar
Group: Development/Other
Url: http://aarddict.org
License: GPL3

# Automatically added by buildreq on Mon Apr 01 2013
BuildRequires: python-module-distribute python-module-icu python-module-mwlib

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

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir --record=INSTALLED_FILES

%files
%_bindir/aard*
%python_sitelibdir/%name
%python_sitelibdir/%{name}*egg-info
%doc doc/*

%changelog
* Mon Apr 01 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.8.3-alt1.git.72.ga609acb
- initial build for ALT Linux Sisyphus
