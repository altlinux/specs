%define oname cHaversine

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: Fast haversine calculation
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/cHaversine

# https://github.com/doublemap/cHaversine.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

%py3_provides %oname


%description
Fast haversine calculation. Returns distance between two lat/lon pairs
in meters. Implemented using Cython.

%prep
%setup

%build
cython3 %oname/%oname.pyx
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v
%__python3 setup.py build_ext -i
%__python3 test_cHaversine.py -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1.git20150527.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150527.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150527.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150527
- Initial build for Sisyphus

