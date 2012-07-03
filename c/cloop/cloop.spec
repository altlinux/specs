%def_disable debug

Name: cloop
Version: 2.628
%define subver -2
Release: alt1
Summary: %name kernel module and utils
License: %gpl2only
Group: Development/Kernel
URL: http://debian-knoppix.alioth.debian.org/
Source: %url/sources/%{name}_%version%subver.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ zlib-devel kernel-build-tools

%description
%name (Compressed loop) Linux kernel module and utils.


%package -n kernel-source-%name
Summary: %name Linux kernel module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
This is %name sources, a Linux kernel module to add support for
filesystem-independent, transparently decompressed, read-only block
devices.


%package utils
Summary: Tools for handling with %name compressed volumes
Group: System/Base

%description utils
Utilities for creating and unpacking compressed loopback files for
%name.


%prep
%setup
%patch -p1


%build
%define _optlevel 3
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build {create,extract}_compressed_fs %{name}_suspend
bzip2 --best --keep --force debian/changelog


%install
rm -rf kernel-source-%name-%version
install -d -m 0755 {kernel-source-%name-%version,%buildroot{%kernel_src,%_bindir}}
install -m 0755 {create,extract}_compressed_fs cloop_suspend %buildroot%_bindir/
install -m 0644 compressed_loop.[ch] Makefile kernel-source-%name-%version/
tar -c kernel-source-%name-%version | bzip2 --best > %buildroot%kernel_src/kernel-source-%name-%version.tar.bz2
rm -rf kernel-source-%name-%version


%files -n kernel-source-%name
%kernel_src/*


%files utils
%doc README CHANGELOG debian/changelog.*
%_bindir/*


%changelog
* Thu Jan 08 2009 Led <led@altlinux.ru> 2.628-alt1
- 2.628-2

* Mon Oct 27 2008 Led <led@altlinux.ru> 2.625-alt2
- fixed build with gcc 4.3

* Sat Sep 27 2008 Led <led@altlinux.ru> 2.625-alt1
- 2.625-1
- added %name-2.625-alt.patch

* Sun Jan 27 2008 Led <led@altlinux.ru> 2.624-alt0.1
- 2.624-1

* Sun Jan 27 2008 Led <led@altlinux.ru> 2.622-alt0.1
- 2.622-1
- removed %name-2.06-7z.patch

* Sun Oct 07 2007 Led <led@altlinux.ru> 2.06-alt0.1
- initial build
