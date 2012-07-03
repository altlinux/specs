%define plugin xkb

Name: gkrellm-%plugin
Version: 1.05
Release: alt3

Summary: GKrellM xkb plugin
License: GPL
Group: Monitoring
Url: http://sweb.cz/tripie/gkrellm/xkb/
Source: http://sweb.cz/tripie/gkrellm/xkb/dist/%name-%version.tar.gz

Patch0: gkrellm-xkb-1.05-alt-flag.patch

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Thu Nov 11 2004
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig

%description
gkrellm-xkb is a plugin for gkrellm which displays a small country flag indicating 
the currently-active national keyboard layout.
The plugin uses the XKB X Window extension and doesn't work when the extension is 
disabled or not available.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%__install -m755 %plugin.so %buildroot%_libdir/gkrellm2/plugins/%plugin.so

%files
%doc TODO doc/*
%_libdir/gkrellm2/plugins/%plugin.so


%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.05-alt3
- fix build

* Thu Nov 11 2004 Alex Murygin <murygin@altlinux.ru> 1.05-alt2
- added Belarus flag (thanks Kirill A. Shutemov)
- added Ukranian flag

* Mon Mar 15 2004 Alex Murygin <murygin@altlinux.ru> 1.05-alt1
- new version

* Thu Jan 08 2004 Alex Murygin <murygin@altlinux.ru> 1.04-alt1
- new version

* Sat Jun 28 2003 Alex Murygin <murygin@altlinux.ru> 1.00-alt1
- Built for ALTLinux

