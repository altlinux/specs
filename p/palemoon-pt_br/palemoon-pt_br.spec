%define cid            langpack-pt-BR@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       pt-BR@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	33.3.0
%define max_version	34.0.*


Name: palemoon-pt_br

Version: 33.3.0
Release: alt1

Summary: Portuguese (Brazilian) Language Pack for Pale Moon
License: MPL-2.0

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: pt_br_palemoon_%version.xpi
Source2: pt_BR_%version.tar


Requires: hunspell-pt
Requires: palemoon >= 33.3.0

ExclusiveArch: x86_64 aarch64

BuildRequires(pre):	rpm-build-palemoon
# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: unzip

%description
Portuguese (Brazilian) Language Pack for Pale Moon

%prep
%setup -c -n %name-%version/%cid

cd ..
tar -xf  %SOURCE2

%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries


# Install translation
cp -r -- %cid/* %buildroot/%cid_dir


ls pt_BR_%version/*
cp pt_BR_%version/install.rdf %buildroot/%cid_dict_dir


cd -

ln -s %_datadir/myspell/pt_BR.aff %buildroot/%cid_dict_dir/dictionaries/pt-BR.aff
ln -s %_datadir/myspell/pt_BR.dic %buildroot/%cid_dict_dir/dictionaries/pt_BR.dic


%files
%cid_dir
%cid_dict_dir


%changelog
* Thu Aug 15 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.3.0-alt1
- Version 33.3.0

* Thu Jul 18 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.2.0-alt1
- Version 33.2.0

* Mon May 06 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.1.0-alt1
- Version 33.1.0

* Sun Feb 04 2024 Hihin Ruslan <ruslandh@altlinux.ru> 33.0.0-alt1
- Version 33.0.0

* Mon Nov 20 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.5.0-alt1
- Version 32.5.0

* Mon Sep 18 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.4.0-alt1
- Version 32.4.0

* Sun Sep 17 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.0.0-alt1.1
- Add ExcludeArch ppc64le

* Tue Jan 31 2023 Hihin Ruslan <ruslandh@altlinux.ru> 32.0.0-alt1
- Version 32.0.0

* Tue Nov 29 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.4.0-alt1
- Build Version 31.4.0

* Sun Oct 30 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1.1
- Fix Build 

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 31.3.0-alt1
- initial build for ALT Linux Sisyphus
