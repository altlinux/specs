%def_with check

Name: e2tools
Version: 0.1.2
Release: alt1

Summary: Manipulate files in unmounted ext2/ext3 filesystems
License: GPL-2.0
Group: File tools

Url: https://e2tools.github.io/
Vcs: https://github.com/e2tools/e2tools

Source: %name-%version.tar

BuildRequires: e2fsprogs libcom_err-devel libe2fs-devel

%description
A simple set of utilities to read, write, and manipulate files in an
ext2/ext3 filesystem directly using the ext2fs library. This works

  - without root access
  - without the filesystem being mounted
  - without kernel ext2/ext3 support

The utilities are: e2cp e2ln e2ls e2mkdir e2mv e2rm e2tail

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc COPYING ChangeLog TODO AUTHORS
%_bindir/*
%_mandir/man?/*

%changelog
* Fri Jan 17 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1.2-alt1
- New version.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.16-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.16-alt2
- Fixed build, cleaned up specfile.
- Synced with Fedora e2tools-0.0.16-17.

* Sat Oct 13 2007 Kirill A. Shutemov <kas@altlinux.ru> 0.0.16-alt1
- First build for ALT Linux

* Mon Jul 31 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-5
- fix broken cast in rm.c:248 (exhibited on x86_64, but buggy everywhere)
  from Hans Ulrich Niedermann

* Mon Jul 17 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-4
- Introduced %%check

* Mon Jul 17 2006 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-3
- initial package for fedora extras

