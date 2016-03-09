Name: slock
Version: 1.2
Release: alt1

Summary: Simple X display locker

License: MIT/X11
Group: System/X11
Url: http://tools.suckless.org/slock/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name-%version.tar.gz

BuildRequires: libX11-devel libXext-devel

%description
Simple X display locker.

%prep
%setup

%build
make

%install
make PREFIX=%buildroot%_prefix install

%files
%_bindir/*


%changelog
* Mon Dec 07 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2-alt1
- Initial build.
