Name: moka-icon-theme
Version: 5.3.5
Release: alt1
Summary: Moka icon theme
Group: Graphical desktop/GNOME
License: GPL-3.0+
Url: https://github.com/snwh/moka-icon-theme
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains the Moka icon theme.

%prep
%setup

%build
%define _configure_script ./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING LICENSE_* README.md
%_datadir/icons/Moka

%changelog
* Mon Mar 27 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.3.5-alt1
- first build for ALT Linux
