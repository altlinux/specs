%define _unpackaged_files_terminate_build 1
%def_without test

%define oname texext

Name: python3-module-%oname
Version: 0.6.6
Release: alt1

Summary: Sphinx extensions for working with LaTeX math
License: BSD
Group: Development/Python3
Url: https://github.com/matthew-brett/texext

BuildArch: noarch

# https://github.com/matthew-brett/texext.git
Source: %name-%version.tar
Patch0: texext-0.6.1-Adapt-tests-to-Sphinx-2-output.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-docutils
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxtesters
BuildRequires: python3-module-sympy
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-matplotlib-sphinxext

%description
Texext - sphinx extensions for working with LaTeX math.

%prep
%setup
#patch0 -p1

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%build
%python3_build

%install
%python3_install

%check
py.test3 -vv

%files
%python3_sitelibdir/*

%changelog
* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt1
- NMU: new version 0.6.6
- NMU: disable tests (wait for real users of texext)

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- Build for python2 disabled.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 0.6.1-alt2
- Fixed testing against Sphinx 2.x.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Build new version.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1
- Initial build for ALT.
