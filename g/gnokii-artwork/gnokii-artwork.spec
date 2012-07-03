# vim: set ft=spec: -*- rpm-spec -*-

Name: gnokii-artwork
Version: 1.1
Release: alt1

Summary: Artwork for xgnokii package
Group: Communications
License: GPL

Packager: Sir Raorn <raorn@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
This is the artwork package for xgnokii. You will find here Nokia phone
pixmaps for use for xgnokii modules:
 - keyboard simulation
 - operator logo preview

%prep
%setup
%patch -p1

%install
%make_install \
	DESTDIR=%buildroot \
	INSTALL_DATA="%__install -p" \
	xgnokiidir=%_datadir/xgnokii \
	install

%files
%doc README
%dir %_datadir/xgnokii
%_datadir/xgnokii/*

%changelog
* Wed Aug 01 2007 Sir Raorn <raorn@altlinux.ru> 1.1-alt1
- Initial build

