%define shortname bluez

Name: gkrellm-%shortname
Version: 0.2
Release: alt2.qa1

Summary: GKrellm plugin monitoring Linux BlueZ adapters
License: GPL
Group: Monitoring
Url: http://sourceforge.net/projects/gkrellm-bluez/

Source: %name-%version.tar.bz2

BuildPreReq: gkrellm-devel libgtk+2-devel pkgconfig 
BuildPreReq: gcc-c++ libbluez-devel

%description
This plugin monitors the Bluetooth adapters in your computer and displays a
graph of the rx/tx bytes for each adapter.

%prep
%setup
%__autoreconf

%build
%configure --disable-static
%make_build

%install
%makeinstall PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins/

%files
%_libdir/gkrellm2/plugins/*.so
%doc AUTHORS README THEMING TODO

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 25 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- fix building with new autotools

* Mon Dec 18 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- initial build
