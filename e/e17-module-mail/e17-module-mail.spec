%define _name mail

Name: e17-module-%_name
Version: 0.0.3
Release: alt6

Summary: %_name module for the Enlightenment desktop
License: BSD
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/

#Source: ftp://ftp.enlightenment.org/pub/enlightenment/%_name-%version.tar.gz
Source: %_name-%version.tar

Requires: e17 = %e17_version

BuildRequires: e17-devel
BuildRequires: edje embryo_cc

%description
Mail notification gadget for the Enlightenment desktop.
Checks POP3, IMAP, maildir, and mbox mailboxes.

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
* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt6
- rebuilt for e17-0.17.5

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt5
- rebuilt for e17-0.17.4

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt4
- rebuilt for e17-0.17.3

* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt3
- rebuilt for e17-0.17.2.1

* Sat Apr 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt2
- updated from upstream git, built for e17-0.17.1

* Tue Jan 22 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- first build for Sisyphus

