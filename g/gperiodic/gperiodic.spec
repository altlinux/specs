Name: gperiodic
Version: 2.0.10
Release: alt4

Summary: Program for browsing the periodic table
License: GPL
Group: Sciences/Chemistry

Url: http://www.frantz.fi/software/gperiodic.php
Source0: http://www.frantz.fi/software/%name-%version.tar.gz
Source1: gperiodic.1
Patch0: 11_remove_DEPRECATED_flags_for_GTK_2_4.dpatch
Patch1: 12_fix_desktop_file.dpatch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Jun 30 2007
BuildRequires: libgtk+2-devel

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%prep
%setup -q -n gperiodic-%version
%patch0 -p1
%patch1 -p1

%build
%make

%install
mkdir -p %buildroot{%_bindir,%_desktopdir,%_pixmapsdir}
%makeinstall
mkdir -p %buildroot%_man1dir/
install -p -m644 %SOURCE1 %buildroot%_man1dir/
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_man1dir/*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_pixmapsdir/gperiodic-crystal.png
%doc README NEWS AUTHORS ChangeLog gpl.txt

%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 2.0.10-alt4
- applied repocop patch

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gperiodic

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 2.0.10-alt3
- updated Url:

* Mon Nov 12 2007 Michael Shigorin <mike@altlinux.org> 2.0.10-alt2
- rebuild

* Mon Nov 12 2007 Igor Zubkov <icesik@altlinux.org> 2.0.10-alt1.1
- NMU:
  + fix rebuild with new gtk+2 (patch from debian)
  + add manual page (patch from debian)

* Thu Jul 12 2007 Michael Shigorin <mike@altlinux.org> 2.0.10-alt1
- ru.po merged upstream (with some other changes as well)

* Sat Jun 30 2007 Michael Shigorin <mike@altlinux.org> 2.0.9-alt2
- added ru.po (I've translated 1.2.6 last century...)

* Sat Jun 30 2007 Michael Shigorin <mike@altlinux.org> 2.0.9-alt1
- built for ALT Linux
- major spec cleanup

* Wed Jun 27 2007 Jonas Frantz <jonas.frantz@helsinki.fi> 2.0.9
- Merged fixes from the debian project, submitted by Daniel Leidert
- Included galician translation submitted by Gonzalo and Leandro Regueiro

* Sat Aug 9 2003 Jonas Frantz <jonas.frantz@helsinki.fi>
- Initial build

