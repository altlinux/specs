Name: lsdvd
Version: 0.17
Release: alt1

Summary: list contents of DVD disks
Group: Video
License: GPLv2
Url: https://sourceforge.net/projects/lsdvd/

# VCS: git://git.code.sf.net/p/lsdvd/git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libdvdread-devel >= 4.1.3

%description
lsdvd is a program that reads information about a DVD and outputs it to
the console in various formats: human-readable, perl, python, ruby and
XML.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README

%changelog
* Wed Feb 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- pre0.18 from new upstream git (ALT #31771)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.16-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sat Sep 19 2009 Terechkov Evgenii <evg@altlinux.ru> 0.16-alt3
- Spec translation removed
- Rebuild with new libdvdread

* Sat Jun 23 2007 Terechkov Evgenii <evg@altlinux.ru> 0.16-alt2
- Spec cleanup

* Sat Oct  7 2006 Terechkov Evgenii <evg@altlinux.ru> 0.16-alt1
- take from orphaned
- 0.16 + SF patches (0-edited, 1-unmodified)
- spec cleanups

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- NMU: fix charset in descr/summary (bug #5116)
- remove Provides:
- remove INSTALL from doc

* Tue Jan 24 2006 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt0.1
- NMU: new version
- remove COPYING, cleanup spec

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.10-alt1.1
- Rebuilt with libdvdread.so.3.

* Mon Oct 06 2003 Egor S. Orlov <oes@altlinux.ru> 0.10-alt1
- New version

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.2
- Added URL

* Fri Aug 01 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.1
- Initial spec for ALT

