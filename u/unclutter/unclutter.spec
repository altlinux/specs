Name: unclutter
Version: 8
Release: alt1

Summary: Hides X11 cursor when idle
License: PD
Group: System/X11
Url: ftp://export.lcs.mit.edu/contrib/utilities/
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

# Automatically added by buildreq on Sun Sep 27 2009 (-bi)
BuildRequires: libX11-devel

%description
unclutter hides your X mouse cursor when you don't need it, to prevent
it from getting in the way. You have only to move the mouse to restore
the mouse cursor.

%prep
%setup

%build
make

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
make install install.man BINDIR=%buildroot%_bindir MANDIR=%buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/*

%changelog
* Sun Sep 27 2009 Terechkov Evgenii <evg@altlinux.ru> 8-alt1
- Initial build for ALT Linux Sisyphus
