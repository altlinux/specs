Name: gif2png
Version: 2.5.1
Release: alt1.2.1

Summary: Tools for converting files from using GIFs to using PNGs
Group: Graphics
License: MIT-like
Url: http://catb.org/~esr/gif2png/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %url/gif2png-%version.tar.bz2
Patch1: gif2png-2.4.6-alt-web2png.patch
Patch2: gif2png-2.5.1-deb-comment.patch
Patch3: gif2png-2.5.1-deb-man.patch

# Automatically added by buildreq on Mon Oct 21 2002
BuildRequires: libpng-devel zlib-devel

%description
The gif2png program converts files from the patent-encumbered Graphic
Interchange Format to Portable Network Graphics.

This distribution also supplies web2png, a Python front end for
gif2png which automagically converts entire web hierarchies (the
graphics files themselves and references to them in web pages).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_mandir/man?/*
%doc AUTHORS COPYING README NEWS

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt1.2.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.5.1-alt1.1
- Rebuilt with python-2.5.

* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 2.5.1-alt1
- Updated to 2.5.1.
- Imported patches from Debian gif2png_2.5.1-3 package.

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.6-alt1
- 2.4.6

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.4-alt1
- 2.4.4

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Rebuilt with libpng.so.3

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.1-ipl2
- Rebuilt with python-2.1

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.1-ipl1
- 2.4.1

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.0-ipl1
- Initial revision.
