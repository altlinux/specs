%define oname leveldb

Name: python3-module-%oname
Version: 0.193
Release: alt4

Summary: Python bindings for leveldb database library
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/leveldb/

Source: %name-%version.tar
Patch0: py38-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3-module-nose

%py3_provides %oname


%description
Python bindings for leveldb database library.

%prep
%setup
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3

%files
%doc README
%python3_sitelibdir/*


%changelog
* Tue Feb 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.193-alt4
- Build for python 3.8 fixed.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.193-alt3
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.193-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Feb 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.193-alt2
- fix build on aarch64

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.193-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.193-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.193-alt1.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.193-alt1
- Initial build for Sisyphus

