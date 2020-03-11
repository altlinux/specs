%define oname jenkins

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: Python ctypes wrapper around Bob Jenkins' hash functions
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jenkins/

# https://github.com/lgastako/jenkins.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This python module provides Bob Jenkin's hash functions in python (via
a ctypes wrapper calling the original C implementation).

%prep
%setup

sed -i 's|@CPYTHON@|.cpython-%{python_version_nodots python3}|' jenkins.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Wed Mar 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1.git20091202.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20091202.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20091202.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20091202
- Initial build for Sisyphus

