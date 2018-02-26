Name: mithraen-installer-busybox
Version: 1.10.1
Release: alt2.1

Obsoletes: seiros-installer-busybox

Summary: Busybox build for installer
License: GPL
Group: System/Kernel and hardware

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: busybox.tar
Source1: %name.config

BuildRequires: glibc-kernheaders

Patch1: cpio.patch
Patch2: getopt.patch
Patch3: iptunnel.patch

%description
%summary

%prep
%setup -q -c
%patch1 -p0
#patch2 -p0
%patch3 -p2
cp %SOURCE1 .config

%build
# SMP-incompatible build - fails to build config.h before it is needed :(
%make oldconfig
%make_build
#LIBRARIES="-lcompat"

%install
%make_install install
mkdir -p %buildroot%_datadir/%name
cd _install
mkdir -p usr/sbin usr/bin
pushd bin
for s in *; do
  ln -sf ../../bin/$s ..%_bindir/$s
done
popd
pushd sbin
for s in *; do
  ln -sf ../../sbin/$s ..%_sbindir/$s
done
popd
ln -s /bin/busybox sbin/ip
find . | cpio -o -c > %buildroot%_datadir/%name/busybox.cpio

%files
%dir %_datadir/%name
%_datadir/%name/busybox.cpio

%changelog
* Tue Feb 02 2010 Kirill A. Shutemov <kas@altlinux.org> 1.10.1-alt2.1
- NMU:
  + Fix build with new glibc-kernheaders

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 1.10.1-alt2
- package %_datadir/%name

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 1.10.1-alt1
- first build for Sisyphus



