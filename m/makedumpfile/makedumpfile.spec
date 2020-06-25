# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name:    makedumpfile
Version: 1.6.7.0.10.gc9e0785
Release: alt1
Summary: Make a small dumpfile of kdump (Linux crash dump)
Group:   System/Kernel and hardware
License: GPL-2.0-only
Url:     https://github.com/makedumpfile/makedumpfile
Vcs:     https://github.com/makedumpfile/makedumpfile.git
# Wiki:  https://github.com/makedumpfile/makedumpfile/wiki

Source: %name-%version.tar

BuildRequires: bzlib-devel
BuildRequires: libdw-devel
BuildRequires: libelf-devel
BuildRequires: liblzma-devel
BuildRequires: liblzo2-devel
BuildRequires: libncurses-devel
BuildRequires: libsnappy-devel
BuildRequires: perl-Math-BigInt
BuildRequires: zlib-devel

%description
Exclude unnecessary pages for crash analysis
Compress dump data with zlib, lzo or snappy
Multi-thread processing

(Experimental.)

%prep
%setup

%build
export USELZO=on
export USESNAPPY=on
export LINKTYPE=dynamic
%make_build

%install
%makeinstall_std

%files
%doc COPYING README IMPLEMENTATION
/etc/makedumpfile.conf.sample
%_sbindir/makedumpfile
%_sbindir/makedumpfile-R.pl
%_man5dir/makedumpfile.conf.5.xz
%_man8dir/makedumpfile.8.xz
%_datadir/makedumpfile*

%changelog
* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.6.7.0.10.gc9e0785-alt1
- First import of Released-1-6-7-10-gc9e0785. (Experimental).

