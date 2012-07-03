Name: lsdvd
Version: 0.16
Release: alt3

Summary: list contents of DVD disks

License: GPL
Group: Video
Url: http://untrepid.com/lsdvd

Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: %name-0.16-configure.patch
Patch1: %name-0.16-cell_sizes.patch

# Automatically added by buildreq on Sat Oct 07 2006
BuildRequires: libdvdread-devel

%description
List contents of DVD disks. May be used by AcidRip, Ogle or
standalone.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --prefix=%buildroot
%make_build

%install
mkdir -p %buildroot/%_bindir
%makeinstall

%files
%_bindir/*
%_man1dir/%name.1*

%doc AUTHORS NEWS README

%changelog
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

