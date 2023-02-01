%define cid            langpack-uk@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       uk@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	32.0.0
%define max_version	33.0.*

%define bname		newmoon
%define newmoon_dir 	%palemoon_datadir/browser/

Name: palemoon-uk

Version: 32.0.0
Release: alt1

Summary: Ukrainian (UA) Language Pack for Pale Moon
License: MPL-2.0

ExcludeArch: %ix86 %arm

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: uk_palemoon_%version.xpi
Source2: uk_UA_%version.tar

Requires: hunspell-uk
Requires: palemoon >= 27.7.0

#BuildArch: noarch

BuildRequires(pre):	rpm-build-palemoon

# Automatically added by buildreq on Mon Nov 28 2022
# optimized out: libgpg-error sh4
BuildRequires: unzip


%description
The Palemoon Ukrainian translation and dictionary.

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
ls uk_UA_%version/*
cp uk_UA_%version/install.rdf %buildroot/%cid_dict_dir

cd -


ln -s %_datadir/myspell/uk_UA.aff %buildroot/%cid_dict_dir/dictionaries/uk-UA.aff
ln -s %_datadir/myspell/uk_UA.dic %buildroot/%cid_dict_dir/dictionaries/uk-UA.dic

%files
%cid_dir
%cid_dict_dir

%changelog
* Wed Feb 01 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.0.0-alt1
- Update to release 32.0.0

* Mon Nov 28 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.4.0-alt1
- Update to release 31.4.0

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1
- Update to release 31.3.0

* Sat Aug 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.2.0-alt1
- Update to release 31.2.0

* Sun Apr 15 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.9.0-alt1
- Update for release 27.7.9-RC3

* Tue Mar 13 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.8.0-alt1
- Update from https://github.com/JustOff/pale-moon-localization.git
  commit db3903541364659a9299cae4016a1210b5f5fbd2

* Wed Jan 17 2018 Hihin Ruslan <ruslandh@altlinux.ru> 27.7.0-alt1
- Update for release 27.7.0-RC6

* Tue Nov 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.6.0-alt1
- Update for release 27.6.0-RC3

* Sun Sep 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt4
- Update Translations

* Mon Aug 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt3
- Update Translations

* Sun Aug 20 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt2
- Update Translations

* Sun Aug 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.5.0-alt1
- Update for release 27.5.0_RC4

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt1
- initial build for ALT Linux Sisyphus
