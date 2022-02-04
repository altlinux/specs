%define modulename CacheMan

%def_with check

Name: python3-module-%modulename
Version: 2.1.0
Release: alt2

Summary: A Python interface for managing dependent caches

License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/MSeal/py_cache_manager
# Source-url: https://github.com/MSeal/py_cache_manager/archive/refs/tags/%version.tar.gz
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %modulename-%version.tar
# Fix compatibility with Python 3.10
Patch: d8d9adbce96cf132504d0cd9bd64a2ada72875cd.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-future
BuildRequires: python3-module-six
BuildRequires: python3-module-psutil
BuildRequires: /proc
%endif

%description
This module acts as a dependency manager for caches and is ideal for instances
where a program has many repeated computations that could be safely persisted.
This usually entails a DB layer to house key value pairs. However, such a layer
is sometimes overkill and managing a DB along with a project can be more effort
than it's worth. That's where CacheMan comes in and provides an interface
through which you can define savers, loaders, builders, and dependencies with
disk-based defaults.

By default all caches will auto save when 10k changes occur over 60 seconds, 10
changes occur over 300 seconds (but after 60 seconds), or 1 change occurs within
900 seconds (after 300 seconds). This behavior can be changed by instantiating
an AutoSyncCache from the autosync submodule.

%prep
%setup -n %modulename-%version
%patch -p1

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2
- Fix compatibility with Python 3.10.
- Enable check.

* Sun Aug 22 2021 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- initial build
