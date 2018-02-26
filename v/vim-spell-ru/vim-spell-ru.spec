# vim: set ft=spec: -*- rpm-spec -*-
# $Id: vim-spell-ru,v 1.1 2006/03/29 15:21:35 raorn Exp $

%define spelllang ru
%define fulllang Russian

Name: vim-spell-%spelllang
Version: %vimspell_version.20050915
Release: alt1

Summary: VIM spelling dictionaries (%fulllang)
Group: Text tools
License: distributable
Url: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries

BuildArch: noarch

Source1: %url/ru_RU.zip
Source2: %url/ru_RU_yo.zip

BuildPreReq: vim-devel >= 4:7.0

# Automatically added by buildreq on Wed Mar 29 2006
BuildRequires: unzip vim-console vim-spell-source

%description
VIM (VIsual editor iMproved) is an updated and improved version of the vi
editor.  Vi was the first real screen-based editor for UNIX, and is still
very popular.  VIM improves on vi by adding new features: multiple windows,
multi-level undo, block highlighting and more.  The vim-common package
contains files which every VIM binary will need in order to run.

This package contains dictionaries for VIM's spellcheking feature (%fulllang).

%prep
%setup -T -c
%__cp -a %vim_spell_source_dir/%{spelllang}* .
pushd %spelllang
  %__unzip -qa %SOURCE1
  %__unzip -qa %SOURCE2
  %__mv ru_RU_yo.aff ru_YO.aff
  %__mv ru_RU_yo.dic ru_YO.dic
  patch <ru_RU.diff
  patch <ru_YO.diff
popd

%build
pushd %spelllang
  echo "ru_RU:" > ../README_%spelllang.txt
  %__cat README_ru_RU.txt >> ../README_%spelllang.txt
  echo "===================================================" >> ../README_%spelllang.txt
  echo "ru_YO:" >> ../README_%spelllang.txt
  %__cat README_ru_RU_yo.txt >> ../README_%spelllang.txt
popd

for enc in KOI8-R CP1251 UTF-8; do
  %mkvimspell -L ru_RU.$enc %spelllang %spelllang/ru_RU %spelllang/ru_YO
done

%install
%__mkdir_p %buildroot%vim_spell_dir

%__install -p -m644 %spelllang.* %buildroot%vim_spell_dir/

%files
%doc README_%spelllang.txt
%vim_spell_dir/%spelllang.*

%changelog
* Wed Mar 29 2006 Sir Raorn <raorn@altlinux.ru> 50.1.20050915-alt1
- Built for vim7

