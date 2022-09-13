%def_with check
Name: python3-module-jeepney
Version: 0.8.0
Release: alt1.1
License: MIT
Group: Development/Python3
Url: https://gitlab.com/takluyver/jeepney
Source: jeepney-%version.tar.gz

Summary: Pure Python DBus interface
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-build
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-async-timeout
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-trio
%endif

BuildRequires: python3-dev
BuildArch: noarch

%description
Jeepney is a pure Python implementation of D-Bus messaging. It has an
I/O-free core, and integration modules for different event loops.

D-Bus is an inter-process communication system, mainly used in Linux.

%package extras
Group: Development/Python3
Summary: Extra dependencies of jeepney

%description extras
Extra dependencies for jeepney, namely tests and trio I/O

%prep
%setup -n jeepney-%version

%build
python3 -m build -n

%if_with check
%check
python3 -m pytest
%endif

%install
pip3 install --root=%buildroot --no-deps dist/jeepney-%version-py3-none-any.whl

%files
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/jeepney/io/trio.py
%exclude %python3_sitelibdir_noarch/jeepney/tests
%exclude %python3_sitelibdir_noarch/jeepney/io/tests

%files extras
%python3_sitelibdir_noarch/jeepney/io/trio.py
%python3_sitelibdir_noarch/jeepney/tests
%python3_sitelibdir_noarch/jeepney/io/tests

%changelog
* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1.1
- NMU: Fixed build requires

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.8.0-alt1
- Autobuild version bump to 0.8.0
- Switch build scheme
- Introduce tests

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Autobuild version bump to 0.6.0

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.0-alt0
- Empty skeleton

