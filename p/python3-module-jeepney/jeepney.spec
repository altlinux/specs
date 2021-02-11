Name: python3-module-jeepney
Version: 0.6.0
Release: alt1
License: MIT
Group: Development/Python3
Url: https://gitlab.com/takluyver/jeepney
Source: jeepney-%version.tar.gz

Summary: Pure Python DBus interface
BuildRequires(pre): rpm-build-python3
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
Extra dependencies for jeepney, namely, tornado and trio I/O

%prep
%setup -n jeepney-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/jeepney/io/tornado.py
%exclude %python3_sitelibdir_noarch/jeepney/integrate/tornado.py
%exclude %python3_sitelibdir_noarch/jeepney/io/trio.py
%exclude %python3_sitelibdir_noarch/jeepney/tests
%exclude %python3_sitelibdir_noarch/jeepney/io/tests
%exclude %python3_sitelibdir_noarch/jeepney/integrate/tests

%files extras
%python3_sitelibdir_noarch/jeepney/io/tornado.py
%python3_sitelibdir_noarch/jeepney/io/trio.py
%python3_sitelibdir_noarch/jeepney/integrate/tornado.py
%python3_sitelibdir_noarch/jeepney/tests
%python3_sitelibdir_noarch/jeepney/io/tests
%python3_sitelibdir_noarch/jeepney/integrate/tests

%changelog
* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Autobuild version bump to 0.6.0

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 0.0-alt0
- Empty skeleton

