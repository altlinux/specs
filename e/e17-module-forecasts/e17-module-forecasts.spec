%define _name forecasts

Name: e17-module-%_name
Version: 0.2.0
Release: alt1

Summary: %_name module for the Enlightenment desktop
License: BSD
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/

#Source: ftp://ftp.enlightenment.org/pub/enlightenment/%_name-%version.tar.gz
Source: %_name-%version.tar

Requires: e17

BuildRequires: e17-devel
BuildRequires: edje embryo_cc

%description
The forecasts gadget for the Enlightenment desktop to display the current
weather conditions plus a few days forecast.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/enlightenment/modules/%{_name}*
%doc AUTHORS ChangeLog COPYING* NEWS README

%changelog
* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

