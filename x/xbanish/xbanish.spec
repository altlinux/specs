Name: 	  xbanish
Version:  1.8
Release:  alt1

Summary:  banish the mouse cursor when typing, show it again when the mouse moves
License:  BSD-3-Clause
Group:    System/X11
Url: 	  https://github.com/jcs/xbanish

Packager: Gordeev Mikhail <obirvalger@altlinux.org>

Source0:  %name-%version.tar
Source1:  LICENSE

#BuildRequires: libX11 libX11-locales libX11-devel
BuildRequires: libXt-devel libXfixes-devel libXi-devel

%description
xbanish hides the mouse cursor when you start typing, and shows it again when
the mouse cursor moves or a mouse button is pressed.  This is similar to
xterm's pointerMode setting, but xbanish works globally in the X11 session.

%prep
%setup
cp %SOURCE1 .

%build
%make_build

%install
install -D -m 755 %name %buildroot%_bindir/%name
install -D -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc README.md
%_bindir/*
%_man1dir/*

%changelog
* Thu May 04 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.8-alt1
- New version 1.8.

* Mon Apr 06 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.6-alt1
- new version 1.6

* Sat May 27 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.5-alt1
- Initial build in Sisyphus
