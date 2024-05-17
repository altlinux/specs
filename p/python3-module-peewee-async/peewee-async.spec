%define oname peewee-async

%def_without check

Name: python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: Asynchronous interface for peewee ORM powered by asyncio

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/peewee-async
VCS: https://github.com/05bit/peewee-async

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-peewee
BuildRequires: python3-module-importlib_metadata
%endif

%py3_provides peewee_async
%py3_requires asyncio peewee aiopg

%description
peewee-async is a library providing asynchronous interface powered by
asyncio for peewee ORM.

%prep
%setup

sed -i 's/0.9.1/%version/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/peewee_async.py
%python3_sitelibdir/peewee_asyncext.py
%python3_sitelibdir/peewee_async-%version.dist-info
%python3_sitelibdir/__pycache__

%changelog
* Fri May 17 2024 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Automatically updated to 0.10.0.

* Mon Sep 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt1
- Automatically updated to 0.9.1.

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

