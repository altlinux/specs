Name: icewm-theme-darkt
Version: 0.1.0
Release: alt1

License: GPL
Group: Graphical desktop/Icewm
URL: http://icewmdarkt.berlios.de
Summary: A theme for IceWM inspired by the Silver Vista, IceVista and VistaBlack themes
BuildArch: noarch

Requires: design-icewm >= 1.0-alt6

Source: http://download.berlios.de/icewmdarkt/darkt-0.1.0.tar.gz

%description
These themes were inspired by the Silver Vista, IceVista and VistaBlack themes.
They have a look based on gradients, rounded borders and shaped windows's decorations.
Currently there are two themes: DarkT and DarkT II.

%prep

%install
/bin/mkdir -p %buildroot%_x11x11dir/icewm/themes/
/bin/tar xzf %SOURCE0 -C %buildroot%_x11x11dir/icewm/themes/

# don't use nonexistent background image
/bin/sed -i 's|DesktopBackgroundImage="bgimage.png"|# DesktopBackgroundImage=""|' %buildroot%_x11x11dir/icewm/themes/*/default.theme
# show default network status
/bin/sed -i 's|NetworkStatusDevice|# NetworkStatusDevice|' %buildroot%_x11x11dir/icewm/themes/*/default.theme
# fix font name
/bin/sed -i 's|-koi8-r|-*-*|g' %buildroot%_x11x11dir/icewm/themes/*/default.theme

/bin/find %buildroot%_x11x11dir/icewm/themes -type f -print0 | 
	xargs -r0 chmod 0444
/bin/find %buildroot%_x11x11dir/icewm/themes -type d -print0 | 
	xargs -r0 chmod 0755

%files
%_x11x11dir/icewm/themes/*

%changelog
* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 0.1.0-alt1
- initial build for ALTLinux
