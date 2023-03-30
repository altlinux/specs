%define oname leveldb

%def_with check

Name: python3-module-%oname
Version: 0.201
Release: alt1

Summary: Python bindings for leveldb database library
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/leveldb/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++

%py3_provides %oname

%description
Python bindings for leveldb database library.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m unittest discover -v test/

%files
%doc README LICENSE
%python3_sitelibdir/*


%changelog
* Thu Mar 30 2023 Anton Vyatkin <toni@altlinux.org> 0.201-alt1
- New version 0.201.

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

