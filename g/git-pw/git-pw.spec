# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: git-pw
Summary: Git-Patchwork integration tool
Version: 2.4.0
Release: alt1
License: MIT
Group: Development/Tools
Url: https://github.com/getpatchwork/git-pw

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-arrow    >= 0.10
BuildRequires: python3-module-click    >= 6.0
BuildRequires: python3-module-pbr
BuildRequires: python3-module-pyaml    >= 5.1
BuildRequires: python3-module-requests >= 2.0
BuildRequires: python3-module-tabulate >= 0.8
# For %%check
BuildRequires: git-core
BuildRequires: python3-module-pytest   >= 3.0

%description
git-pw is a tool for integrating Git with Patchwork, the web-based
patch tracking system.

%prep
%setup

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install
install -p -D -m 644 man/*.1 -t %buildroot%_man1dir

%check
PYTHONPATH=%buildroot%python3_sitelibdir_noarch py.test3

%files
%doc LICENSE README.rst
%_bindir/git-pw
%python3_sitelibdir_noarch/git_pw*
%_man1dir/git-pw*.1*

%changelog
* Thu Dec 08 2022 Vitaly Chikunov <vt@altlinux.org> 2.4.0-alt1
- Update to 2.4.0 (2022-12-06).

* Tue Feb 01 2022 Vitaly Chikunov <vt@altlinux.org> 2.2.3-alt1
- First import of 2.2.3 (2021-11-29).
