Name: fprintd
Version: 0.1
Release: alt3
Summary: D-Bus service for Fingerprint reader access
Group: System/Servers
License: GPLv2+

Requires: hal polkit
Requires: pam_fprintd = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc intltool libdbus-glib-devel libfprint-devel libpam-devel libpolkit1-devel

%description
D-Bus service to access fingerprint readers.

%package -n pam_fprintd
Summary: PAM module for fingerprint authentication
Provides: pam_fprint
Obsoletes: pam_fprint <= 0.2
Group: System/Base

%description -n pam_fprintd
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/Other

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
%setup -q
%patch -p1

%build
gtkdocize
%autoreconf
%configure \
	--libdir=/%_lib \
	--libexecdir=%_prefix/libexec \
	--enable-gtk-doc \
	--enable-pam \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/pam.d
cat %_sysconfdir/pam.d/system-auth-local | sed 's|^#%PAM-1.0|#%PAM-1.0\nauth     sufficient\tpam_fprintd.so|' > \
	%buildroot%_sysconfdir/pam.d/system-auth-fprintd
mkdir -p %buildroot%_localstatedir/fprint

%files
%doc README COPYING AUTHORS TODO
%config(noreplace) %_sysconfdir/fprintd.conf
%_sysconfdir/pam.d/system-auth-fprintd
%_sysconfdir/dbus-1/system.d/net.reactivated.Fprint.conf
%_bindir/fprintd-*
%_prefix/libexec/fprintd
%_datadir/dbus-1/system-services/net.reactivated.Fprint.service
%_datadir/polkit-1/actions/net.reactivated.fprint.device.policy
%dir %_localstatedir/fprint

%files -n pam_fprintd
%doc pam/README
/%_lib/security/pam_fprintd.so

%files devel
%_datadir/gtk-doc/html/fprintd
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt3
- ported to PolicyKit 1

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt2
- pam_fprintd: fixed obsoletes

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release

