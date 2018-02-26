
Name:	xye
Version:	0.12.1
Release:	alt1
Summary:	Puzzle game that reproduces and extends Kye
License:	GPL
Packager: Alex Karpov <karpov@altlinux.ru>

Url:	http://xye.sourceforge.net
Group:	Games/Puzzles
Source:	http://heanet.dl.sourceforge.net/sourceforge/xye/%name-%version.tar.gz


# Automatically added by buildreq on Sun Feb 03 2008
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_ttf-devel

Requires: fonts-ttf-dejavu

%description
Xye is a new, free version of the classic game Kye which also extends the game adding more objects and gameplay options

Kye is a win32 game made by Colin Garbutt, released in 1992. It was a Charity Shareware - you had to donate to Save the Children in order to register and get a lot of more levels.

I consider Kye to be one of the best games ever, because it combines strategy, reflexes and even speed.

Yet it was a very simple game to understand the nice thing was the way the objects interacted.

%prep
%setup -q

%build
autoreconf -fisv
%configure 
%make_build

%install
make docdir=%_defaultdocdir/%name-%version DESTDIR=%buildroot install

%files
%doc NEWS AUTHORS COPYING INSTALL README 
%_bindir/%name
%_datadir/%name
#exclude %_datadir/%name/*.ttf

%changelog
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

