Name: man-pages-posix
Version: 2003a
Release: alt1

Summary: Manual pages about using POSIX system
License: Distributable
Group: Documentation
Url: http://www.kernel.org/pub/linux/docs/man-pages/man-pages-posix/
BuildArch: noarch

# ftp://ftp.kernel.org/pub/linux/docs/man-pages/man-pages-posix/man-pages-posix-2003-a.tar.xz
Source: %name-%version.tar

Provides: man-pages-POSIX = %version, man-pages-posix-2003-a = %version
Obsoletes: man-pages-POSIX < %version, man-pages-posix-2003-a < %version

Requires: man >= 1.5i2-alt4

%package devel
Summary: Manual pages about using a POSIX system for development
Group: Development/Documentation
Requires: %name = %version-%release

%description
This package contains manual pages for POSIX utilities (1p section).

%description devel
T his package contains manual pages describing the POSIX programming
interface, including these two sections:
  3p = POSIX library calls;
  7p = POSIX header files.

%prep
%setup

mv man0p man7p
rename .0p .7p man7p/*.0p
find -type f -print0 |
	xargs -r0 grep -EZl '\<(man0p|0p)\>' -- |
	xargs -r0 sed -i 's/\<man0p\>/man7p/g; s/\<0p\>/7p/g' --

%install
%makeinstall_std

%files
%_mandir/man1p
%doc POSIX-COPYRIGHT *.Announce *.lsm Changes

%files devel
%_mandir/man[37]p

%changelog
* Tue Jun 26 2012 Dmitry V. Levin <ldv@altlinux.org> 2003a-alt1
- Repackaged as man-pages-posix + man-pages-posix-devel.

* Thu Jun 19 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.2003-alt1
- repackaged source

* Tue Dec 21 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.01-alt1
- 2.01

* Mon Dec 20 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.00-alt1
- 2.00
- Minor changes in spec.

* Wed Oct 27 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.69-alt1
- sched_setaffinity.2, shmctl.2, killpg.3, proc.5 are new or have been updated.
- Headers added.
- Error sections were sorted.

* Sun May 23 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0-alt2
- Updated POSIX-COPYRIGHT

* Wed Feb 25 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.0-alt1
- POSIX manual pages moved into separate package due to licensing problem.
