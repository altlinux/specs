%define engine_prefix libgtk-engine
%define _name nodoka

Name:           %engine_prefix-%_name
Version:        0.7.2
Release:        alt2
Summary:        The Nodoka GTK2 Theme Engine
Summary(ru_RU.UTF8): Модуль прорисовки тем GTK2 Nodoka

Group:          Graphical desktop/GNOME
License:        GPLv2
URL:            http://fedorahosted.org/nodoka
Source0:        %_name-%version.tar.gz
Source1:        window-border-themes.tar.gz
# https://fedorahosted.org/releases/n/o/gtk-engines-nodoka-%{version}.tar.gz
BuildRequires:  gtk2-devel
Requires:       gtk2 >= 2.12.12

%description
Nodoka is a Murrine engine based GTK2 theme engine. 

%description -l ru_RU.UTF-8
Nodoka - модуль прорисовки GTK2 основанный на Murrine. 

%package  -n gtk2-themes-nodoka
Summary:  Themes for Nodoka GTK2 Theme Engine
Summary(ru_RU.UTF8): Темы для модуля прорисовки GTK2 - Nodoka
Group:    Graphical desktop/GNOME
Requires: %{name} >= 0.6.90.1
BuildArch: noarch

%description -n gtk2-themes-nodoka
This package contains themes for the Nodoka GTK2 theme engine.
Included themes:
Nodoka
Nodoka-Aqua
Nodoka-Gilouche
Nodoka-Looks
Nodoka-Midnight
Nodoka-Rounded
Nodoka-Silver
Nodoka-Squared

%description -n gtk2-themes-nodoka -l ru_RU.UTF-8
Набор тем Nodoka для GNOME и XFCE. В набор включены следующие темы:
Nodoka
Nodoka-Aqua
Nodoka-Gilouche
Nodoka-Looks
Nodoka-Midnight
Nodoka-Rounded
Nodoka-Silver
Nodoka-Squared

%prep
%setup -q -n %_name-%version -a1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%{__cp} -r xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/Nodoka
%{__cp} -r metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/Nodoka
%{__cp} index.theme $RPM_BUILD_ROOT%{_datadir}/themes/Nodoka

#remove .la files
find $RPM_BUILD_ROOT -name *.la | xargs rm -f || true

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libnodoka.so

%files -n gtk2-themes-nodoka
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/themes/Nodoka*

%changelog
* Thu Apr 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.7.2-alt2
Added metacity and xfwm themes

* Sat Dec 6 2008 Denis Koryavov <dkoryavov@altlinux.org>  0.7.2-alt1
- First build for Sisyphus
