%define _unpackaged_files_terminate_build 1
%def_with check
%define py_name libkirk

Name: kirk
Version: 4.2.0
Release: alt4

Summary: The official executor of Linux Test Project
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://kirk.readthedocs.io/en/latest/
Vcs: https://github.com/linux-test-project/kirk.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio

BuildRequires: /proc
BuildRequires: ltp-testsuite
%endif

%description
Kirk is the official executor of Linux Test Project (LTP). It provides
support for remote testing via Qemu, SSH, LTX, parallel execution and
much more.

This package contains the kirk tools and utilities.


%package -n python3-module-%py_name
Summary: Python library for Kirk
Group: Development/Python

%description -n python3-module-%py_name
Kirk is the official executor of Linux Test Project (LTP). It provides
support for remote testing via Qemu, SSH, LTX, parallel execution and
much more.

This package contains the kirk python library.


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%__install -Dm755 utils/json2html.py %buildroot%_libexecdir/%name/json2html
%__install -Dm755 utils/json2logs.py %buildroot%_libexecdir/%name/json2logs

%check
%pyproject_run_pytest

%files
%_bindir/*
%_libexecdir/%name

%files -n python3-module-%py_name
%python3_sitelibdir_noarch/%{py_name}*
%python3_sitelibdir_noarch/%{name}*

%changelog
* Wed Sep 16 2026 Ivan A. Melnikov <iv@altlinux.org> 4.2.0-alt4
- correct license (thx andy@)

* Wed Sep 16 2026 Ivan A. Melnikov <iv@altlinux.org> 4.2.0-alt3
- correct package summary and description

* Tue Sep 08 2026 Ivan A. Melnikov <iv@altlinux.org> 4.2.0-alt2
- package utils to %_libexecdir/%name.

* Tue Sep 08 2026 Ivan A. Melnikov <iv@altlinux.org> 4.2.0-alt1
- 4.2.0

* Mon Sep 07 2026 Ivan A. Melnikov <iv@altlinux.org> 4.1.0-alt1
- build for Sisyphus
- fix test_com tests on slower machines
- set defalut LTPROOT to /usr/lib/ltp to match ALT ltp-suite packaging
