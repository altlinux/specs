# Some tests can fail in girar (due to timeout for service start),
# but they work well in a local hasher.
# Just don't forget to enable them for local build when new version
# is released,
%def_enable check

#define git_date .git20160601
%define git_date %nil

%define dbus_version 1.1
%define libgudev_version 232

%def_with qrtr
%def_with qmi
%def_with mbim
%def_enable introspection
%def_disable vala

Name: ModemManager
Version: 1.20.2
Release: alt1%git_date
License: GPLv2+
Group: System/Configuration/Networking
Summary: Mobile broadband modem management service
Url: https://www.freedesktop.org/wiki/Software/ModemManager/
Vcs: https://gitlab.freedesktop.org/mobile-broadband/ModemManager.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: dbus >= %dbus_version

BuildRequires(pre): meson

BuildRequires: libgudev-devel >= %libgudev_version
BuildRequires: libgio-devel
%{?_with_qrtr:BuildRequires: libqrtr-glib-devel >= 1.0.0}
%{?_with_qmi:BuildRequires: libqmi-glib-devel >= 1.32.0}
%{?_with_mbim:BuildRequires: libmbim-glib-devel >= 1.28.0}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}
BuildRequires: ppp-devel
BuildRequires: libpolkit-devel
BuildRequires: libsystemd-devel >= 209
BuildRequires: libdbus-devel
BuildRequires: gtk-doc bash-completion

# For tests
%{?!_without_check:%{?!_disable_check:BuildRequires: /dev/pts}}
%{?!_without_check:%{?!_disable_check:BuildRequires: dbus}}
%{?!_without_check:%{?!_disable_check:BuildRequires: python3-module-pygobject3 python3-module-dbus}}

# Because of starting from the init script
Conflicts: NetworkManager < 0.9.8.9

%define _unpackaged_files_terminate_build 1

%description
ModemManager provides a DBus interface to communicate with
mobile broadband (GSM, CDMA, UMTS, ...) cards. Implements
a loadable plugin interface to add work-arounds for
non standard devices.

%package devel
License: LGPLv2+
Group: Development/C
Summary: Headers for adding ModemManager support to applications

%description devel
This package contains various headers accessing some ModemManager
functionality from applications.

%package devel-doc
Group: Development/Documentation
Summary: Development documentation for %name
BuildArch: noarch

%description devel-doc
%summary

%package -n libmm-glib
License: LGPLv2+
Summary: Libraries for adding ModemManager support to applications that use glib
Group: System/Libraries

%description -n libmm-glib
This package contains the libraries that make it easier to use some
ModemManager functionality from applications that use glib.

%package -n libmm-glib-devel
License: LGPLv2+
Summary: Development files for libmm-glib
Group: Development/C
Requires: libmm-glib = %version-%release

%description -n libmm-glib-devel
This package contains libraries and header files for
developing applications that use libmm-glib.

%package -n libmm-glib-devel-doc
Group: Development/Documentation
Summary: Development documentation for libmm-glib
BuildArch: noarch

%description -n libmm-glib-devel-doc
%summary

%package -n libmm-glib-gir
Summary: GObject introspection data for the ModemManager
Group: System/Libraries
Requires: libmm-glib = %version-%release

%description -n libmm-glib-gir
%summary

%package -n libmm-glib-gir-devel
Summary: GObject introspection devel data for the ModemManager
Group: System/Libraries
BuildArch: noarch
Requires: libmm-glib-gir = %version-%release
Requires: libmm-glib-devel = %version-%release

%description -n libmm-glib-gir-devel
%summary

%package -n libmm-glib-vala
Summary: Vala bindings for the ModemManager
Group: Development/Other
BuildArch: noarch
Requires: libmm-glib-devel = %version-%release

%description -n libmm-glib-vala
%summary

%prep
%setup -n %name-%version
%patch -p1

%build
%meson \
	-Dudevdir=/lib/udev \
	-Dpolkit=strict \
	-Dsystemdsystemunitdir=%_unitdir \
	-Dsystemd_suspend_resume=true \
	-Dsystemd_journal=true \
	-Dudev=true \
%if_with qrtr
	-Dqrtr=true \
%else
	-Dqrtr=false \
%endif
%if_with qmi
	-Dqmi=true \
%else
	-Dqmi=false \
%endif
%if_with mbim
	-Dmbim=true \
%else
	-Dmbim=false \
%endif
%if_enabled introspection
	-Dintrospection=true \
%else
	-Dintrospection=false \
%endif
%if_enabled vala
	-Dvapi=true \
%else
	-Dvapi=false \
%endif
	-Dgtk_doc=true

%meson_build -v

%install
%meson_install
%find_lang %name

%check
%meson_test

%post
if sd_booted; then
	%post_service_posttrans_restart %name.service
fi

%preun
# Don't stop service:
# the network can be via modem controlled
# by ModemManager itself.
#preun_service %name
if [ "$1" -eq 0 ]; then
	SYSTEMCTL=systemctl
	if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
		"$SYSTEMCTL" --no-reload -q disable %name.service ||:
	fi
fi

%files -f %name.lang
%doc NEWS AUTHORS README
%_datadir/dbus-1/system-services/*.service
%_sysconfdir/ModemManager/
%dir %_libdir/ModemManager/
%dir %_libdir/ModemManager/fcc-unlock.d/
%dir %_libdir/ModemManager/connection.d/

%_libdir/ModemManager/*.so
%_sbindir/*
%_bindir/mmcli
%_datadir/%name/
%_datadir/bash-completion/completions/mmcli
%_sysconfdir/dbus-1/system.d/*.conf
/lib/udev/rules.d/*
%_iconsdir/hicolor/*/apps/*
%_datadir/polkit-1/actions/*.policy
%_unitdir/*.service
%doc %_man1dir/*.*
%doc %_man8dir/*.*

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc
%_datadir/dbus-1/interfaces/*.xml

%files devel-doc
%doc %_datadir/gtk-doc/html/%name

%files -n libmm-glib
%_libdir/libmm-glib.so.*

%files -n libmm-glib-devel
%_libdir/libmm-glib.so
%_includedir/libmm-glib
%_pkgconfigdir/mm-glib.pc

%files -n libmm-glib-devel-doc
%doc %_datadir/gtk-doc/html/libmm-glib

%if_enabled introspection
%files -n libmm-glib-gir
%_libdir/girepository-1.0/ModemManager-1.0.typelib

%files -n libmm-glib-gir-devel
%_datadir/gir-1.0/ModemManager-1.0.gir
%endif

%if_enabled vala
%files -n libmm-glib-vala
%_datadir/vala/vapi/*
%endif

%changelog
* Tue Nov 15 2022 Mikhail Efremov <sem@altlinux.org> 1.20.2-alt1
- Updated to 1.20.2.

* Tue Nov 08 2022 Mikhail Efremov <sem@altlinux.org> 1.20.0-alt1
- Use %%post_service_posttrans_restart macro.
- Use meson build system.
- Updated to 1.20.0.

* Mon Sep 12 2022 Mikhail Efremov <sem@altlinux.org> 1.18.12-alt1
- Updated to 1.18.12.

* Tue Jun 28 2022 Mikhail Efremov <sem@altlinux.org> 1.18.10-alt1
- Patch from upstream:
   + mm-sms-part-3gpp: sms_decode_text: avoid decoding an empty.
- Updated to 1.18.10.

* Wed May 11 2022 Mikhail Efremov <sem@altlinux.org> 1.18.8-alt1
- Moved DBus interface xml files to devel subpackage.
- Updated to 1.18.8.

* Tue Feb 15 2022 Mikhail Efremov <sem@altlinux.org> 1.18.6-alt1
- Updated to 1.18.6.

* Thu Dec 09 2021 Mikhail Efremov <sem@altlinux.org> 1.18.4-alt1
- Updated to 1.18.4.

* Tue Sep 21 2021 Mikhail Efremov <sem@altlinux.org> 1.18.2-alt1
- Updated to 1.18.2.

* Wed Sep 15 2021 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt1
- Disabled tests.
- Explicitly enabled libqrtr-glib support.
- Do not add --no-as-needed to LDFLAGS.
- Dropped autoconf-archive from BR.
- Updated to 1.18.0.

* Fri Aug 13 2021 Mikhail Efremov <sem@altlinux.org> 1.16.10-alt1
- Updated to 1.16.10.

* Tue Jul 13 2021 Mikhail Efremov <sem@altlinux.org> 1.16.8-alt1
- Updated to 1.16.8.

* Tue Jun 08 2021 Mikhail Efremov <sem@altlinux.org> 1.16.6-alt1
- Disabled gtkdocize in autoreconf.
- Updated to 1.16.6.

* Thu Apr 22 2021 Mikhail Efremov <sem@altlinux.org> 1.16.4-alt1
- Updated to 1.16.4.

* Tue Mar 02 2021 Mikhail Efremov <sem@altlinux.org> 1.16.2-alt1
- BR: require autoconf-archive >= 2021.02.19-alt1.
- Dropped workaround for --no-as-needed.
- Updated to 1.16.2.

* Wed Feb 24 2021 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt1
- Dropped --no-as-needed from LD_FLAGS.
- Added python3 modules to BR for tests.
- Fixed configure option.
- Updated to 1.16.0.

* Fri Jan 22 2021 Mikhail Efremov <sem@altlinux.org> 1.14.10-alt1
- Updated to 1.14.10.

* Wed Nov 18 2020 Mikhail Efremov <sem@altlinux.org> 1.14.8-alt1
- Updated Url and Vcs tags.
- Updated to 1.14.8.

* Fri Oct 16 2020 Mikhail Efremov <sem@altlinux.org> 1.14.6-alt1
- Updated to 1.14.6.

* Tue Sep 22 2020 Mikhail Efremov <sem@altlinux.org> 1.14.2-alt1
- Updated to 1.14.2.

* Mon Jul 27 2020 Mikhail Efremov <sem@altlinux.org> 1.14.0-alt1
- Added autoconf-archive to BR.
- Updated to 1.14.0.

* Tue May 12 2020 Mikhail Efremov <sem@altlinux.org> 1.12.10-alt1
- Updated to 1.12.10.

* Wed Mar 18 2020 Mikhail Efremov <sem@altlinux.org> 1.12.8-alt1
- Updated to 1.12.8.

* Fri Feb 14 2020 Mikhail Efremov <sem@altlinux.org> 1.12.6-alt1
- Updated to 1.12.6.

* Tue Jan 21 2020 Mikhail Efremov <sem@altlinux.org> 1.12.4-alt1
- Updated to 1.12.4.

* Tue Dec 24 2019 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt1
- Don't use rpm-build-licenses.
- Updated to 1.12.2.

* Wed Nov 06 2019 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1
- Updated to 1.12.0.

* Tue Nov 05 2019 Mikhail Efremov <sem@altlinux.org> 1.10.8-alt1
- Updated to 1.10.8.

* Thu Sep 12 2019 Mikhail Efremov <sem@altlinux.org> 1.10.6-alt1
- Updated to 1.10.6.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt1
- Update url.
- Updated to 1.10.4.

* Thu Jun 13 2019 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- Make tests conditional.
- Updated to 1.10.2.

* Thu Jan 17 2019 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Updated to 1.10.0.

* Thu Jan 10 2019 Mikhail Efremov <sem@altlinux.org> 1.9.990-alt1
- Disabled silent rules.
- Updated to 1.9.990 (1.10-rc1).

* Mon Sep 24 2018 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt1
- Fix changelog entry.
- Updated to 1.8.2.

* Mon Jun 04 2018 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Drop init script.
- Updated to 1.8.0.
- Use %%e2k macro.

* Tue Mar 27 2018 Mikhail Efremov <sem@altlinux.org> 1.7.991-alt1
- Updated to 1.7.991 (1.8-rc2).

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 1.7.990-alt2
- Patch from upstream:
    + don't depend on GLib in ModemManager headers (closes: #34491).
- Drop intltool from BR.

* Fri Jan 26 2018 Mikhail Efremov <sem@altlinux.org> 1.7.990-alt1
- Updated to 1.7.990 (1.8-rc1).

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 1.6.12-alt1
- Updated to 1.6.12.

* Fri Oct 20 2017 Mikhail Efremov <sem@altlinux.org> 1.6.10-alt1
- Updated to 1.6.10.

* Wed Jul 05 2017 Mikhail Efremov <sem@altlinux.org> 1.6.8-alt1
- Patches from upstream:
  + libmm-glib,voice: fix object unref in
    list_call_context_complete_and_free.
  + libmm-glib,modem: fix object unref in
    list_bearers_context_complete_and_free.
  + libmm-glib,messaging: fix object unref in
    list_sms_context_complete_and_free.
- Updated to 1.6.8.

* Tue Nov 15 2016 Mikhail Efremov <sem@altlinux.org> 1.6.4-alt1
- Updated to 1.6.4.

* Mon Sep 19 2016 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Tue Jul 26 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Tue Jul 19 2016 Mikhail Efremov <sem@altlinux.org> 1.5.993-alt1
- Enable suspend/resume support (systemd).
- Updated to 1.5.993 (1.6-rc4).

* Thu Jun 09 2016 Mikhail Efremov <sem@altlinux.org> 1.5.992-alt1.git20160601
- Upstream git snapshot (1.6-rc3 with updates from master branch).

* Tue Oct 27 2015 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt1
- Updated to 1.4.12.

* Tue Jul 14 2015 Mikhail Efremov <sem@altlinux.org> 1.4.10-alt1
- Updated to 1.4.10.

* Tue Apr 28 2015 Mikhail Efremov <sem@altlinux.org> 1.4.8-alt1
- Updated to 1.4.8.

* Mon Mar 23 2015 Mikhail Efremov <sem@altlinux.org> 1.4.6-alt1
- Updated to 1.4.6.

* Fri Feb 13 2015 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Mon Jan 19 2015 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1
- Updated to 1.4.2.

* Wed Aug 27 2014 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Wed Aug 06 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3
- Don't restart service during upgrade.
- Rebuild with libmbim-glib-1.10.0.

* Thu Apr 03 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- Use post_service/preun_service.
- Add init script.

* Fri Jan 31 2014 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Wed Dec 18 2013 Mikhail Efremov <sem@altlinux.org> 1.1.900-alt1
- Fixes from upstream git:
  + iface-modem: fix crash in
    wait_for_final_state_context_complete_and_free.
  + broadband-modem-qmi: fix segfault when using AT-fallback mode
    for messaging.
- Enable gobject-introspection.
- Drop dia from BR.
- Fix URL.
- Updated to 1.1.900 (1.2-rc1).

* Fri Sep 06 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with libqmi-glib-1.6.0.

* Mon Jul 22 2013 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- tests: Fix DSO linking.
- Drop ModemManager-launcher script.
- Updated to 1.0.0.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 0.7.991-alt1
- Updated to 0.7.991.

* Tue Jun 04 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130531
- Build with MBIM support.
- Upstream git snapshot (master branch).

* Tue Apr 23 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130422
- Upstream git snapshot (master branch).

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130326
- Preset/disable MM service in case of systemd.
- Upstream git snapshot (master branch).

* Tue Mar 05 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130304
- Start ModemManager on non-systemd systems.
- Package doc subpackages as noarch.
- Upstream git snapshot (master branch).

* Mon Feb 25 2013 Mikhail Efremov <sem@altlinux.org> 0.7.990-alt1.git20130225
- upstream git snapshot (master branch).

* Tue Feb 19 2013 Mikhail Efremov <sem@altlinux.org> 0.6.0.0-alt1.git20130215
- upstream git snapshot (MM_06 branch).

* Sun Sep 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt1
- Updated to 0.5.4.0.

* Fri Jul 20 2012 Mikhail Efremov <sem@altlinux.org> 0.5.3.96-alt1
- Updated to 0.5.3.96 (0.5.4-rc2).

* Tue Apr 03 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt2
- Patches from upstream git:
  + option: hso_get_cid() always returns >= 0.
  + serial: fix crash when sending some commands to a closed port.
  + gsm: define the PPP auth preferences for STATIC and DHCP device use.

* Mon Mar 19 2012 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Thu Mar 01 2012 Mikhail Efremov <sem@altlinux.org> 0.5.1.97-alt1
- Updated to 0.5.1.97 (0.5.2 RC).

* Thu Dec 08 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20111208
- upstream git snapshot (MM_05 branch).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20110821
- upstream git snapshot (0.5 release and some bugfixes).

* Mon Aug 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4.998-alt1.git20110728
- upstream git snapshot (MM_05 branch) (closes: #25834).

* Fri Jun 24 2011 Mikhail Efremov <sem@altlinux.org> 0.4.997-alt1.git20110624
- upstream git snapshot (MM_05 branch) (closes: #25766).

* Sun May 01 2011 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20110501
- upstream git snapshot

* Tue Nov 30 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20101130
- upstream git snapshot

* Wed Sep 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100922
- upstream git snapshot (#23978 may be closed).

* Mon Sep 06 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100906
- upstream git snapshot

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100722
- upstream git snapshot

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20100628
- upstream git snapshot

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.3.997-alt1
- 0.3.997 (0.4-beta1)

* Tue Apr 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100427
- upstream git snapshot

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100227
- upstream git snapshot

* Fri Feb 05 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20100204
- upstream git snapshot

* Mon Jan 18 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt3.git20100105
- get version of pppd during build.

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20100105
- BuildRequire ppp-devel.
- upstream git snapshot

* Fri Dec 25 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt2.git20091225
- upstream git snapshot

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2.997-alt1
- 0.2.997

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091124
- upstream git snapshot

* Mon Oct 26 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt2.git20091026
- upstream git snapshot

* Mon Feb 09 2009 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- initial build for Sisyphus

