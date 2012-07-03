Name: ibam
Version: 0.5.2
Release: alt2

Summary: Intelligent Battery Monitor
License: GPL
Group: Monitoring

Url: http://ibam.sourceforge.net
Source: %name-%version.tar.gz
Patch1: %name-gkrellm-fix-display-order.patch
Patch2: %name-0.4-alt-linking.patch
Patch3: ibam-0.5.2-debian-acpi-check.patch
Patch4: ibam-0.5.2-debian-sysfs-lenovo.patch
Packager: Ilya Mashkin <oddity@altlinux.org>

# Automatically added by buildreq on Thu Mar 01 2012
# optimized out: glib2-devel libatk-devel libcairo-devel libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ gdk-pixbuf-devel gkrellm-devel gtk+-devel

%description
IBAM is an advanced battery monitor for laptops, which uses statistical
and adaptive linear methods to provide accurate estimations of minutes
of battery left or of the time needed until full recharge.

%package -n gkrellm-%name
Group: Monitoring
Summary: GKrellM Intelligent Battery Monitor (IBaM) plugin

%description -n gkrellm-%name
IBAM is an advanced battery monitor for laptops, which uses statistical
and adaptive linear methods to provide accurate estimations of minutes
of battery left or of the time needed until full recharge.

This is the GKrellM2 plugin.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build RPM_OPT_FLAGS="%optflags" ibam krell

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 ibam-krell.so %buildroot%_libdir/gkrellm2/plugins/ibam-krell.so

%files
%doc CHANGES README REPORT
%_bindir/%name

%files -n gkrellm-%name
%_libdir/gkrellm2/plugins/%name-*

%changelog
* Thu Mar 01 2012 Michael Shigorin <mike@altlinux.org> 0.5.2-alt2
- applied Debian patches (fixes: #25725)
- minor spec cleanup
- buildreq

* Sat Jun 11 2011 Ilya Mashkin <oddity@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Thu Oct 30 2008 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sun Nov 11 2007 Igor Zubkov <icesik@altlinux.org> 0.4-alt4
- merge changes from ildar@
- buildreq
- link ibam-krell.so with -lgtk-x11-2.0

* Tue Nov 06 2007 Ildar Mulyukov <ildar@altlinux.ru> 0.4-alt3
- Added package: gkrellm-%name
- ibam-gkrellm-fix-display-order.patch added

* Wed Dec 13 2006 Igor Zubkov <icesik@altlinux.org> 0.4-alt2
- merge changes from mike@

* Tue Dec 12 2006 Michael Shigorin <mike@altlinux.org> 0.4-alt1.1
- fixed Group:

* Tue Dec 12 2006 Igor Zubkov <icesik@altlinux.org> 0.4-alt1
- Initial build for Sisyphus

