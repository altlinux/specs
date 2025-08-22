%define _unpackaged_files_terminate_build 1

Name: keama
Version: 4.5.0
Release: alt2.gitd99ec01f

Summary: ISC DHCP Kea Migration Assistant

License: MPL-2.0
Group: System/Configuration/Other
Url: https://gitlab.isc.org/isc-projects/keama

Packager: Maria Alexeeva <alxvmr@altlinux.org>

BuildRequires: make gcc autoconf automake
BuildRequires: libisc-export-dhcp-devel

Source: %name-%version.tar
Patch1: alt-remove-example.patch

%description
This tool analyzes a valid ISC DHCP server configuration file and 
provides an equivalent configuration file for a Kea DHCP server. 
The resulting file is a starting point for your Kea configuration, 
but it will probably require editing before use.

%package -n python3-module-keama-leases
Summary: A tool to migrate the lease file, which contains the running state of your DHCP server. 
Group: System/Configuration/Other
BuildRequires: rpm-build-python3

%description -n python3-module-keama-leases
This tool is used to migrate the lease file, which contains 
the running state ("address assignments" or "leases") of your 
DHCP server. The other, even more important aspect is migration 
of your configuration file, which can be done 
using KeaMA (the Kea Migration Assistant).

%prep
%setup
%autopatch -p1
sed -i '1s|^#!.*|#!/usr/bin/python3|' leases/%name-leases.py
sed -i 's|\./configure |%autoreconf \&\& &|' bind/Makefile.in
# make sure it's there
grep autoreconf bind/Makefile.in

%build
%add_optflags -I%_includedir/bind9

%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -f %buildroot/%_libdir/libdhcp.a
rm -rf %buildroot/%_includedir/omapip/
# The page is taken from the vendor-provided libdhcp and is not related to the keama package.
# Also this page is provided by the dhcp-server package.
rm -rf %buildroot/%_man5dir/*

mkdir -p \
	%buildroot%python3_sitelibdir/leases/

cp leases/*.py \
	%buildroot%python3_sitelibdir/leases/

ln -s %python3_sitelibdir/leases/%name-leases.py  \
	%buildroot%_bindir/%name-leases

%files
%_bindir/%name
%_man8dir/*

%files -n python3-module-keama-leases
%_bindir/%name-leases
%attr(755,-,-) %python3_sitelibdir/leases/%name-leases.py
%python3_sitelibdir/leases/__pycache__/*.pyc

%changelog
* Fri Aug 22 2025 Ivan A. Melnikov <iv@altlinux.org> 4.5.0-alt2.gitd99ec01f
- NMU: Use %%autoreconf (fixes FTBFS on loongarch64 and riscv64)

* Sun Jul 13 2025 Maria Alexeeva <alxvmr@altlinux.org> 4.5.0-alt1.gitd99ec01f
- First build
