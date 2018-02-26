Name: pangzero
Version: 1.3
Release: alt1

Summary: Clone of Super Pang, a fast-paced action game
License: GPLv2
Group: Games/Arcade
Url: http://apocalypse.rulez.org/pangzero

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 25 2008
BuildRequires: perl-SDL

%description
Pang Zero is a clone of Super Pang, a fast-paced action game that involves
popping balloons with a harpoon. The intention of our effort is to create a
fun, open-source game that many (currently up to 6) people can play
together.

For more info, please visit our website at
http://apocalypse.rulez.org/pangzero

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%dir %_datadir/pangzero/
%_datadir/pangzero/

%changelog
* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 1.3-alt1
- 0.13 -> 1.3
- buildreq
- add Url

* Thu Aug 31 2006 Igor Zubkov <icesik@altlinux.org> 0.13-alt1
- Initial build for Sisyphus
