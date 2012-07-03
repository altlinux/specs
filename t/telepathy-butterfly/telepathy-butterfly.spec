Name: telepathy-butterfly
Version: 0.5.15
Release: alt1.1

Summary: Telepathy MSN connection manager
License: GPL
Group: Networking/Instant messaging
Url: http://telepathy.freedesktop.org/wiki/TelepathyButterfly

Source: http://telepathy.freedesktop.org/releases/%name/%name-%version.tar.gz

BuildArch: noarch

Requires: python-module-papyon >= 0.5.4
BuildRequires: python-modules-compiler python-module-telepathy >= 0.15.19

%description
Telepathy MSN connection manager.

%prep
%setup -q

%build
./configure --prefix=/usr --libexecdir=/usr/lib
%make_build

%install
make DESTDIR=%buildroot install

%files
%_libexecdir/%name
%python_sitelibdir_noarch/butterfly/
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.butterfly.service
%_datadir/telepathy/managers/butterfly.manager
%doc AUTHORS NEWS

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.15-alt1.1
- Rebuild with Python-2.7

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.15-alt1
- 0.5.15

* Fri Sep 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.13-alt1
- 0.5.13

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.11-alt1
- 0.5.11

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.10-alt1
- 0.5.10

* Fri Apr 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.8-alt1
- 0.5.8

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.6-alt1
- 0.5.6

* Fri Mar 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Thu Nov 19 2009 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Thu Feb 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt2
- fixed directories ownership violation

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Mon Jul 21 2008 Igor Zubkov <icesik@altlinux.org> 0.3.2-alt1
- 0.3.1 -> 0.3.2

* Thu Jan 24 2008 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1

* Mon Jan 14 2008 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- 0.1.4 -> 0.3.0

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- build for Sisyphus


