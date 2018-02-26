Name: plymouth-theme-xbmc
Version: 1.0
Release: alt1

Summary: Graphical Boot Animation theme for XBMC
License: GPLv2+
Group: System/Base
Url: http://xbmc.org/

Requires: plymouth plymouth-plugin-script
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains XBMC boot splash theme for Plymouth.

%prep
%setup

%install
mkdir -p %buildroot%_datadir
cp -a plymouth %buildroot%_datadir

%files
%_datadir/plymouth/themes/xbmc-logo/*.png
%_datadir/plymouth/themes/xbmc-logo/xbmc-logo.script
%_datadir/plymouth/themes/xbmc-logo/xbmc-logo.plymouth

%changelog
* Fri Nov 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- Initial
