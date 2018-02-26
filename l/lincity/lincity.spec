Name: lincity
Version: 1.12.1
Release: alt2.1

Summary: SimCity clone
Group: Games/Strategy
License: GPL
URL: http://lincity.sourceforge.net/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: imake libXext-devel libXt-devel xorg-cf-files

%description
Lincity is a well designed and easy to play SimCity clone. Besides the
game itself it provides an editor for easily creating new levels and
obstacles.

%prep
%setup -q

%build
%configure --bindir=%_gamesbindir/
%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=LinCity I
GenericName=LinCity is CimCity clone
Comment=%{summary}
Icon=%{name}
Exec=%_gamesbindir/xlincity
Terminal=false
Categories=Game;StrategyGame;
EOF

%find_lang %name

%files -f %name.lang
%doc README CHANGES Acknowledgements TODO
%_gamesbindir/*
%dir %_datadir/lincity/
%_datadir/lincity/
%_man6dir/*
%_desktopdir/%{name}.desktop

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2.1
- NMU: converted debian menu to freedesktop

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.12.1-alt2
- apply patch from repocop
- buildreq

* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 1.12.1-alt1.1
- rebuild with new gcc flags (-Wl,--as-needed)

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Sun Nov 27 2005 Igor Zubkov <icesik@altlinux.ru> 1.12.0-alt1
- Initial build for Sisyphus
