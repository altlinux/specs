# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: codespell
Version: 2.2.6
Release: alt1
Summary: Check code for common misspellings
Group: Development/Tools
License: GPL-2.0-only
Url: https://github.com/codespell-project/codespell
BuildArch: noarch

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: help2man
BuildRequires: python3-devel >= 3.8
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%{?!_without_check:%{?!_disable_check:
BuildRequires: pytest3
BuildRequires: python3-module-chardet
BuildRequires: python3-module-pytest-cov
}}

%description
Fix common misspellings in text files. It's designed primarily for checking
misspelled words in source code, but it can be used with other files as well.

%prep
%setup
subst 's/help2man/& -L en_US.UTF-8 --no-discard-stderr/' Makefile

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

# Manpage requires 'codespell' executable.
# Create venv then make it accessible.
%pyproject_run true
PATH=$PWD/.run_venv/bin:$PATH
type codespell
# Note: man-page is incorrectly formatted because it uses GNU help2man which
# don't understand Python argparse output.
make codespell.1
! grep 'runas:' codespell.1 || exit 1

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
install -D -m644 %name.1 %buildroot%_man1dir/%name.1
# Compatibility with scripts/checkpatch.pl
ln -sf -r %buildroot%python3_sitelibdir/codespell_lib/data %buildroot%_datadir/codespell
# I think we don't need this:
rm -rf %buildroot%python3_sitelibdir/codespell_lib/data/{__pycache__,__init__.py}

%check
# codespell executable is required both for pytest and our smoke test.
PATH=%buildroot%_bindir:$PATH

# UserWarning: aspell not found, but not required, skipping aspell tests.
%pyproject_run_pytest

export PYTHONPATH=%buildroot%python3_sitelibdir
codespell --version | grep -Fw %version
echo Millenium  > /tmp/example.txt
! codespell /tmp/example.txt || exit 2
  codespell --ignore-words-list=millenium /tmp/example.txt
  codespell --summary --write-changes /tmp/example.txt |& grep FIXED
  codespell /tmp/example.txt
  grep -qx Millennium /tmp/example.txt
  rm /tmp/example.txt

%files
%define _customdocdir %_docdir/%name
%doc COPYING README.rst
%_bindir/%name
%_man1dir/%name.1*
%python3_sitelibdir/*
%_datadir/codespell

%changelog
* Tue Oct 03 2023 Vitaly Chikunov <vt@altlinux.org> 2.2.6-alt1
- Update to v2.2.6 (2023-09-30).
- Fix man page generation error.
- spec: Improve testing.

* Thu Jun 15 2023 Vitaly Chikunov <vt@altlinux.org> 2.2.5-alt1
- Update to v2.2.5 (2023-06-14).

* Thu Mar 09 2023 Vitaly Chikunov <vt@altlinux.org> 2.2.4-alt1
- Update to v2.2.4 (2023-03-08).

* Tue Oct 18 2022 Vitaly Chikunov <vt@altlinux.org> 2.2.2-alt1
- Update to v2.2.2 (2022-10-14).

* Fri Aug 19 2022 Vitaly Chikunov <vt@altlinux.org> 2.2.1-alt1
- Update to v2.2.1 (2022-08-18).

* Thu Aug 18 2022 Vitaly Chikunov <vt@altlinux.org> 2.2.0-alt1
- Update to v2.2.0 (2022-08-17).

* Fri Jun 11 2021 Vitaly Chikunov <vt@altlinux.org> 2.1.0-alt1
- Update to v2.1.0 (2021-06-10).

* Wed Nov 25 2020 Vitaly Chikunov <vt@altlinux.org> 2.0.0-alt1
- Update to v2.0.0 (2020-11-23).

* Mon May 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.17.1-alt1
- Update to v1.17.1.

* Wed Sep 18 2019 Vitaly Chikunov <vt@altlinux.org> 1.16.0.0.5.g8b321f0-alt1
- Build v1.16.0-5-g8b321f0

* Thu Oct 04 2018 Vitaly Chikunov <vt@altlinux.ru> 1.14.0-alt1
- First packaging for ALT
