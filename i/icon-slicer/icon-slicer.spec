Name: icon-slicer
Version: 0.3
Release: alt2
Summary: Utility for icon theme generation
License: MIT
Group: Development/Tools
Url: http://www.freedesktop.org/software/icon-slicer/
Packager: Sugar Development Team <sugar@packages.altlinux.org>

Source: http://www.freedesktop.org/software/icon-slicer/releases/icon-slicer-0.3.tar.gz

Patch: icon-slicer-0.3-sugar-297.patch

BuildPreReq: pkg-config
BuildPreReq: xcursorgen
BuildPreReq: libgtk+2-devel
BuildPreReq: libpopt-devel

%description
Utility for generating icon themes and libXcursor cursor themes.

%prep
%setup -v
%patch -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/%name
%doc AUTHORS ChangeLog README TODO

%changelog
* Sat May 09 2009 Aleksey Lim <alsroot@altlinux.org> 0.3-alt2
- fix SL#297

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 0.3-alt1
- first build for ALT Linux Sisyphus
