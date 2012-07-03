%define real_name oxygen
%define gtk2_prefix gtk2-theme

Summary: Oxygen GTK2 theme
Summary(ru_RU.UTF8): Тема Oxygen для GTK2
Name: %gtk2_prefix-%real_name
Version: 1.0
Release: alt1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.gnome-look.org/content/show.php/KDE4+Oxygen+new+port+for+GNOME?content=86653
Packager: Denis Koryavov <dkoryavov@altlinux.org>
BuildArch: noarch

Source0: %{gtk2_prefix}-%{real_name}-%{version}.tar.bz2

%description
Oxygen is the default KDE4 theme. This is GTK2 port.

%description -l ru_RU.UTF8
Данная тема представляет собой порт на GTK2 стандартной темы KDE4 - Oxygen.
Декорации окон для XFCE так же включены. Лучше всего сочетается с темой иконок OxygenRefit2.

%prep
%setup -q -n %{gtk2_prefix}-%{real_name}-%{version}

%install
%{__mkdir} -p %buildroot%_datadir/themes/oxygen-gtk2
%{__cp} -r gtk-2.0 $RPM_BUILD_ROOT%{_datadir}/themes/oxygen-gtk2
%{__cp} -r metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/oxygen-gtk2
%{__cp} -r xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/oxygen-gtk2

%files
%defattr(-, root, root, 0755)
%{_datadir}/themes/oxygen-gtk2/

%changelog
* Fri Nov 7 2008 Denis Koryavov <dkoryavov@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
