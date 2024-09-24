%define _unpackaged_files_terminate_build 1

Name: fprintd
Version: 1.94.4
Release: alt1

Summary: D-Bus service for Fingerprint reader access
License: GPLv2+
Group: System/Servers
Url: https://www.freedesktop.org/wiki/Software/fprint/fprintd
VCS: https://gitlab.freedesktop.org/libfprint/fprintd.git

Source: %name-%version.tar
Source1: system-auth-fprintd
Source2: system-auth-use_first_pass-fprintd

Patch: %name-%version.patch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

BuildRequires: libgio-devel
BuildRequires: libpam0-devel
BuildRequires: libpolkit-devel
BuildRequires: libsystemd-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libfprint2-gir-devel

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: perl-podlators
BuildRequires: xml-utils
BuildRequires: xsltproc
BuildRequires: docbook-dtds

BuildRequires: pam_wrapper
BuildRequires: rpm-macros-pam0
BuildRequires: libpamtest-devel
BuildRequires: python3-module-libpamtest

BuildRequires: python3-module-pycairo
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dbusmock
BuildRequires: python3-module-pygobject3

Requires: %name-clients = %EVR

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
Requires: %name = %EVR
Group: Development/Other
BuildArch: noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%package clients
Summary: %name clients
Group: System/Base

%description clients
Client appications to access fingerprint readers

%prep
%setup -q
%patch -p1

%build
%meson -Dpam_modules_dir=%_pam_modules_dir
%meson_build

%install
%meson_install
%find_lang %name

mkdir -p %buildroot%_sysconfdir/pam.d
install -m0644 -p %SOURCE1 %buildroot%_sysconfdir/pam.d/
install -m0644 -p %SOURCE2 %buildroot%_sysconfdir/pam.d/

%check
%meson_test -j1

%files -f %name.lang
%doc README COPYING AUTHORS TODO
%config(noreplace) %_sysconfdir/fprintd.conf
%_datadir/dbus-1/system.d/net.reactivated.Fprint.conf
%_prefix/lib/fprintd
%_unitdir/fprintd.service
%_datadir/dbus-1/system-services/net.reactivated.Fprint.service
%_datadir/polkit-1/actions/net.reactivated.fprint.device.policy
%_man1dir/fprintd.1*

%files -n pam_fprintd
%doc pam/README
%_pam_modules_dir/pam_fprintd.so
%_man8dir/pam_fprintd.8*
%_sysconfdir/pam.d/system-auth-*

%files devel
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%files clients
%_bindir/%name-*

%changelog
* Tue Sep 24 2024 Egor Ignatov <egori@altlinux.org> 1.94.4-alt1
- 1.94.4

* Thu Apr 04 2024 Egor Ignatov <egori@altlinux.org> 1.94.3-alt1
- 1.94.3

* Wed Apr 03 2024 Egor Ignatov <egori@altlinux.org> 1.94.2-alt3
- Remove unnecessary BRs

* Sun Mar 10 2024 Egor Ignatov <egori@altlinux.org> 1.94.2-alt2
- update Russian translation
- fix tests

* Tue Jun 21 2022 Egor Ignatov <egori@altlinux.org> 1.94.2-alt1
- 1.94.2
- backport upstream fix for tests (issue #135)

* Mon Nov 08 2021 Anton Farygin <rider@altlinux.ru> 1.94.1-alt1
- 1.94.1

* Thu Sep 02 2021 Anton Farygin <rider@altlinux.ru> 1.94.0-alt1
- 1.94.0

* Tue Jul 27 2021 Anton Farygin <rider@altlinux.ru> 1.92.0-alt1
- 1.92.0

* Tue Jun 29 2021 L.A. Kostis <lakostis@altlinux.ru> 1.90.9-alt1.1
- Split -clients pkg (to use them with other fingerprint providers).
- Add pam.d configuration into pam pkg.

* Mon Apr 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.90.9-alt1
- Updated to upstream version 1.90.9.
- Cleaned up spec and patches.

* Thu Aug 13 2020 Anton Farygin <rider@altlinux.ru> 1.90.1-alt1
- 1.90.1

* Sat Mar 17 2018 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

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
