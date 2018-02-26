Name: faketime
Version: 0.2.2
Release: alt1

Summary: Execute program with changed notion of system time
License: GPL
Group: Development/Other
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: faketime-%version.tar
Source1: gnulib.tar

BuildPreReq: help2man

%description
The faketime utility helps to execute programs with changed notion of
system time.

%prep
%setup -q -a1
./gnulib.sh gnulib
sed -i 's/return (/return (int)(/' lib/timespec.h

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall
rm %buildroot%_libdir/*.la

%files
%_bindir/*
%_libdir/*.so
%_man1dir/*

%changelog
* Tue Oct 28 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Fixed build with fresh gcc.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- Updated gnulib.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Changed option processing to stop after the first non-option argument (at).
- Fixed to build with current gnulib.

* Thu Dec 15 2005 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
