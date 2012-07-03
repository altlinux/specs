Name: xmms-lirc
Version: 1.4
Release: alt2

Summary: Infra-red control plugin for XMMS
License: GPL
Group: Toys
URL: http://sourceforge.net/projects/lirc/

BuildRequires: xmms-devel, liblirc-devel

Source0: %name-%version.tar.bz2

%description
Allow to control XMMS by your infra-red remote control, required LIRC

%prep
%setup -q

%build

%configure
%make_build

%install
%makeinstall libdir=$RPM_BUILD_ROOT%_libdir/xmms/General

%files
%_libdir/xmms/General/*.so
%doc lircrc AUTHORS ChangeLog NEWS README

%changelog
* Thu Nov 27 2003 Kachalov Anton <mouse@altlinux.ru> 1.4-alt2
- removed .la file

* Tue Jun 24 2003 Kachalov Anton <mouse@altlinux.ru> 1.4-alt1
- new version 1.4

* Tue Oct 29 2002 Kachalov Anton <mouse@altlinux.ru> 1.2-alt2
- rebuild

* Fri Jan 11 2002 Kachalov Anton <mouse@altlinux.ru> 1.2-alt1
- build for Sisyphus
