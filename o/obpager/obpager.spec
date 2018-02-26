Name: obpager
Version: 1.8
Release: alt2

Summary: OBPager is a simple pager dockapp designed for use with netwm-compliant WM
License: GPL
Group: Graphical desktop/Other
Url: http://obpager.sourceforge.net/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz

Patch0: %name-1.8-alt-build.patch
Patch1: %name-1.8-alt-gcc43.patch

# Automatically added by buildreq on Wed Dec 03 2008 (-bi)
BuildRequires: gcc-c++ libX11-devel libXext-devel

%description
OBPager is a simple pager dockapp designed for use with netwm-compliant
window managers like OpenBox. OBPager shows a miniature representation of
the windows on a virtual desktop, as well as  the desktop number.  Clicking
on an OBPager requests a switch to that desktop by the window manager.

OBPager is very lightweight, requiring only glibc++ and Xlib; no Gnome or
KDE necessary, thank you very much. The general rationale is that if you 
are running something like OpenBox, you don't want all that extra baggage
anyway.
 
Unlike other pagers, OBPager is designed to manage a single virtual desktop,
so it is expected that you will run multiple instances of the applet-- one 
for each virtual desktop. This was done intentionally, since it looks 
better, IMNSHO, and it eats up what is otherwise wasted real estate in 
the dock/slit.  If you don't like that, then change it, or use a 
different pager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m755 %name %buildroot%_bindir/

%files
%doc README
%_bindir/%name

%changelog
* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.8-alt2
- fix build

* Fri Mar 17 2006 Igor Zubkov <icesik@altlinux.ru> 1.8-alt1
- Initial build for Sisyphus
