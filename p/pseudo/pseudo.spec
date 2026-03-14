# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lfs=relaxed

Name: pseudo
Version: 1.9.3
Release: alt1
Summary: An analogue to sudo and an alternative to fakeroot (experimental)
License: LGPL-2.1-only
Group: System/Configuration/Other
Url: https://git.yoctoproject.org/pseudo

Source: %name-%version.tar
BuildRequires: libattr-devel
BuildRequires: libsqlite3-devel
BuildRequires: python3
%{?!_without_check:%{?!_disable_check:
BuildRequires: acl
BuildRequires: attr
BuildRequires: /proc
BuildRequires: tcl
}}

%description
The pseudo utility offers a way to run commands in a virtualized "root"
environment, allowing ordinary users to run commands which give the
illusion of creating device nodes, changing file ownership, and otherwise
doing things necessary for creating distribution packages or filesystems.

NOTE: Do not expect it to work flawlessly due to its Yocto-centeredness.

%prep
%setup

%build
# LFS flags should not be used.
./configure \
	--cflags="%optflags" \
	--enable-memory-db \
	--enable-xattr \
	--enable-xattrdb \
	--libdir=%_libdir/%name \
	--prefix=%prefix \
	--without-rpath \
	%nil
%make_build
sed -e 's,@LIBDIR@,%_libdir,g' debian/fakeroot-pseudo.in > debian/fakeroot-pseudo

%install
%makeinstall_std
install -Dpm644 pseudo.1 -t %buildroot%_man1dir
install -Dpm644 pseudolog.1 -t %buildroot%_man1dir
install -Dp debian/fakeroot-pseudo -t %buildroot%_bindir
install -Dp debian/fakeroot-pseudo.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/pseudo -V | grep -Fx '%name version %version'
%make_build test-verbose |& tee test.log
%ifarch %ix86
# debug_logfile: fd 2
# pid 2032582 [parent 2032581], doing new pid setup and server start
# Setup complete, sending SIGUSR1 to pid 2032581.
# test-cp-setuid: Failed.
failed=1
%else
failed=0
%endif
grep -Px "$failed/\d+ test\(s\) failed\." test.log

%files
%define _customdocdir %_docdir/%name
%doc COPYING ChangeLog.txt README SECURITY.md
%_bindir/pseudo
%_bindir/pseudodb
%_bindir/pseudolog
%_bindir/fakeroot-pseudo
%_libdir/%name
%_man1dir/pseudo*.1*
%_man1dir/fakeroot-pseudo*.1*

%changelog
* Sat Mar 14 2026 Vitaly Chikunov <vt@altlinux.org> 1.9.3-alt1
- Experimental import pseudo-1.9.3-3-g43cbd8f (2026-02-17).
  This is experimental due to apparent incompatibility of the tool designed for
  Yocto with the normal Linux systems.
