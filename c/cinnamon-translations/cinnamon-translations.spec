%define ver_major 6.2

Name: cinnamon-translations
Version: %ver_major.1
Release: alt1

Summary: Translations for Cinnamon
License: GPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-translations
BuildArch: noarch

# Source-url: https://github.com/linuxmint/cinnamon-translations/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Conflicts: cinnamon < 1.9.1

%description
Translations for Cinnamon

%package -n nemo-translations
Summary: Translations for Nemo
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n nemo-translations
Translations for Nemo

%package -n nemo-extensions-translations
Summary: Translations for Nemo extensions
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n nemo-extensions-translations
Translations for Nemo extensions

%package -n cinnamon-control-center-translations
Summary: Translations for cinnamon-control-center
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n cinnamon-control-center-translations
Translations for cinnamon-control-center

%package -n cinnamon-screensaver-translations
Summary: Translations for cinnamon-screensaver
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n cinnamon-screensaver-translations
Translations for cinnamon-screensaver

%package -n cinnamon-session-translations
Summary: Translations for cinnamon-session
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n cinnamon-session-translations
Translations for cinnamon-session

%package -n cinnamon-settings-daemon-translations
Summary: Translations for cinnamon-settings-daemon
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later

%description -n cinnamon-settings-daemon-translations
Translations for cinnamon-settings-daemon

%prep
%setup -q -n %name-%version

%build
make

%install
install -m 0755 -d %{buildroot}%{_datadir}/locale
cp -Rp usr/share/locale/* %{buildroot}%{_datadir}/locale

%find_lang cinnamon
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

%files -f cinnamon.lang
%doc COPYING

%files -n nemo-translations -f nemo.lang

%files -n nemo-extensions-translations -f nemo-extensions.lang

%files -n cinnamon-control-center-translations -f cinnamon-control-center.lang

%files -n cinnamon-screensaver-translations -f cinnamon-screensaver.lang

%files -n cinnamon-session-translations -f cinnamon-session.lang

%files -n cinnamon-settings-daemon-translations -f cinnamon-settings-daemon.lang

%changelog
* Fri Jun 21 2024 Anton Midyukov <antohami@altlinux.org> 6.2.1-alt1
- 6.2.1

* Sun Jun 16 2024 Anton Midyukov <antohami@altlinux.org> 6.2.0-alt1
- 6.2.0

* Fri Jan 05 2024 Anton Midyukov <antohami@altlinux.org> 6.0.2-alt1
- 6.0.2

* Mon Dec 04 2023 Anton Midyukov <antohami@altlinux.org> 6.0.1-alt1
- 6.0.1

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- 6.0.0
- Fix License

* Mon Jul 10 2023 Vladimir Didenko <cow@altlinux.org> 5.8.2-alt1
- 5.8.2

* Thu Jun 8 2023 Vladimir Didenko <cow@altlinux.org> 5.8.1-alt1
- 5.8.1

* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 5.6.1-alt1
- 5.6.1

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 5.4.2-alt1
- 5.4.2

* Tue Jul 12 2022 Vladimir Didenko <cow@altlinux.org> 5.4.1-alt1
- 5.4.1

* Thu Jan 13 2022 Vladimir Didenko <cow@altlinux.org> 5.2.2-alt1
- 5.2.2

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 5.2.1-alt1
- 5.2.1

* Tue Jun 29 2021 Vladimir Didenko <cow@altlinux.org> 5.0.2-alt1
- 5.0.2

* Thu Jun 17 2021 Vladimir Didenko <cow@altlinux.org> 5.0.1-alt1
- 5.0.1

* Fri May 28 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt1
- 5.0.0

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 4.8.3-alt1
- 4.8.3

* Tue Dec 22 2020 Vladimir Didenko <cow@altlinux.org> 4.8.2-alt1
- 4.8.2

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 4.8.1-alt1
- 4.8.1

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 4.6.2-alt1
- 4.6.2

* Tue Jun 23 2020 Vladimir Didenko <cow@altlinux.org> 4.6.1-alt1
- 4.6.1

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0

* Wed Jan 8 2020 Vladimir Didenko <cow@altlinux.org> 4.4.2-alt1
- 4.4.2

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1
- 4.4.1

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.2-alt1
- 4.2.2

* Mon Jul 15 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.1-alt1
- 4.0.1

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 5 2018 Vladimir Didenko <cow@altlinux.org> 3.6.4-alt1
- 3.6.4

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 3.6.3-alt1
- 3.6.3

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1

* Thu Jul 7 2016 Vladimir Didenko <cow@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue May 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.8.3-alt1
- 2.8.3

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.2-alt1
- 2.8.2

* Wed Oct 21 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.7.0-alt1
- 2.6.3-9-ga2a26c3

* Wed Jul 1 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3

* Wed Jun 3 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Tue Nov 11 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue May 27 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- don't pack translations for bluetooth applet

* Fri Nov 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt2
- rebuild for GNOME-3.10

* Wed Aug 28 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- Initial build
