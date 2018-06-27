Name:	xye
Version:	0.12.1
Release:	alt3
Summary:	Puzzle game that reproduces and extends Kye
License:	GPL

Url:	http://xye.sourceforge.net
Group:	Games/Puzzles
Source:	http://heanet.dl.sourceforge.net/sourceforge/xye/%name-%version.tar.gz
Source1: xye.xpm
Source2: xye.desktop

Patch: xye-0.12.1-alt-glibc-2.16.patch
Patch1: xye-0.12.1-alt-gcc4.7.patch


BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_ttf-devel desktop-file-utils

Requires: fonts-ttf-dejavu

%description
Xye is a new, free version of the classic game Kye which also extends the game
adding more objects and gameplay options. Kye is a win32 game made by Colin Garbutt,
released in 1992. It was a Charity Shareware - you had to donate
to Save the Children in order to register and get a lot of more levels.
I consider Kye to be one of the best games ever, because it combines strategy,
reflexes and even speed. Yet it was a very simple game to understand the nice thing
was the way the objects interacted.

%prep
%setup -q
%patch -p2
%patch1 -p2

%build
%add_optflags -Wno-error=narrowing
%autoreconf
%configure 
%make_build

%install
make docdir=%_defaultdocdir/%name-%version DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_pixmapsdir/%name.xpm
desktop-file-install --dir %buildroot%_desktopdir %SOURCE2

# remove bundled fonts (see ALT 25355)
rm %buildroot%_datadir/%name/res/DejaVuSans.ttf %buildroot%_datadir/%name/res/DejaVuSans-Bold.ttf
ln -srf %buildroot%_datadir/fonts/ttf/dejavu/DejaVuSans.ttf %buildroot%_datadir/%name/res/DejaVuSans.ttf
ln -srf %buildroot%_datadir/fonts/ttf/dejavu/DejaVuSans-Bold.ttf %buildroot%_datadir/%name/res/DejaVuSans-Bold.ttf

%files
%doc NEWS AUTHORS COPYING INSTALL README 
%_bindir/%name
%_datadir/%name
#exclude %_datadir/%name/*.ttf
%_pixmapsdir/%name.xpm
%_desktopdir/*.desktop

%changelog
* Wed Jun 27 2018 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt3
- Remove bundled fonts (Closes: #25355).

* Fri Oct 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.12.1-alt2
- Fixed build with new toolchain.
- Added desktop menu entry.

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.1
- Fixed build with glibc 2.16

* Thu Mar 15 2012 Alex Karpov <karpov@altlinux.ru> 0.12.1-alt1
- new version

* Mon Nov 14 2011 Alex Karpov <karpov@altlinux.ru> 0.12.0-alt1
- new version

* Wed Oct 12 2011 Alex Karpov <karpov@altlinux.ru> 0.11.2-alt1
- new version

* Thu Aug 25 2011 Alex Karpov <karpov@altlinux.ru> 0.10.0-alt1
- new version

* Sun Apr 03 2011 Alex Karpov <karpov@altlinux.ru> 0.9.3-alt1.1
- exclude fonts from packaging (close #25355)

* Mon Feb 28 2011 Alex Karpov <karpov@altlinux.ru> 0.9.3-alt1
- new version

* Wed Dec 16 2009 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1
- new version

* Fri Aug 07 2009 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt1
- new version

* Thu Nov 27 2008 Alex Karpov <karpov@altlinux.ru> 0.8.0-alt0.2
- code cleanup for build with new toolchain

* Thu Jan 17 2008 Alex Karpov <karpov@altlinux.ru> 0.8.0-alt0.1
- 0.8.0

* Mon Jan 15 2007 Alex Karpov <karpov@altlinux.ru> 0.7.6.2-alt0.1
- picked from orphaned

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 0.7.5-alt0.1
- initial packaging for Sisyphus

