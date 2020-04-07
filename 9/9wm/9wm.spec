Name: 9wm
Version: 1.4.1
Release: alt1

Summary: Emulation of the Plan 9 window manager 8 1/2

License: MIT
Group: Emulators
Url: https://github.com/9wm/9wm

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildRequires: libXext-devel
BuildRequires: libX11-devel
Requires: xterm

%description
9wm is an X window manager which attempts to emulate the Plan 9 window
manager 8-1/2 as far as possible within the constraints imposed by X.
It provides a simple yet comfortable user interface, without garish
decorations or title-bars. Or icons.  And it's click-to-type.

%prep
%setup

%build
%make_build

%install
%makeinstall_std install.man

%files
%doc README.md CREDITS.md LICENSE.md
%_bindir/9wm
%_man1dir/*

%changelog
* Tue Apr 07 2020 Maxim Knyazev <mattaku@altlinux.org> 1.4.1-alt1
- Initial build to Sisyphus

