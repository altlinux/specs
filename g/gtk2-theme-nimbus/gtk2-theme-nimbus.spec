%define real_name nimbus
%define gtk2_prefix gtk2-theme

Summary: Nimbus GTK2 theme
Summary(ru_RU.UTF8): Тема для GTK2 Numbus
Name: %gtk2_prefix-%real_name
Version: 0.1.3
Release: alt1
License: GPL
Group: Graphical desktop/GNOME
URL: http://dlc.sun.com/osol/jds/downloads/extras/
Packager: Denis Koryavov <dkoryavov@altlinux.org>

Source0: %{real_name}-%{version}.tar.bz2
Source1: nimbus-xfwm4.tar.bz2

BuildRequires: gtk2-devel, automake, autoconf
BuildRequires: intltool >= 0.23
BuildRequires: gnome-common >= 1.2.4
BuildRequires: icon-naming-utils >= 0.8.1

%description
Nimbus is the default GTK2 theme from OpenSolaris.

%description -l ru_RU.UTF8
Nimbus - стандартная тема GTK2 используемая в OpenSolaris.

%prep
%setup -q -n %{real_name}-%{version} -a1

%build
%autoreconf
%configure --enable-animation --enable-macmenu --prefix=%{_prefix}
%make

%install
%makeinstall
%{__cp} -r xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/nimbus

%files
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/icons/nimbus/
%{_datadir}/themes/nimbus/
%{_datadir}/themes/dark-nimbus
%{_datadir}/themes/light-nimbus
%{_libdir}/gtk-2.0/*/engines/libnimbus.so

%exclude %{_libdir}/gtk-2.0/*/engines/libnimbus.a
%exclude %{_libdir}/gtk-2.0/*/engines/libnimbus.la

%changelog
* Thu Sep 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.1.3-alt1
- Version update

* Sun Feb 22 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.1.2-alt1
- Version update.

* Fri Oct 3 2008 Denis Koryavov <dkoryavov@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
