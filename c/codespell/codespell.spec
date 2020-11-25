# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:		codespell
Version:	2.0.0
Release:	alt1
Summary:	Check code for common misspellings
Group:		Development/Tools
License:	GPL-2.0-only
Url:		https://github.com/codespell-project/codespell
Vcs:		https://github.com/codespell-project/codespell.git
Source:		%name-%version.tar
BuildArch:	noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: help2man
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Fix common misspellings in text files. It's designed primarily for checking
misspelled words in source code, but it can be used with other files as well.

%prep
%setup
subst 's/help2man/& -L en_US.UTF-8 --no-discard-stderr/' Makefile

%build
%python3_build
make codespell.1

%install
%python3_install
install -D -m644 %name.1 %buildroot%_man1dir/%name.1
# Compatibility with scripts/checkpatch.pl
ln -sf -r %buildroot%python3_sitelibdir/codespell_lib/data %buildroot/usr/share/codespell
# I think we don't need this:
rm -rf %buildroot%python3_sitelibdir/codespell_lib/data/{__pycache__,__init__.py}

%check
cd %buildroot
export PYTHONPATH=$PWD%python3_sitelibdir
PATH=$PWD%_bindir:$PATH
codespell --version
echo Millenium  > /tmp/example.txt
! codespell /tmp/example.txt
  codespell --ignore-words-list=millenium /tmp/example.txt
! codespell --summary --write-changes /tmp/example.txt
  codespell /tmp/example.txt
  grep -qx Millennium /tmp/example.txt

%files
%doc COPYING README.rst
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir/*
/usr/share/codespell

%changelog
* Wed Nov 25 2020 Vitaly Chikunov <vt@altlinux.org> 2.0.0-alt1
- Update to v2.0.0 (2020-11-23).

* Mon May 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.17.1-alt1
- Update to v1.17.1.

* Wed Sep 18 2019 Vitaly Chikunov <vt@altlinux.org> 1.16.0.0.5.g8b321f0-alt1
- Build v1.16.0-5-g8b321f0

* Thu Oct 04 2018 Vitaly Chikunov <vt@altlinux.ru> 1.14.0-alt1
- First packaging for ALT
