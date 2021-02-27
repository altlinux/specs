Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: seahorse-adventures
Summary: Help barbie the seahorse float on bubbles to the moon
License: GPLv2+

Version: 1.2
Release: alt1_4

URL: http://www.imitationpickles.org/barbie/

%global git_tag release-%{version}
Source0: https://github.com/dulsi/seahorse-adventures/archive/%{git_tag}/%{name}-%{git_tag}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.appdata.xml

Patch0: seahorse-adventures-1.2--symlink.patch
Patch1: seahorse-adventures-1.2--build.patch

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: icon-theme-hicolor
Requires: python3-module-pygame

%global fontlist font(bitstreamverasans)
BuildRequires: fontconfig
BuildRequires: fonts-ttf-vera
Requires: fonts-ttf-vera
Source44: import.info


%description
Help barbie the seahorse float on bubbles to the moon. This is a retro-side
scroller game. It won the teams category in pyweek 4. Includes original
soundtrack, graphics, and 15 levels!


%prep
%setup -q -n %{name}-%{git_tag}
%patch0 -p1
%patch1 -p1

sed \
	-e 's|#![ ]*/usr/bin/python|#!%{_bindir}/python3|' \
	-e 's|#![ ]*/usr/bin/env python|#!%{_bindir}/python3|' \
	-i create-upload.py leveledit.py run_game.py tileedit.py


%build
# nothing to build, pure python code only


%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
install -m 755 -p leveledit.py run_game.py tileedit.py %{buildroot}%{_datadir}/%{name}/
cp -a data/ lib/ %{buildroot}%{_datadir}/%{name}

VERA_PATH="$(fc-match -f "%%{file}" "Bitstream Vera Sans")"
for FONT_FILE in $(find %{buildroot}%{_datadir}/%{name}/ -name 'Vera.ttf'); do
	ln -sf "${VERA_PATH}" "${FONT_FILE}"
done

install -m 755 -d %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/run_game.py %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

for ICON_SIZE in 32 64 128; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "icon${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%doc CHANGES.txt LEVELS.txt NOTES.txt README.txt TODO.txt
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt1_4
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_19
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_17
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_13
- update to new release by fcimport

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_9
- update to new release by fcimport

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3_8.1
- Rebuild with Python-2.7

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_8
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8
- converted from Fedora by srpmconvert script

