# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xsecurelock
Version: 1.8.0
Release: alt1
URL: https://github.com/google/xsecurelock
Summary: X11 screen lock utility with security in mind
License: Apache-2.0
Group: System/X11

# Optional savers and examples.
%filter_from_requires /\b\(htpasswd\|mplayer\|mpv\|grep\|coreutils\|sh\)\b/d

Source: %name-%version.tar

BuildRequires: fontconfig-devel
BuildRequires: libbsd-devel
BuildRequires: libpam-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: pandoc

%description
XSecureLock is an X11 screen lock utility designed with the primary
goal of security.

Screen lock utilities are widespread. However, in the past they often
had security issues regarding authentication bypass (a crashing screen
locker would unlock the screen), information disclosure (notifications
may appear on top of the screen saver), or sometimes even worse.

In XSecureLock, security is achieved using a modular design to avoid
the usual pitfalls of screen locking utility design on X11.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--with-pam-service-name=system-auth \
	--with-dpms \
	--with-fontconfig \
	--with-htpasswd=/usr/bin/htpasswd \
	--with-libbsd \
	--with-mplayer=/usr/bin/mplayer \
	--with-mpv=/usr/bin/mpv \
	--with-pam \
	--with-pandoc \
	--with-xfixes \
	--with-xft \
	--with-xkb \
	--with-xscreensaver=/usr/libexec/xscreensaver \
	--with-xss \

%make_build GIT_VERSION=v%version

%install
%makeinstall_std

%files
%_bindir/xsecurelock
%attr(2711,root,chkpwd) %_libexecdir/xsecurelock/authproto_pam
%_libexecdir/xsecurelock
%_defaultdocdir/xsecurelock
%_man1dir/xsecurelock.1*

%changelog
* Fri Sep 16 2022 Vitaly Chikunov <vt@altlinux.org> 1.8.0-alt1
- Update to v1.8.0 (2022-09-14).

* Mon Jul 05 2021 Vitaly Chikunov <vt@altlinux.org> 1.7.0-alt1
- Update to v1.7.0 (2020-01-15).

* Fri Aug 01 2014 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
