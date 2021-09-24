%define srcname gsocketpool

#%%def_disable check

Name:    python3-module-%srcname
Version: 0.1.6
Release: alt1

Summary: Lightweight MessagePack RPC library
License: ASL-2.0
Group:   Development/Python3
URL:     https://github.com/studio-ousia/gsocketpool

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-gevent
BuildRequires: python3-module-nose
BuildRequires: python3-module-mock
%endif

# Source-url: https://github.com/studio-ousia/gsocketpool/archive/refs/tags/v%version.tar.gz
Source: %srcname-%version.tar

BuildArch: noarch

%description
mprpc is a lightweight MessagePack RPC library. It enables you to easily build
a distributed server-side system by writing a small amount of code. It is built
on top of gevent and MessagePack.

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
%doc *.rst

%changelog
* Fri Sep 24 2021 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus
