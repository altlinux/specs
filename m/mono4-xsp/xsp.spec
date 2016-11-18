Name: mono4-xsp
Url: http://go-mono.com/
License: X11/MIT
Group: System/Servers
Version: 4.4
Release: alt1
Summary: Small Web Server Hosting ASP.NET
Packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar.bz2

BuildRequires(pre): rpm-build-mono4  sqlite3 mono4-devel-full mono4-full pkg-config /proc
%define xspConfigsLocation %_sysconfdir/xsp/4.0
%define xspAvailableApps %xspConfigsLocation/applications-available
%define xspEnabledApps %xspConfigsLocation/applications-enabled

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
* Thu Nov 17 2016 Denis Medvedev <nbr@altlinux.org> 4.4-alt1
- new upstream version

* Wed Jan 13 2016 Denis Medvedev <nbr@altlinux.org> 4.2-alt1
- initial build for ALT Linux Sisyphus

