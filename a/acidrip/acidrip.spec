Name: acidrip
Version: 0.14
Release: alt2.qa1

Summary: Video ripping and conversion tool
License: GPL
Group: Video

URL: http://untrepid.com/acidrip/
Source: %name-%version.tar.gz

BuildArch: noarch

Requires: lsdvd mencoder mplayer

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: lsdvd mencoder mplayer perl-Gtk2 perl-devel perl-podlators

%description
AcidRip is an automated front end for MPlayer/Mencoder written in Perl,
using Gtk2::Perl for a graphical interface. Makes encoding a DVD just
one button click!

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=AcidRip
Comment=Video ripping and conversion tool
Icon=%name
Exec=%name
Terminal=false
Categories=AudioVideo;Video;AudioVideoEditing;
EOF

%files
%_bindir/%name
%_man1dir/%name.*
%_desktopdir/%name.desktop
%dir %perl_vendor_privlib/AcidRip
%perl_vendor_privlib/AcidRip/*.pm
%perl_vendor_privlib/AcidRip/logo.png

%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2.qa1
- NMU: converted menu to desktop file

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- rebuilt

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.14-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for acidrip
  * postclean-05-filetriggers for spec file

* Sat Mar 05 2005 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.11 -> 0.14, resurrected from orphaned packages
- heavy specfile clenaup and policy enforcement

* Tue Nov 18 2003 Egor S. Orlov <oes@altlinux.ru> 0.11-alt3
- added fix from at@altlinux

* Wed Nov 12 2003 Egor S. Orlov <oes@altlinux.ru> 0.11-alt2
- fixed rebuild problem with lsdvd

* Mon Oct 06 2003 Egor S. Orlov <oes@altlinux.ru> 0.11-alt1
- New version

* Fri Oct 03 2003 Egor S. Orlov <oes@altlinux.ru> 0.10-alt1
- Fixed requires for hasher build

* Fri Aug 29 2003 Egor S. Orlov <oes@altlinux.ru> 0.10-alt0.1
- Version 0.10 (GTK2)

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.4
- Added russian translation for description and summary

* Tue Aug 05 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.3
- Fixed BuildArch

* Fri Aug 01 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.2
- Fixed menu item

* Fri Aug 01 2003 Egor S. Orlov <oes@altlinux.ru> 0.9-alt0.1
- Initial build for ALT
- Added acidrip-howto.html

* Fri Sep 27 2002 - Chris Phillips,,, <acid_kewpie\@users.sourceforge.net>
  wrote stuff
