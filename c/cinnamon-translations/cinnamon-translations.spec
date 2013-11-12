%define ver_major 2.0

Name: cinnamon-translations
Version: %ver_major.2
Release: alt1

Summary: Translations for Cinnamon
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-translations
Packager: Vladimir Didenko <cow@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses

Conflicts: cinnamon < 1.9.1

%description
Translations for Cinnamon

%package -n nemo-translations
Summary: Translations for Nemo
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n nemo-translations
Translations for Nemo

%package -n cinnamon-control-center-translations
Summary: Translations for cinnamon-control-center
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n cinnamon-control-center-translations
Translations for cinnamon-control-center

%package -n cinnamon-screensaver-translations
Summary: Translations for cinnamon-screensaver
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n cinnamon-screensaver-translations
Translations for cinnamon-screensaver

%package -n cinnamon-bluetooth-translations
Summary: Translations for cinnamon-bluetooth
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n cinnamon-bluetooth-translations
Translations for cinnamon-bluetooth

%prep
%setup -q -n %name-%version

%build

%install
install -m 0755 -d %{buildroot}%{_datadir}/cinnamon/locale/ 
cp -Rp mo-export/* %{buildroot}%{_datadir}/cinnamon/locale/

%find_lang cinnamon
%find_lang nemo
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-bluetooth

%files -f cinnamon.lang
%doc COPYING

%files -n nemo-translations -f nemo.lang

%files -n cinnamon-control-center-translations -f cinnamon-control-center.lang

%files -n cinnamon-screensaver-translations -f cinnamon-screensaver.lang

%files -n cinnamon-bluetooth-translations -f cinnamon-bluetooth.lang

%changelog
* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt2
- rebuild for GNOME-3.10

* Wed Aug 28 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- Initial build
