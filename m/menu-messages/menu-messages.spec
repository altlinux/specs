%def_with merged_po
Name: menu-messages
Version: 0.3.2
Release: alt1

Group: System/Base
Summary: Localization files for Menu system
License: GPL

BuildArch: noarch
Conflicts: menu < 2.1.6

%if_with merged_po
Source0: po-merged.tar
%else 
Source0: menu-messages-20100829.tar
%endif
Source1: menu-ru-20051006.po
Source2: menu-uk-20050802.po
Source3: menu-be-20050802.po
Source4: menu_2.1.45.tar
Source5: menu-messages-20100829.tar

# temporary need
Source100: menu-file2pot
Source102: menu-messages-WM-ru.po
Source103: menu-get_menu_files

# Automatically added by buildreq on Mon Oct 29 2001
BuildRequires: gettext-tools

%description
This package includes that translations of the main menu used by the
different desktops and window managers of the distribution;
as well as translations used by specifically added features.

%prep
%if_with merged_po
%setup -q -n po
%else
%setup -q -n %name

install -m 0644 %SOURCE1 ru.po
install -m 0644 %SOURCE2 uk.po
install -m 0644 %SOURCE3 be.po
%endif

%install
mkdir -p %buildroot/%_datadir/locale

# fix norwegian bokmål in kde
[ ! -r nb.po -a -r no.po ] && cp no.po nb.po

# menu-messages files
for i in ./*.po
do
    langdir="%buildroot/%_datadir/locale/`basename ${i} .po`/LC_MESSAGES/"
    mkdir -p ${langdir}
    msgfmt -o ${langdir}/menu-messages.mo ${i}
done

%find_lang menu-messages

%post
# update_menus macro is deprecated, so we expanded it there
update_menus_bin=%_bindir/update-menus
[ -x "$update_menus_bin" ] && "$update_menus_bin" ||:


%files -f menu-messages.lang

%changelog
* Sat May 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- updated menu entries translations

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- updated freedesktop menu categories translations

* Sun Apr 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- merged freedesktop menu categories translations

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt4
- updated menu-messages from Mandriva
- added Simulation to ru/uk/be custom po files

* Thu Oct 06 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt3
- fix Russian translation

* Fri Sep 30 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt2
- update Russian translation

* Tue Aug 09 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- update Russian translation

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt3
- update Ukrainian translation by Andriy Dobrovolskii <dobr@altlinux>

* Wed Jun 16 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt2
- update Russian translation

* Thu Feb 26 2004 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial spec
