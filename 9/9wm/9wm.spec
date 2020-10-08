Name: 9wm
Version: 1.4.1
Release: alt2

Summary: Emulation of the Plan 9 window manager 8 1/2

License: MIT
Group: Emulators
Url: https://github.com/9wm/9wm

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar
Source1: 9wm.desktop
Source2: 9wm.wmsession

BuildRequires: libXext-devel libX11-devel
BuildRequires: /usr/bin/desktop-file-install
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

# future compatibility
desktop-file-install --dir=%buildroot%_datadir/xsessions/ %{SOURCE1}
# ALT specific
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/X11/wmsession.d/07%name

%files
%doc README.md CREDITS.md LICENSE.md
%_bindir/9wm
%_man1dir/9wm*
%_datadir/xsessions/9wm.desktop
%config %_sysconfdir/X11/wmsession.d/*

%changelog
* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt2
- NMU: added wmsession (closes: #38868)

* Tue Apr 07 2020 Maxim Knyazev <mattaku@altlinux.org> 1.4.1-alt1
- Initial build to Sisyphus

