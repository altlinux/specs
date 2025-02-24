%def_without check
Name: cgdb
Summary: Frontend for GDB
Version: 0.8.0
Release: alt1
Url: http://cgdb.github.io/
License: GPLv2
Group: Development/Debuggers
Source: %name-%version.tar.gz
Patch1: 0001-Fix-autoupdate.patch
Patch2: 0002-Fix-readlina-m4.patch

Requires: gdb

BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: libncursesw-devel
BuildRequires: libreadline-devel
BuildRequires: texinfo
BuildRequires: help2man
BuildRequires: dejagnu

%description
CGDB is a curses (terminal-based) interface to the GNU Debugger (GDB).
Its goal is to be lightweight and responsive; not encumbered with
unnecessary features.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
echo "%version" > VERSION

%build
%autoreconf
%configure
printf '#define HAVE_DEV_PTMX 1\n' >> config.h

%make_build

%install
%makeinstall_std

%files
%doc README.md NEWS *.txt FAQ
%_bindir/*
%_datadir/%name
%_infodir/*

%if_with check
%check
make check
%endif

%changelog
* Mon Feb 24 2025 Fr. Br. George <george@altlinux.org> 0.8.0-alt1
- New version (0.8.0).

* Tue Feb 05 2019 Alexey Gladkov <legion@altlinux.ru> 0.7.0-alt1
- New version (0.7.0).

* Thu Dec 10 2015 Alexey Gladkov <legion@altlinux.ru> 0.6.8-alt1
- New version (0.6.8).

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.4-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Dec 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt3
- Remove obsolete macros.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt2
- Fix requires.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux Sisyphus
