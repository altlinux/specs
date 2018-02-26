%def_enable static

Name: speex
Version: 1.2
%define prerel pre1
Release: alt0.5.pre1
Summary: An open-source, patent-free speech codec
License: BSD-style
Group: Sound
Url: http://www.speex.org
%define pkgdocdir %_docdir/%name-%version
Packager: Denis Smirnov <mithraen@altlinux.ru>

# %url/download/%name-%version%prerel.tar.bz2
Source: %name-%version.tar
Requires: lib%name = %version-%release

BuildRequires: libogg-devel >= 1.1

%description
Speex is a patent-free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n lib%name
Summary: Speex shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library required by Speex-based software.

%package -n lib%name-devel
Summary: Speex development file
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains heade files required to develop
Speex-based softwae.

%package -n lib%name-devel-doc
Summary: Speex development documentation
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
The Speex programming manual in PDF format.

%if_enabled static
%package -n lib%name-devel-static
Summary: Speex static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static library required to develop
Speex-based software.
%endif

%prep
%setup

%build
%add_optflags -DRELEASE
%autoreconf -fisv
%configure \
%ifarch pentium4 x86_64 athlon_xp k8 nocona
    --enable-sse \
%endif
%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot docdir=%pkgdocdir install
install -m 0644 COPYING AUTHORS NEWS README %buildroot%pkgdocdir/

%files
%_bindir/*
%_man1dir/*
%dir %pkgdocdir
%pkgdocdir/COPYING
%pkgdocdir/AUTHORS
%pkgdocdir/NEWS
%pkgdocdir/README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/aclocal/*
%_includedir/*

%files -n lib%name-devel-doc
%dir %pkgdocdir
%pkgdocdir/manual.pdf

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.5.pre1
- fix build

* Fri Mar 25 2011 Alexey Tourbin <at@altlinux.ru> 1.2-alt0.4.pre1.2
- rebuilt for debuginfo
- made libspeex-devel-doc noarch

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.4.pre1.1
- auto rebuild

* Sun Jan 03 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.4.pre1
- 1.2pre1 (ALT #22661)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.3.beta3.2
- cleanup spec

* Mon May 12 2008 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.2.beta3.2
- CVE-2008-1686
- 1.2beta3.2
- enabled SSE for athlon_xp arch (thanks to led@)
- cleaned up spec (thanks to led@)

* Mon Oct 16 2006 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt0.1.beta1
- Speed improvments
- Critical bugfixes (instability problem with pure sinusoids has been fixed)

* Fri Apr 14 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.12-alt1
- Release 1.1.12

* Sat Dec 17 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.11.1-alt1
- Updated to 1.1.11.1
- Separated manual.pdf to libspeex-devel-doc
- Disabled static by default
- Do autoreconf
- Spec cleanup

* Wed May 25 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Sun Mar 20 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Tue May 18 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Thu Feb 05 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.4-alt2
- Fixed BuildRequieres.

* Mon Feb 02 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Dec 09 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1.3-alt1
- *.la files removed.

* Sat Sep 20 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1-alt1
- 1.1

* Fri Jun 06 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Mar 26 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt1
- 1.0

* Mon Feb 10 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt0.8rc2
- 1.0rc2
- fixed permissions on docs

* Mon Dec 23 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt0.2beta4
- 1.0beta4

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0-alt0.1beta3
- First build for Sisyphus.
