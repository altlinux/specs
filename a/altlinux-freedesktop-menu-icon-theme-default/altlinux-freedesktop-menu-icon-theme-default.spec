Name: altlinux-freedesktop-menu-icon-theme-default
Version: 0.0.23
Release: alt1

Group: Graphical desktop/Other
Summary: Icons for Freedesktop Menu system
License: GPL
URL: http://www.altlinux.org/Menu_Policy
BuildArch: noarch

Provides: altlinux-freedesktop-menu-icon-theme = %version
Requires: icon-theme-hicolor
Requires: menu-icons-default > 0.2.0.11
BuildRequires: menu-icons-default > 0.2.0.11

Source0: link.sh

%description
Icons for Freedesktop Menu system

%prep

%install
#    %_iconsdir/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,scalable}/categories; do
for pixpath in \
    %_iconsdir/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,scalable}/apps; do
    destpath=`echo $pixpath | sed -e 's,apps,categories,'`
    pixdir=%{buildroot}${destpath}
    mkdir -p $pixdir
    pushd $pixdir
    	sh -v %{SOURCE0} $pixpath/ $(relative $pixpath $destpath/)/ ||:
    popd
done

%files
%_iconsdir/hicolor/*/categories/*.png
%_iconsdir/hicolor/scalable/categories/*

%changelog
* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.23-alt1
- fixed missing symlinks

* Wed May 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.22-alt1
- use source-target generator script

* Tue May 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.21-alt1
- added symlinks to scalable pixmaps

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.20-alt1
- Provides: altlinux-freedesktop-menu-icon-theme

* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.19-alt1
- sync with menu-icons-default-0.2.0.12

* Sat Apr 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.18-alt1
- sync with menu-icons-default-0.2.0.11

* Fri Apr 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.17-alt1
- sync with menu-icons-default-0.2.0.10

* Thu Apr 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.16-alt1
- sync with menu-icons-default-0.2.0.9

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1
- sync with menu-icons-default-0.2.0.8

* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.14-alt1
- updated categories

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1
- sync with menu-icons-default-0.2.0.6

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1
- sync with menu-icons-default-0.2.0.3

* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.11-alt1
- sync with menu-icons-default-0.2.0.1

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1
- updated categories

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1
- updated categories

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- updated categories

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1
- updated categories

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1
- sync with menu-icons-default-0.2

* Tue Mar 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt1
- updated categories

* Tue Mar 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt1
- updated categories

* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- use menu-icons-default-0.1.2

* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1
- use computer_science.png

* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1
- initial spec

