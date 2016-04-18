# ########################################################
# non latin symbols shouldn't be in first 256 byte block #
# ########################################################

%define dict_name		tt-ru
%define dict_file		tt_RU-ru_RU
%define dict_eng_name		Tatarian-Russian
%define dict_rus_name		татарско-русский


Name: stardict-%dict_name
Version: 1.0
Release: alt1.qa1

Summary: Dictionary: %dict_eng_name
Summary(ru_RU.KOI8-R): Словарь: %dict_rus_name
License: GPL
Group: Text tools
Requires: stardict >= 2.4.2
BuildArchitectures: noarch

Source: stardict-tt-ru.tar.gz

# Automatically added by buildreq on Mon Apr 18 2016
# optimized out: python-base python-modules
BuildRequires: dict-tools

%description
Dictionary: %dict_eng_name

%description -l ru_RU.KOI8-R
Словарь %dict_rus_name

%prep
%setup -q -c

%build
gzip %name/%dict_name.idx
dictzip %name/%dict_name.dict

%install

install -p -m644 -D %name/%dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.dict.dz
install -p -m644 -D %name/%dict_name.idx.gz $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.idx.gz
install -p -m644 -D %name/%dict_name.ifo $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.ifo
# install -p -m644 -D %name/%dict_name.idx.oft $RPM_BUILD_ROOT%_datadir/stardict/dic/%dict_name.idx.oft

%files
%_datadir/stardict/dic/*

%changelog
* Mon Apr 18 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0-alt1.qa1
- Removed libaudio fron BR.
- Updated BR with buildreq.

* Wed Jun 18 2008 Alexandra Panyukova <mex3@altlinux.ru> 1.0-alt1
- build for Sisyphus

* Wed Jun 18 2008 Alexandra Panyukova <mex3@altlinux.ru> 1.0-alt0
- build for ALTLinux
