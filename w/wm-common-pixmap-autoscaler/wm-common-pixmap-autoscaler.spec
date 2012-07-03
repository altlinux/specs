Summary: Support for pixmap autoscaling for ancient Window Managers.
Name: wm-common-pixmap-autoscaler
Version: 1.0
Release: alt1
License: GPL2+
Group: Graphical desktop/Other
Packager: Igor Vlasenko <viy@altlinux.ru>
URL: http://wiki.altlinux.org/WMPackagingPolicy
BuildArch: noarch
Source0: %name-%version.tar

# /usr/bin/convert
Requires(pre): ImageMagick

%description
wm-common-pixmap-autoscaler is a helper tool for ancient Window Managers
that support only fixed size pixmaps in menu.

wm-common-pixmap-autoscaler scales pixmaps automatically to 
16x16 and 32x32 using 48x48 pixmaps in standard locations.
Scaled pixmaps are cached in /var/cache/icons/ hierarchy.

ALT Linux Icons Packaging policy does not require packages to 
have 16x16 and 32x32 pixmaps. Instead, the Window Managers
that require such pixmaps should depend on wm-common-pixmap-autoscaler
instead.

%prep
%setup

%build

%install
install -pD -m755 %name.sh %buildroot%_sbindir/%name
install -pD -m755 %name.uninstall.sh %buildroot%_sbindir/%name.uninstall
install -pD -m755 %name.filetrigger %buildroot%_rpmlibdir/%name.filetrigger

install -d -m755 %buildroot/var/cache/icons/hicolor/{48x48,32x32,16x16}/apps

%post
%_sbindir/%name ||:

%preun
[ $1 = 0 ] && %_sbindir/%name.uninstall ||:

%files 
%_sbindir/%name
%_sbindir/%name.uninstall
%_rpmlibdir/%name.filetrigger
/var/cache/icons

%changelog
* Fri Mar 06 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first version
