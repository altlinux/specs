%define modulename CacheMan

%def_disable check

Name: python3-module-%modulename
Version: 2.1.0
Release: alt1
Summary: A Python interface for managing dependent caches

License: BSD
Group: Development/Python3
Url: https://github.com/MSeal/py_cache_manager
# Source-url: https://github.com/MSeal/py_cache_manager/archive/refs/tags/%version.tar.gz
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%if_disabled check
%else
BuildRequires: python3-module-pytest
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
* Sun Aug 22 2021 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- initial build
