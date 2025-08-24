# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_disable test
%define sover 1

Name: accel-config
Version: 4.1.9
Release: alt1
Summary: Intel Data Accelerators support
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/intel/idxd-config
Provides: idxd-config = %EVR
Requires: libaccel%sover = %EVR

ExclusiveArch: %ix86 x86_64

Source: %name-%version.tar
BuildRequires: asciidoc
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(uuid)
BuildRequires: xmlto
%if_enabled test
BuildRequires: libssl-devel
BuildRequires: zlib-devel
%endif

%description
Utility for controlling and configuring DSA (Intel Data Streaming
Accelerator Architecture) and IAA (Intel Analytics Accelerator
Architecture) sub-systems in the Linux kernel.

%package -n libaccel%sover
Summary: Development files for accel-config
Group: System/Libraries
License: LGPL-2.1-only

%description -n libaccel%sover
Utility library for controlling and configuring DSA (Intel Data
Streaming Accelerator Architecture) and IAA (Intel Analytics Accelerator
Architecture) sub-systems in the Linux kernel.

%package -n libaccel-devel
Summary: Development files for accel-config
License: LGPL-2.1-only
Group: Development/C
Requires: libaccel%sover = %EVR

%description -n libaccel-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
echo %version > version
./autogen.sh
%configure \
	%{subst_enable test}
%make_build

%install
%makeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%buildroot%_bindir/accel-config --version | grep -Fx '%version'

%files
%doc README.md licenses/accel-config-licenses LICENSE_GPL_2_0
%_bindir/accel-config
%_man1dir/accel-config*.1*
%_sysconfdir/%name
%if_enabled test
/usr/libexec/%name
%endif

%files -n libaccel%sover
%doc licenses/BSD-MIT licenses/CC0 licenses/libaccel-config-licenses
%doc accfg/lib/LICENSE_LGPL_2_1
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n libaccel-devel
%doc Documentation/COPYING licenses/libaccel-config-licenses
%_includedir/%name
%_libdir/lib%name.so
%_libdir/pkgconfig/lib%name.pc

%changelog
* Sun Aug 24 2025 Vitaly Chikunov <vt@altlinux.org> 4.1.9-alt1
- First import accel-config-v4.1.9 (2025-07-31). The tool requires kernel
  module idxd successfully loaded, which is hardware dependent.
