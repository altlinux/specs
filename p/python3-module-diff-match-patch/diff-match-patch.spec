%define oname diff-match-patch
%define pkgname diff_match_patch

%def_with check

Name: python3-module-%oname
Version: 20230430
Release: alt1

Summary: Python diff, match and patch libraries
License: Apache-2.0
Group: Development/Python3

URL: https://pypi.org/project/diff-match-patch
VCS: https://github.com/diff-match-patch-python/diff-match-patch
Packager: Vladimir Didenko <cow@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
The Diff Match and Patch libraries offer robust algorithms to perform the
operations required for synchronizing plain text.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pkgname
%python3_sitelibdir/%pkgname-%version.dist-info

%changelog
* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 20230430-alt1
- Build new version.
- Build with check.

* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 20181111-alt2
- Build for python2 disabled.

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 20181111-alt1
- new version

* Thu Mar 16 2017 Vladimir Didenko <cow@altlinux.ru> 20121119-alt1
- Initial build for Sisyphus

