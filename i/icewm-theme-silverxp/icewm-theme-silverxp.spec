Name: icewm-theme-silverxp
Version: 1.2.17
Release: alt4

License: GPL
Group: Graphical desktop/Icewm
URL: http://sourceforge.net/projects/icewmsilverxp/
Summary: A theme for IceWM inspired by the Silver theme of WindowsXP
BuildArch: noarch

Requires: design-icewm >= 1.0-alt6

%define theme SilverXP-%version-single-1

Source: http://prdownloads.sourceforge.net/icewmsilverxp/%theme.tar.bz2

%description
A theme for IceWM window manager inspired by the Silver theme of WindowsXP.
The theme have a very nice look based on gradients and shaped windows
decorations.

%prep

%install
/bin/mkdir -p %buildroot%_x11x11dir/icewm
/bin/tar xjf %SOURCE0 -C %buildroot%_x11x11dir/
/bin/rm -rf %buildroot%_x11x11dir/icewm/themes/*/{README*,Linux,FreeBSD}
/bin/mv %buildroot%_x11x11dir/icewm/themes/%theme %buildroot%_x11x11dir/icewm/themes/SilverXP

# fix font name
/bin/sed -i 's,-koi8-r,-*-*,g' %buildroot%_x11x11dir/icewm/themes/*/default.theme
# do not paint buttons border
/bin/sed -i 's,^#  $,ShowButtonBorder=0,' %buildroot%_x11x11dir/icewm/themes/*/default.theme

find %buildroot%_x11x11dir/icewm/themes -type f -print0 | 
	xargs -r0 chmod 0444
find %buildroot%_x11x11dir/icewm/themes -type d -print0 | 
	xargs -r0 chmod 0755

%files
%_x11x11dir/icewm/themes/SilverXP

%changelog
* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt4
- now depends of design-icewm

* Sun Nov 01 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt3
- internal RPM macros are replaced by real commands

* Sat Jan 20 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt2
- rebuild (fix bug #10391)

* Mon Sep 26 2005 Kachalov Anton <mouse@altlinux.ru> 1.2.17-alt1
- first build
