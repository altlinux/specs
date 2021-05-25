%define oname banyan

# very slow!
%def_disable check

Name: python3-module-%oname
Version: 0.1.6
Release: alt2.git20141121
Summary: Backup of Banyan Python module
License: BSD
Group: Development/Python3
Url: https://github.com/pyannote/pyannote-banyan

# https://github.com/pyannote/pyannote-banyan.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-build.patch

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-UnittestRandGenState python3-module-pytest
BuildRequires: python3-module-matplotlib python3-module-six

%py3_provides %oname
%py3_provides %{oname}_c

%description
Highly-optimized search trees (red-black, splay, and sorted-list) with
optional augmentation (dynamic order statistics, interval trees, etc.)

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Highly-optimized search trees (red-black, splay, and sorted-list) with
optional augmentation (dynamic order statistics, interval trees, etc.)

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%build
%add_optflags -fno-strict-aliasing -fpermissive -std=gnu++11
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.6-alt2.git20141121
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1.git20141121.2.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1.git20141121.2
- Fixed build.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.git20141121.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141121.1
- NMU: Use buildreq for BR.

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141121
- Version 0.1.6

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5.1-alt1.git20141112
- Initial build for Sisyphus

