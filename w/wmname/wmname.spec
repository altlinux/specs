Name: wmname
Version: 0.1
Release: alt2
Summary: prints/sets the window manager name property of the root window
License: MIT/X
Group: Graphical desktop/Other
Url: http://tools.suckless.org/wmname
Packager: Denis Klimov <zver@altlinux.org>
Source: %name-%version.tar

BuildRequires: libX11-devel

%description
wmname prints/sets the window manager name property of the root window
similar to how hostname(1) behaves.
wmname is a nice utility to fix problems with JDK versions and other
broken programs assuming a reparenting window manager for instance.

%prep
%setup

%build
%make_build DESTDIR=%buildroot PREFIX=/usr

%install
%makeinstall DESTDIR=%buildroot PREFIX=/usr

%files
%doc README
%_bindir/wmname

%changelog
* Tue Jul 27 2010 Denis Klimov <zver@altlinux.org> 0.1-alt2
- add BuildRequires for libX11-devel

* Mon Jul 26 2010 Denis Klimov <zver@altlinux.org> 0.1-alt1
- Initial build for ALT Linux

