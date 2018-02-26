Name: gpicview
Version: 0.2.2
Release: alt1

Summary: A simple and fast image viewer with low memory usage
License: GPLv2+
Group: Graphics

Url: http://lxde.sourceforge.net/gpicview/
Source: http://downloads.sourceforge.net/lxde/gpicview-%version.tar.gz

# gpicview may use invocation of xdg-mime from xdg-utils to become default
# viewer for supported image formats
Requires: xdg-utils

BuildRequires: intltool libgtk+2-devel libjpeg-devel

%description
GPicView is a simple and fast image viewer with low memory usage. It's aimed at
replacing the default image viewer of current desktop systems. Fast startup, low
memory usage, and a simple user interface make it a good choice for a default
viewer. It is extremely lightweight and fast with low memory usage, has a simple
and intuitive interface, minimal library dependencies (only GTK+ is used), and
doesn't require any specific desktop environment. It was inspired by the Windows
XP image viewer and gimmage.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
install -pD -m644 gpicview.png %buildroot%_liconsdir/gpicview.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/gpicview
%_pixmapsdir/*
%_liconsdir/*
%_desktopdir/*

%changelog
* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- new version (ALT #26197)
- removed obsolete gpicview-0.2.1-desktop.patch

* Mon Jan 10 2011 Victor Forsiuk <force@altlinux.org> 0.2.1-alt2
- Add russian and ukrainian translations to desktop file (closes: #24889).

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jun 22 2009 Victor Forsyuk <force@altlinux.org> 0.2.0-alt1
- 0.2.0

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 0.1.11-alt1
- 0.1.11

* Fri Nov 21 2008 Victor Forsyuk <force@altlinux.org> 0.1.10-alt2
- Fix typo in russian .po.

* Fri Sep 26 2008 Victor Forsyuk <force@altlinux.org> 0.1.10-alt1
- 0.1.10
- Fixed CVE-2008-3904, CVE-2008-3791.

* Fri Mar 21 2008 Victor Forsyuk <force@altlinux.org> 0.1.9-alt1
- 0.1.9
- Fixed packaging mistakes spotted by repocop.

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 0.1.7-alt1
- 0.1.7

* Tue Nov 13 2007 Victor Forsyuk <force@altlinux.org> 0.1.6-alt1
- 0.1.6

* Fri Sep 14 2007 Victor Forsyuk <force@altlinux.org> 0.1.5-alt1
- Initial build.
