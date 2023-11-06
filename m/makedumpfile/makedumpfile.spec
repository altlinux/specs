# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:    makedumpfile
Version: 1.7.4
Release: alt1
Summary: Make vmcore smaller by filtering and compressing pages
Group:   System/Kernel and hardware
License: GPL-2.0-only
Url:     https://github.com/makedumpfile/makedumpfile
# Wiki:  https://github.com/makedumpfile/makedumpfile/wiki

Source: %name-%version.tar

BuildRequires: bzlib-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: libeppic-devel >= 4.0.0.13.gdc60e00-alt3
BuildRequires: liblzma-devel
BuildRequires: liblzo2-devel
BuildRequires: libncurses-devel
BuildRequires: libsnappy-devel
BuildRequires: libzstd-devel
BuildRequires: perl-Math-BigInt
BuildRequires: zlib-devel

%description
The makedumpfile can make a Linux crash dump smaller.
- Exclude unnecessary pages for crash analysis
- Compress dump data with zlib, lzo or snappy
- Multi-thread processing

%prep
%setup

%build
export CFLAGS="%optflags"
export USELZO=on
export USEZSTD=on
export USESNAPPY=on
export LINKTYPE=dynamic
%make_build
%make_build eppic_makedumpfile.so

%install
%makeinstall_std
install -Dm0755 eppic_makedumpfile.so %buildroot%_libdir/%name/eppic_makedumpfile.so

%files
%doc COPYING README IMPLEMENTATION
%_sbindir/makedumpfile
%_sbindir/makedumpfile-R.pl
%_man5dir/makedumpfile.conf.5.xz
%_man8dir/makedumpfile.8.xz
%_datadir/makedumpfile
%_libdir/%name

%changelog
* Mon Nov 06 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.4-alt1
- Update to 1.7.4 (2023-11-06).

* Tue Apr 25 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.3-alt1
- Update to 1.7.3 (2023-04-25).

* Fri Oct 21 2022 Vitaly Chikunov <vt@altlinux.org> 1.7.2-alt1
- Update to 1.7.2 (2022-10-20).

* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 1.7.1-alt1
- Update to 1.7.1 (2022-04-18).

* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.6.7.0.10.gc9e0785-alt1
- First import of Released-1-6-7-10-gc9e0785. (Experimental).
