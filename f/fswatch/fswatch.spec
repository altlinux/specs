# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fswatch
Version: 1.17.1
Release: alt1
Summary: A cross-platform file change monitor
License: GPL-3.0-or-later
Group: File tools
Url: https://emcrisostomo.github.io/fswatch/
Vcs: https://github.com/emcrisostomo/fswatch

Source: %name-%version.tar
BuildRequires: gcc-c++

%description
fswatch is a file change monitor that receives notifications when the
contents of the specified files or directories are modified.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--disable-shared \
	--disable-static \
	--disable-nls
%make_build

%install
%makeinstall_std

# devel
rm %buildroot%_libdir/libfswatch.a
rm -rf %buildroot%_pkgconfigdir
rm -rf %buildroot%_includedir
rm -rf %buildroot%_docdir

%check
PATH=%buildroot%_bindir:$PATH
fswatch --version |& grep -Fx '%name %version'
fswatch --list-monitors | grep -zw inotify_monitor
# fswatch_test.c does not work (fails to create a thread).
# make check does not run anything.
# Thus, a simple smoke test.
{ sleep 1; touch a-test; } & timeout 9 fswatch -v -1t . | grep -n a-test

%files
%define _customdocdir %_docdir/%name
%doc AUTHORS COPYING LICENSE-2.0.txt NEWS README.md README.linux
%_bindir/fswatch
%_man7dir/fswatch.7*

%changelog
* Sun Aug 25 2024 Vitaly Chikunov <vt@altlinux.org> 1.17.1-alt1
- First import 1.17.1-36-gba411e0 (2022-09-02).
- Build only the tool, not the devel package.
- Note: The upstream does not seem to have been maintained since 2022.
