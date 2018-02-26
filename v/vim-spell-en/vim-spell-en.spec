# vim: set ft=spec: -*- rpm-spec -*-
# $Id: vim-spell-en,v 1.1 2006/03/29 15:21:34 raorn Exp $

%define spelllang en
%define fulllang English

Name: vim-spell-%spelllang
Version: %vimspell_version.20060311
Release: alt1

Summary: VIM spelling dictionaries (%fulllang)
Group: Text tools
License: distributable
Url: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries

BuildArch: noarch

Source1: %url/en_US.zip
Source2: %url/en_AU.zip
Source3: %url/en_CA.zip
Source4: %url/en_GB.zip
Source5: %url/en_NZ.zip

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
for dict in en_US en_AU en_CA en_GB en_NZ; do
  %__unzip -qa "%_sourcedir/$dict.zip"
  patch <"$dict.diff"
done
popd

%build
pushd %spelllang
  echo "en_US:" >../README_%spelllang.txt
  %__cat README_en_US.txt >>../README_%spelllang.txt
  echo "===================================================" >>../README_%spelllang.txt
  echo "en_AU:" >>../README_%spelllang.txt
  %__cat README_en_AU.txt >>../README_%spelllang.txt
  echo "===================================================" >>../README_%spelllang.txt
  echo "en_CA:" >>../README_%spelllang.txt
  %__cat README_en_CA.txt >>../README_%spelllang.txt
  echo "===================================================" >>../README_%spelllang.txt
  echo "en_GB:" >>../README_%spelllang.txt
  %__cat README_en_GB.txt >>../README_%spelllang.txt
  echo "===================================================" >>../README_%spelllang.txt
  echo "en_NZ:" >>../README_%spelllang.txt
  %__cat README_en_NZ.txt >>../README_%spelllang.txt
popd

%mkvimspell -a                 %spelllang %spelllang/en_US %spelllang/en_AU %spelllang/en_CA %spelllang/en_GB %spelllang/en_NZ
%mkvimspell -L en_US.ISO8859-1 %spelllang %spelllang/en_US %spelllang/en_AU %spelllang/en_CA %spelllang/en_GB %spelllang/en_NZ
%mkvimspell -L en_US.UTF-8     %spelllang %spelllang/en_US %spelllang/en_AU %spelllang/en_CA %spelllang/en_GB %spelllang/en_NZ

%install
%__mkdir_p %buildroot%vim_spell_dir

%__install -p -m644 %spelllang.* %buildroot%vim_spell_dir/

%files
%doc README_%spelllang.txt
%vim_spell_dir/%spelllang.*

%changelog
* Wed Mar 29 2006 Sir Raorn <raorn@altlinux.ru> 50.1.20060311-alt1
- Built for vim7

