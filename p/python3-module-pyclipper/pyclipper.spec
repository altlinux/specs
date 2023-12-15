%define oname pyclipper

%def_with check

Name: python3-module-%oname
Version: 1.3.0.post5
Release: alt1

Summary: Cython wrapper for the C++ translation of the Angus Johnson's Clipper library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyclipper
Vcs: https://github.com/fonttools/pyclipper

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools_scm
BuildRequires: gcc-c++
%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname

%description
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the Angus Johnson's Clipper library.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Fri Dec 15 2023 Anton Vyatkin <toni@altlinux.org> 1.3.0.post5-alt1
- New version 1.3.0.post5.

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.6-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1
- NMU: rebuild with libpolyclipping
- new version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.b0.git20150320.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.b0.git20150320
- Initial build for Sisyphus

