Name: fprintd
Version: 0.4.1
Release: alt1.1
Summary: D-Bus service for Fingerprint reader access
Group: System/Servers
Url: http://www.freedesktop.org/wiki/Software/fprint/fprintd
License: GPLv2+

Source: %name-%version.tar
Source1: system-auth-fprintd
Patch: %name-%version-%release.patch
Patch1: %name-%version-alt-build.patch
Patch2: %name-%version-debian-pam_args.patch
Patch3: %name-%version-alt-pam_docs.patch

BuildRequires: libdbus-glib-devel libfprint-devel libpam0-devel libpolkit-devel
BuildRequires: gtk-doc intltool

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
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/pam.d
cp system-auth-fprintd %buildroot%_sysconfdir/pam.d
mkdir -p %buildroot%_localstatedir/fprint
rm -fv %buildroot/%_lib/security/pam_fprintd.{a,la,so.*}
%find_lang %name

%files -f %name.lang
%doc README COPYING AUTHORS TODO
%config(noreplace) %_sysconfdir/fprintd.conf
%_sysconfdir/pam.d/system-auth-fprintd
%_sysconfdir/dbus-1/system.d/net.reactivated.Fprint.conf
%_bindir/fprintd-*
%_prefix/libexec/fprintd
%_datadir/dbus-1/system-services/net.reactivated.Fprint.service
%_datadir/polkit-1/actions/net.reactivated.fprint.device.policy
%dir %_localstatedir/fprint
%_man1dir/fprintd.1*

%files -n pam_fprintd
%doc pam/README
/%_lib/security/pam_fprintd.so

%files devel
%_datadir/gtk-doc/html/fprintd
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1.1
- NMU: added URL

* Fri Oct 26 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.4.1-alt1
- 0.4.1 with git updates (closes: #27851)

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt3
- ported to PolicyKit 1

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt2
- pam_fprintd: fixed obsoletes

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release
