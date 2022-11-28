%define cid            langpack-el@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       el@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	31.3.0
%define max_version	31.4.*

%define bname		newmoon
%define newmoon_dir 	%palemoon_datadir/browser/

Name: palemoon-el


Version: 31.4.0
Release: alt1

Summary: Greek (EL) Language Pack for Pale Moon
License: MPL-2.0

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: el_palemoon_%version.xpi
Source2: el_GR_%version.tar

ExcludeArch: %ix86 %arm

Requires: hunspell-el
Requires: palemoon >= 27.7.0


BuildRequires(pre):	rpm-build-palemoon

# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: unzip


%description
The Palemoon Greek translation and dictionary

%prep
%setup -c -n %name-%version/%cid

cd ..
tar -xf  %SOURCE2

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

install -d -m 755 %buildroot/%newmoon_dir/

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir

ls el_GR_%version/*
cp el_GR_%version/install.rdf %buildroot/%cid_dict_dir

cd -


ln -s %_datadir/myspell/el_GR.aff %buildroot/%cid_dict_dir/dictionaries/el_GR.aff
ln -s %_datadir/myspell/el_GR.dic %buildroot/%cid_dict_dir/dictionaries/el_GR.dic

%files
%cid_dir
%cid_dict_dir


%changelog
* Mon Nov 28 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.4.0-alt1
- Version 31.4.0

* Sun Oct 30 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1.1
- Fix Build

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1
- initial build for ALT Linux Sisyphus
