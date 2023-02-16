# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: git-retry
Version: 0.0.20230216
Release: alt1
Summary: Bootstrap function to retry a git command
License: BSD-3-Clause
Group: Development/Tools
Url: https://chromium.googlesource.com/chromium/tools/depot_tools/
Requires: git-core

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
%{?!_without_check:%{?!_disable_check:
BuildRequires: git-core
BuildRequires: python3
BuildRequires: python3-module-colorama
}}

%description
%summary.
Part of the chromium depot_tools suite.

%prep
%setup

%install
install -Dp git_retry.py %buildroot%_bindir/git-retry
install -Dpm644 git_common.py  -t %buildroot%python3_sitelibdir_noarch/depot_tools
install -Dpm644 setup_color.py -t %buildroot%python3_sitelibdir_noarch/depot_tools
install -Dpm644 subprocess2.py -t %buildroot%python3_sitelibdir_noarch/depot_tools
install -Dpm644 man/man1/git-retry.1 -t %buildroot%_man1dir

%check
PATH=%buildroot%_bindir:$PATH
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
git retry init

%files
%doc LICENSE
%_bindir/git-retry
%python3_sitelibdir_noarch/depot_tools
%_man1dir/*.1*

%changelog
* Thu Feb 16 2023 Vitaly Chikunov <vt@altlinux.org> 0.0.20230216-alt1
- First import 6b98cdcb (2023-02-16).
