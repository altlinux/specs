Name:           xsensors
Version:        0.80
Release:        alt1
Summary:        An X11 interface to lm_sensors

Group:		Monitoring
License:        GPLv2+
Url:            https://github.com/Mystro256/xsensors
# VCS:		https://github.com/Mystro256/xsensors
Source:         %{name}-%{version}.tar

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires:  libgtk+2-devel
BuildRequires:  libsensors3-devel
Requires:	lm_sensors3

%description
Xsensors is a simple GUI program that allows you to read useful data
from the lm_sensors library in a digital read-out like fashion, such as
the temperature, voltage ratings and fan speeds of the running computer.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall_std
install -p -D -m 0644 xdg/%name.1 %buildroot/%_man1dir/%name.1  

%files
%doc AUTHORS COPYING README ChangeLog
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/theme.tiff
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1*

%changelog
* Tue Nov 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.80-alt1
- new version 0.80

* Wed Sep 28 2016 Andrey Cherepanov <cas@altlinux.org> 0.75-alt1
- New version

* Wed Mar 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.74-alt2
- Fix upstream problem with missing xsensors.xpm

* Wed Mar 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.74-alt1
- Build to Sisyphus
