%define modulename cyhunspell
%def_with check

Name: python3-module-%modulename
Version: 2.0.2
Release: alt3
Summary: Cython wrapper on Hunspell Dictionary

License: MIT
Group: Development/Python3
Url: https://github.com/MSeal/cython_hunspell
# Source-url: https://github.com/MSeal/cython_hunspell/archive/refs/tags/%version.tar.gz
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %modulename-%version.tar
Source1: https://github.com/hunspell/hunspell/archive/v1.7.0.tar.gz

BuildRequires: gcc-c++
BuildRequires: libhunspell-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-CacheMan
%endif

Requires: python3-module-CacheMan

%description
This repository provides a wrapper on Hunspell
to be used natively in Python. The module uses
cython to link between the C++ and Python code,
with some additional features. There's very
little Python overhead as all the heavy lifting
is done on the C++ side of the module interface,
which gives optimal performance.

The hunspell library will cache any corrections,
you can use persistent caching by adding the
use_disk_cache argument to a Hunspell constructor.
Otherwise it uses in-memory caching.

%prep
%setup -n %modulename-%version
mkdir -p external
tar -xf %SOURCE1 -C external/

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/*

%changelog
* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt3
- Enabled check back.

* Fri Dec 17 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt2
- Disabled check for python3.10.

* Sun Aug 22 2021 Anton Midyukov <antohami@altlinux.org> 2.0.2-alt1
- initial build
