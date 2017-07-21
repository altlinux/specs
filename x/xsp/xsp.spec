Name: xsp
Url: http://go-mono.com/
License: X11/MIT
Group: System/Servers
Version: 4.4
Release: alt1
Summary: Small Web Server Hosting ASP.NET

Source: %name-%version.tar.bz2

BuildRequires(pre): rpm-build-mono  sqlite3 mono-devel-full mono-full pkg-config /proc
%define xspConfigsLocation %_sysconfdir/xsp/4.0
%define xspAvailableApps %xspConfigsLocation/applications-available
%define xspEnabledApps %xspConfigsLocation/applications-enabled

Conflicts: mono4-xsp

%description
The XSP server is a small Web server that hosts the Mono System.Web
classes for running what is commonly known as ASP.NET.


%prep
%setup
#%patch0

%build
cd xsp
%define _configure_script ./autogen.sh
%configure
make

%install
cd xsp
%makeinstall_std
rm -rf %buildroot%_libdir/xsp/unittests
mkdir -p %buildroot%_datadir
mv %buildroot%_pkgconfigdir %buildroot%_datadir
mkdir -p %buildroot/%_fwdefdir
mkdir -p %buildroot/%xspAvailableApps
mkdir -p %buildroot/%xspEnabledApps
mkdir -p %buildroot/etc/init.d/
mkdir -p %buildroot/etc/logrotate.d/
mkdir -p %buildroot/srv/xsp2
mkdir -p %buildroot/var/adm/fillup-templates
mkdir -p %buildroot%_runtimedir/xsp2
install -m 644 man/mono-asp-apps.1 %buildroot%_man1dir/mono-asp-apps.1
install -m 644 packaging/opensuse/sysconfig.xsp2 %buildroot/var/adm/fillup-templates
install -m 644 packaging/opensuse/xsp2.fw %buildroot/%_fwdefdir/xsp2
install -m 644 packaging/opensuse/xsp2.logrotate %buildroot/etc/logrotate.d/xsp2
install -m 755 packaging/opensuse/xsp2.init %buildroot/etc/init.d/xsp2
install -m 755 tools/mono-asp-apps/mono-asp-apps %buildroot%_bindir/mono-asp-apps





%files
%_bindir/*
%_datadir/pkgconfig/*
%_monodir/4.5/Mono.WebServer2.dll
%_monodir/4.5/fastcgi-mono-server4.exe
%_monodir/4.5/mod-mono-server4.exe
%_monodir/4.5/xsp4.exe
%_monogacdir/Mono.WebServer2
%_monogacdir/fastcgi-mono-server4
%_monogacdir/mod-mono-server4
%_monogacdir/xsp4
%_libexecdir/monodoc/sources/Mono.WebServer.*
%_libexecdir/monodoc/sources/Mono.FastCGI.*
%_libexecdir/xs*
%_mandir/*/*

%changelog
* Fri Jul 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4-alt1
- Based on mono4-xsp.
- Rebuilt with mono-5.

* Thu Feb 09 2012 Alexey Shabalin <shaba@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.8.1-alt1
- 2.8.1
- add doc subpackage

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Wed Dec 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Thu Dec 10 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- move pkgconfig files from main to devel package

* Sat Apr 18 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1

* Wed Apr 23 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Dec 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Aug 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.3-alt2
- Do not start on any runlevel by default

* Thu Mar 22 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.3-alt1
- 1.2.3
- Patch source instead of using sed
- Switch to use .gear-tags

* Mon Dec 04 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt1
- 1.2.1
- Rename /etc/sysconfig/xsp.conf to /etc/sysconfig/xsp
- Add dependency on mono-mcs

* Thu Nov 09 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.18-alt1
- 1.1.18
- Move xsp.conf from /etc/ to /etc/sysconfig/
- Add apache{1,2} pseudousers to xsp group
- Use %%_sysconfdir/mono/mod-mono-applications as default path for search for
  mod_mono applications
- Use full url in Source
- Minor spec cleanup

* Wed Nov 23 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release

* Sat Oct 08 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.2-alt1
- update to release

* Sun Aug 07 2005 Pavel Mironchik <tibor@altlinux.ru> 1.0.9-alt2
- fixed xsp-run script
- added tmpdirs to /etc/xsp.conf

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.9-alt1
- release

* Mon Aug  9 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0-alt1
- release

* Thu Feb 26 2004 Pavel S. Mironchik <tibor@altlinux.ru> 0.9-alt1
- new version release

* Wed Dec 17 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.8-alt1
- new release

* Thu Oct 16 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.6-alt1
- new version

* Thu Sep 18 2003 Pavel S. Mironchik <tibor@altlinux.ru> 0.5-alt1
- Initial build for ALTLinux.
