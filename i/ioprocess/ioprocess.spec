%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: ioprocess
Version: 1.4.2
Release: alt1
Summary: Slave process to perform risky IO

Group: System/Base
License: GPLv2+
Url: https://github.com/oVirt/ioprocess

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gthread-2.0)
BuildRequires: libyajl-devel
BuildRequires: schedutils
BuildRequires: util-linux

Requires: yajl

%description
Slave process to perform risky IO.

%package -n python3-module-%name
Summary: Python bindings for ioprocess
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description -n python3-module-%name
Python bindings for ioprocess

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md AUTHORS
%_libexecdir/ioprocess

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1.4.2-alt1
- Initial build.

