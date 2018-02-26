Name: system-tools-backends
Version: 2.10.1
Release: alt1

Summary: System Tools to manage computer configuration -- scripts
License: GPL
Group: System/Libraries
Url: http://system-tools-backends.freedesktop.org
Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %name-%version.tar
Source1: %name.init
Source2: %name.1

BuildRequires: perl-XML-Parser perl-Net-DBus libdbus-devel libdbus-glib-devel glib2-devel libgio-devel libpolkit1-devel autogen intltool

%set_perl_req_method relaxed

%description
The System Tools Backends are a set of cross-platform scripts for Linux
and other Unix systems. The backends provide a standard XML interface
for modifying the configuration regardless of the distribution that's
being used.

%package devel
Summary: System Tools to manage computer configuration -- development files
Group: Development/C
PreReq: %name = %version-%release

%description devel
The System Tools Backends are a set of cross-platform scripts for Linux
and other Unix systems. The backends provide a standard XML interface
for modifying the configuration regardless of the distribution that's
being used.
This package contain development files.

%prep
%setup -q

%build
%autoreconf
%configure --with-net-dbus=%_libdir/perl5 --with-stb-group=stb-admin --localstatedir=%_var
%make_build

%install
%makeinstall_std
install -D %SOURCE1 %buildroot%_initdir/stbd
install -D %SOURCE2 %buildroot%_man1dir/%{name}.1
%find_lang %name

%post
/usr/sbin/groupadd -r -f stb-admin

%files -f %name.lang
%_sysconfdir/dbus-1/system.d/org.freedesktop.SystemToolsBackends.conf
%_initdir/stbd
%_sbindir/%name
%_datadir/%name-2.0
%_datadir/polkit-1/actions/org.freedesktop.SystemToolsBackends.policy
%_datadir/dbus-1/system-services/org.freedesktop.SystemToolsBackends*
%_man1dir/%{name}*

%files devel
%_libdir/pkgconfig/%name-2.0.pc
%doc AUTHORS ChangeLog NEWS COPYING README

%changelog
* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 2.10.1-alt1
- New version 2.10.1

* Sat Apr 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.10.0-alt1
- New version 2.10.0

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 2.9.4-alt1
- New version 2.9.4

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 2.9.3-alt1
- New version 2.9.3

* Sun Jan 24 2010 Vladimir Lettiev <crux@altlinux.ru> 2.9.1-alt1
- New version 2.9.1
- drop patch 08_use_md5.patch

* Mon Dec 28 2009 Vladimir Lettiev <crux@altlinux.ru> 2.8.3-alt1
- new version

* Tue Oct 27 2009 Vladimir Lettiev <crux@altlinux.ru> 2.8.2-alt1
- new version

* Sun May 03 2009 Vladimir Lettiev <crux@altlinux.ru> 2.6.1-alt1
- new release
- s-t-b moved to sbindir (Closes: 17516)
- security fix: CVE-2008-4311

* Wed Sep 17 2008 Vladimir Lettiev <crux@altlinux.ru> 2.6.0-alt1
- Initial build for Sisyphus

