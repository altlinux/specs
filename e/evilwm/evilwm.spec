Name: evilwm
Version: 1.0.1
Release: alt1

Summary: a minimalist window manager derived from aewm
License: BSD-like
Group: Graphical desktop/Other
Url: http://www.6809.org.uk/evilwm/
Packager: Alex V. Myltsev <avm@altlinux.ru>

%def_without terminal_solution

Source: %url/%name-%version.tar.gz
Patch0: evilwm-0.99.24-alt-center-placement.patch
Patch1: evilwm-1.0.0-alt-supermini.patch

# Added by buildreq2 on Fri Mar 31 2006
BuildRequires: libXext-devel libXrandr-devel libXrender-devel

%description
%name is a minimalist window manager for the X Window System.

%name features include:
* No window decorations apart from a simple 1 pixel border.
* No icons.
* Good keyboard control, including repositioning and maximise toggles.
* Virtual desktops.

%prep
%setup

%if_with terminal_solution
# center-placement.patch
%patch0 -p1
# supermini.patch
%patch1 -p2
%endif

%build
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Tue Mar 22 2011 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- New version

* Tue Mar 22 2011 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt2
- Updated build dependencies

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1.1
- NMU:
  * updated build dependencies

* Tue Jul 10 2007 Alex V. Myltsev <avm@altlinux.ru> 1.0.0-alt1
- New version: basic XRandr support, fixes re maximizing and snapping.

* Thu Jul 20 2006 Alex V. Myltsev <avm@altlinux.ru> 0.99.25-alt1
- New version: bug fixes re virtual desktops and keyboard grabs.

* Fri Mar 31 2006 Alex V. Myltsev <avm@altlinux.ru> 0.99.24-alt1
- Initial build for Sisyphus

