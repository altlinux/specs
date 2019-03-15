Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           seahorse-adventures
Version:        1.1
Release:        alt1_1
Summary:        Help barbie the seahorse float on bubbles to the moon
License:        GPL+
URL:            http://www.imitationpickles.org/barbie/
Source0:        http://www.imitationpickles.org/barbie/files/barbie-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         seahorse-adventures-1.0-symlink.patch
Patch1:         seahorse-adventures-1.0-build.patch
BuildRequires:  desktop-file-utils libappstream-glib
BuildArch:      noarch
Requires:       icon-theme-hicolor python-module-pygame fonts-ttf-dejavu
Source44: import.info

%description
Help barbie the seahorse float on bubbles to the moon. This is a retro-side
scroller game. It won the teams category in pyweek 4. Includes original
soundtrack, graphics, and 15 levels!


%prep
%setup -q -n barbie-%{version}
%patch0 -p1
%patch1 -p1
sed -i 's:/usr/bin/python:/usr/bin/python2:' leveledit.py tileedit.py
sed -i 's:/usr/bin/env python:/usr/bin/python2:' run_game.py
rm data/themes/*/Vera.ttf


%build
# nothing to build, pure python code only


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data lib leveledit.py run_game.py tileedit.py \
  $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s ../../../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/themes/default/Vera.ttf
ln -s ../../../../fonts/ttf/dejavu/DejaVuSans.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/themes/gray/Vera.ttf

chmod +x $RPM_BUILD_ROOT%{_datadir}/%{name}/run_game.py
ln -s ../share/%{name}/run_game.py $RPM_BUILD_ROOT%{_bindir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 icon32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 icon64.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 icon128.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc CHANGES.txt LEVELS.txt NOTES.txt README.txt TODO.txt
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
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

