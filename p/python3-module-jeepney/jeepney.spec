%def_with check
Name: python3-module-jeepney
Version: 0.8.0
Release: alt1
License: MIT
Group: Development/Python3
Url: https://gitlab.com/takluyver/jeepney
Source: jeepney-%version.tar.gz

Summary: Pure Python DBus interface
BuildRequires(pre): rpm-build-python3
%if_with check
# Automatically added by buildreq on Sun Apr 17 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-packaging python3-module-pep517 python3-module-pyparsing python3-module-tomli sh4
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools

BuildRequires: python3-module-async-timeout python3-module-build python3-module-flit python3-module-pytest-asyncio python3-module-setuptools python3-module-trio
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
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.8.0-alt1
- Autobuild version bump to 0.8.0
- Switch build scheme
- Introduce tests

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Autobuild version bump to 0.6.0

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.0-alt0
- Empty skeleton

