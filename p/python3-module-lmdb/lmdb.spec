%define oname lmdb

%def_with check

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: Universal Python binding for the LMDB 'Lightning' Database

License: OpenLDAP BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/lmdb/

# https://github.com/dw/py-lmdb.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: liblmdb-devel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cffi
%endif

%description
Universal Python binding for the LMDB 'Lightning' Database.

%prep
%setup

%build
export LMDB_FORCE_SYSTEM=1
%python3_build

%install
export LMDB_FORCE_SYSTEM=1
%python3_install

%check
%__python3 setup.py build_ext -i
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%doc ChangeLog *.md docs/*.rst examples LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Dec 09 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Sat Dec 11 2021 Grigory Ustinov <grenka@altlinux.org> 0.93-alt3
- Fixed build with python3.10.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.93-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.93-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.93-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.93-alt1
- Updated to upstream version 0.93.

* Wed Jun 29 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.89-alt1
- Updated to 0.89.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.84-alt1.git20141109.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84-alt1.git20141109
- Initial build for Sisyphus
