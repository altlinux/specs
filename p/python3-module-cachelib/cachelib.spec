%define  srcname cachelib

# needed /proc/1/stat
%def_disable check

Name:    python3-module-%srcname
Version: 0.2.0
Release: alt1

Summary: A collection of cache libraries in the same API interface
License: BSD
Group:   Development/Python3
URL:     https://github.com/pallets/cachelib

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: memcached
BuildRequires: redis
BuildRequires: python3-module-pylibmc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xprocess
%endif

BuildArch: noarch

# Source-url: https://github.com/pallets/cachelib/archive/refs/tags/%version.tar.gz
Source: %srcname-%version.tar

%description
%summary.

%prep
%setup -n %srcname-%version

%build
%python3_build

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.md

%changelog
* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
