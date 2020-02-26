%define oname diff-match-patch
%define pkgname diff_match_patch

Name: python3-module-%oname
Version: 20181111
Release: alt2

Summary: Python diff, match and patch libraries
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.python.org/pypi/diff-match-patch/
Packager: Vladimir Didenko <cow@altlinux.org>

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3


%description
The Diff Match and Patch libraries offer robust algorithms to perform the
operations required for synchronizing plain text.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%pkgname/
%python3_sitelibdir/*.egg-*


%changelog
* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 20181111-alt2
- Build for python2 disabled.

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 20181111-alt1
- new version

* Thu Mar 16 2017 Vladimir Didenko <cow@altlinux.ru> 20121119-alt1
- Initial build for Sisyphus

