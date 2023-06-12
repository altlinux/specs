%define oname peewee-async

%def_with check

Name: python3-module-%oname
Version: 0.8.1
Release: alt1

Summary: Asynchronous interface for peewee ORM powered by asyncio

License: MIT
Group: Development/Python3
Url: http://peewee-async.readthedocs.org/en/latest/

# https://github.com/05bit/peewee-async.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-peewee
%endif

%py3_provides peewee_async
%py3_requires asyncio peewee aiopg

%description
peewee-async is a library providing asynchronous interface powered by
asyncio for peewee ORM.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md docs/*.rst docs/peewee_async
%python3_sitelibdir/peewee_async.py
%python3_sitelibdir/peewee_asyncext.py
%python3_sitelibdir/peewee_async-%version-py%_python3_version.egg-info
%python3_sitelibdir/__pycache__

%changelog
* Mon Jun 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Automatically updated to 0.8.1.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Automatically updated to 0.8.0.

* Tue Jun 07 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.2-alt1
- Automatically updated to 0.7.2.

* Sat Jun 05 2021 Grigory Ustinov <grenka@altlinux.org> 0.0.2-alt2.git20141030
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt1.git20141030.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20141030.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141030
- Initial build for Sisyphus

