%define _name places

Name: e18-module-%_name
Version: 0.5.0
Release: alt0.2

Summary: %_name module for the Enlightenment desktop
License: BSD
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/

#Source: ftp://ftp.enlightenment.org/pub/enlightenment/%_name-%version.tar.gz
Source: %_name-%version.tar

Requires: e18 = %e18_version

BuildRequires: e18-devel

%description
%_name module for the Enlightenment desktop.
This module manage the volumes device attached to the system.

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
* Wed Mar 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt0.2
- rebuilt for e18-0.18.5

* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt0.1
- 0.5.0 snapshot (b4754088)

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt6
- rebuilt for e17-0.17.5

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt5
- rebuilt for e17-0.17.4

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt4
- rebuilt for e17-0.17.3

* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt3
- rebuilt for e17-0.17.2.1

* Sat Apr 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- updated from upstream git, built for e17-0.17.1

* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

