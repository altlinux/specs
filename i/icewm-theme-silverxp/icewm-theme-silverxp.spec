Name: icewm-theme-silverxp
Version: 1.2.17
Release: alt6

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
/bin/sed -i 's,-koi8-r,-*-*,g' %buildroot%_x11x11dir/icewm/themes/SilverXP/default.theme

cat <<'EOF' >> %buildroot%_x11x11dir/icewm/themes/SilverXP/default.theme
# Colors for memory monitor:

#  User program usage in memory monitor
ColorMEMStatusUser="rgb:00/FF/00"

#  OS buffers usage in memory monitor
ColorMEMStatusBuffers="rgb:FF/00/00"

#  OS cached usage in memory monitor
ColorMEMStatusCached="rgb:FF/FF/FF"

#  Free memory in memory monitor
ColorMEMStatusFree=""

EOF

%files
%_x11x11dir/icewm/themes/SilverXP

%changelog
* Sat Sep 26 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.17-alt6
- added colors for memory monitor
- cleanup spec

* Mon Jan 07 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.17-alt5
- updated some .xpm's for fix breaks themes with xorg 1.12.3.902 and later
  (bfo#54168)

* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt4
- now depends of design-icewm

* Sun Nov 01 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt3
- internal RPM macros are replaced by real commands

* Sat Jan 20 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt2
- rebuild (fix bug #10391)

* Mon Sep 26 2005 Kachalov Anton <mouse@altlinux.ru> 1.2.17-alt1
- first build
