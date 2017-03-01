%def_enable daemon
%def_enable session_helper
%def_enable reverse
%def_enable introspection
%def_enable vala
%def_enable print_profiles
%def_disable bash_completion
%def_enable installed_tests
%def_enable libcolordcompat

%define _libexecdir %_prefix/libexec
%define _icccolordir %_datadir/color/icc
%define _localstatedir %_var

Name: colord
Version: 1.3.5
Release: alt1

Summary: Color daemon
License: GPLv2+
Group: Graphics
URL: http://www.freedesktop.org/software/%name/

Source: http://www.freedesktop.org/software/%name/releases/colord-%version.tar.xz

%define colord_group %name
%define colord_user %name
%define glib_ver 2.36
%define polkit_ver 0.113-alt2
%define lcms_ver 2.6
%define gusb_ver 0.2.2
%define bash_completion_ver 2.0

Requires: lib%name = %version-%release

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: docbook-utils gtk-doc intltool libdbus-devel libgudev-devel libudev-devel
BuildRequires: liblcms2-devel >= %lcms_ver libpolkit-devel >= %polkit_ver
BuildRequires: libsqlite3-devel libusb-devel libgusb-devel >= %gusb_ver systemd-devel libsystemd-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgusb-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_print_profiles:BuildRequires: argyllcms}
%{?_enable_bash_completion:BuildRequires: bash-completion > %bash_completion_ver}
# for check
BuildRequires: /proc dbus-tools-gui valgrind

%description
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

%package -n lib%name
Summary: Colord shared library
Group: System/Libraries

%description -n lib%name
This package provides shared library for Colord to work.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Obsoletes: %name-devel
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
colord is a low level system activated daemon that maps color devices to color
profiles in the system context.

This package provides development files for Colord library.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n lib%name-vala
Summary: Vala Bindings for lib%name
Group: Development/C
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings for %name library

%package extra-profiles
Summary: Color profiles for color management that are less commonly used
Group: Graphics
Requires: %name = %version-%release
BuildArch: noarch

%description extra-profiles
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%package tests
Summary: Tests for the Colord
Group: Development/Other
Requires: lib%name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Golord.

%prep
%setup

%build
%configure --disable-static \
	--disable-rpath \
	%{subst_enable daemon} \
	%{?_enable_session_helper:--enable-session-helper} \
	%{subst_enable reverse} \
	%{subst_enable vala} \
	--with-daemon-user=%colord_user \
	%{?_enable_print_profiles:--enable-print-profiles} \
	%{?_disable_bash_completion:--disable-bash-completion} \
	%{?_enable_installed_tests:--enable-installed-tests} \
	%{subst_enable libcolordcompat}

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_localstatedir/lib/{%name,color}/icc

# databases
touch %buildroot%_localstatedir/lib/%name/mapping.db
touch %buildroot%_localstatedir/lib/%name/storage.db

%find_lang %name

%check
#%make check

%pre
%_sbindir/groupadd -r -f %colord_group 2>/dev/null ||:
%_sbindir/useradd -r -n -g %colord_group -d %_localstatedir/%name \
	-s /dev/null -c "User for colord" %colord_user 2>/dev/null ||:

%files -f %name.lang
%_bindir/*
#%config %_sysconfdir/%name.conf
%_datadir/glib-2.0/schemas/org.freedesktop.ColorHelper.gschema.xml
%_libexecdir/%name
%_libexecdir/colord-session
%_sysconfdir/dbus-1/system.d/org.freedesktop.ColorManager.conf
%_datadir/dbus-1/interfaces/org.freedesktop.ColorManager*.xml
%_datadir/dbus-1/system-services/org.freedesktop.ColorManager.service
%_datadir/polkit-1/actions/org.freedesktop.color.policy
/lib/udev/rules.d/*.rules
%_tmpfilesdir/%name.conf

%if_enabled session_helper
%_datadir/dbus-1/interfaces/org.freedesktop.ColorHelper.xml
%_datadir/dbus-1/services/org.freedesktop.ColorHelper.service
%_prefix/lib/systemd/user/%name-session.service
%endif

%dir %_libdir/colord-sensors
%_libdir/colord-sensors/libcolord_sensor_dummy.so
%_libdir/colord-sensors/libcolord_sensor_huey.so
%_libdir/colord-sensors/libcolord_sensor_colorhug.so
%_libdir/colord-sensors/libcolord_sensor_argyll.so
%_libdir/colord-sensors/libcolord_sensor_dtp94.so
%_libdir/colord-sensors/libcolord_sensor_spark.so
%_libdir/colord-sensors/libdtp94-private.so
%_libdir/colord-sensors/libhuey-private.so
%_libdir/colord-sensors/libmunki-private.so
%_libdir/colord-sensors/libospark-private.so

%dir %_libdir/colord-plugins
%_libdir/colord-plugins/libcd_plugin_camera.so
%_libdir/colord-plugins/libcd_plugin_scanner.so
%_datadir/%name/
%_man1dir/cd-create-profile.1.*
%_man1dir/colormgr.*
%_man1dir/cd-fix-profile.*
%_man1dir/cd-it8.1.*
#%_man1dir/colord.conf.1.*
%attr(755,%colord_user,%colord_group) %dir %_localstatedir/lib/%name
%attr(755,%colord_user,%colord_group) %dir %_localstatedir/lib/%name/icc
%dir %_localstatedir/lib/color
%dir %_localstatedir/lib/color/icc
%ghost %_localstatedir/lib/%name/*.db
%systemd_unitdir/*.service
%{?_enable_bash_completion:%_datadir/bash-completion/completions/colormgr}

%exclude %_libdir/%name-sensors/*.la
%exclude %_libdir/colord-plugins/*.la

# common colorspaces from shared-color-profiles
%dir %_icccolordir/colord
%_icccolordir/colord/AdobeRGB1998.icc
%_icccolordir/colord/AppleRGB.icc
%_icccolordir/colord/CIE-RGB.icc
%_icccolordir/colord/ColorMatchRGB.icc
%_icccolordir/colord/NTSC-RGB.icc
%_icccolordir/colord/PAL-RGB.icc
%_icccolordir/colord/ProPhotoRGB.icc
%_icccolordir/colord/SMPTE-C-RGB.icc
%_icccolordir/colord/sRGB.icc

# so we can display at least something in the default dropdown
%if_enabled print_profiles
%_icccolordir/colord/FOGRA39L_coated.icc
%endif

# monitor test profiles
%_icccolordir/colord/Bluish.icc
%_icccolordir/colord/SwappedRedAndGreen.icc
%_icccolordir/colord/Gamma*.icc

# named color profiles
%_icccolordir/colord/x11-colors.icc

%files extra-profiles
%if_enabled print_profiles
%_icccolordir/colord/FOGRA27L_coated.icc
%_icccolordir/colord/FOGRA28L_webcoated.icc
%_icccolordir/colord/FOGRA29L_uncoated.icc
%_icccolordir/colord/FOGRA30L_uncoated_yellowish.icc
%_icccolordir/colord/FOGRA40L_SC_paper.icc
%_icccolordir/colord/FOGRA45L_lwc.icc
%_icccolordir/colord/FOGRA47L_uncoated.icc
%_icccolordir/colord/GRACoL*.icc
%_icccolordir/colord/IFRA26S_2004_newsprint.icc
%_icccolordir/colord/SNAP*.icc
%_icccolordir/colord/SWOP*.icc
%endif

# other colorspaces not often used
%_icccolordir/colord/BestRGB.icc
%_icccolordir/colord/BetaRGB.icc
%_icccolordir/colord/BruceRGB.icc
%_icccolordir/colord/DonRGB4.icc
%_icccolordir/colord/ECI-RGBv1.icc
%_icccolordir/colord/ECI-RGBv2.icc
%_icccolordir/colord/EktaSpacePS5.icc
%_icccolordir/colord/WideGamutRGB.icc

# other named color profiles not generally useful
%_icccolordir/colord/Crayons.icc

%files -n lib%name
%_libdir/libcolord.so.*
%_libdir/libcolordprivate.so.*
%_libdir/libcolorhug.so.*
%{?_enable_libcolordcompat:%_libdir/libcolordcompat.so}

%files -n lib%name-devel
%_includedir/colord-1/
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc
%_libdir/libcolordprivate.so
%_libdir/libcolorhug.so
%_pkgconfigdir/colorhug.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Colord-1.0.typelib
%_typelibdir/ColorHug-1.0.typelib

%files -n lib%name-gir-devel
%_girdir/Colord-1.0.gir
%_girdir/ColorHug-1.0.gir
%endif

%if_enabled vala
%files -n lib%name-vala
%_datadir/vala/vapi/%name.vapi
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif


%changelog
* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4

* Wed Jul 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Mar 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Fri Nov 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Wed Aug 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.12-alt1
- 1.2.12

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.11-alt1
- 1.2.11

* Thu Apr 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.10-alt1
- 1.2.10

* Sun Mar 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.9-alt1
- 1.2.9

* Thu Jan 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- 1.2.8

* Fri Dec 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.7-alt1
- 1.2.7

* Wed Nov 26 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Sun Oct 12 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sat Sep 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Aug 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu Apr 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0
- new -tests subpackage

* Thu Apr 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Mon Jan 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu Aug 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Jul 07 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Jun 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun May 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.34-alt1
- 0.1.34

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.33-alt1
- 0.1.33

* Sat Mar 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.31-alt1
- 0.1.31

* Mon Feb 18 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.30-alt1
- 0.1.30

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.29-alt1
- 0.1.29
- redefined %%_localstatedir to %%_var and removed corresponding patch

* Tue Jan 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.27-alt1
- 0.1.27
- no more required shared-color-profiles
- new -extra-profiles subpackage

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.26-alt1
- 0.1.26

* Tue Nov 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.25-alt1
- 0.1.25

* Tue Oct 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.24-alt1
- 0.1.24

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.23-alt1
- 0.1.23

* Sun Jul 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.22-alt1
- 0.1.22

* Wed May 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.21-alt1
- 0.1.21

* Sun May 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.20-alt1
- 0.1.20

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.19-alt1
- 0.1.19

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.18-alt1
- 0.1.18

* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.17-alt1
- 0.1.17

* Thu Feb 23 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt2
- fixed permission for %%_localstatedir/colord (ALT #26978)

* Wed Jan 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt1
- 0.1.16

* Sun Nov 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- 0.1.14

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt2
- fixed databases location
- packaged %%_localstatedir/colord/*.db as %%ghost
- added shared-color-profiles to rqs

* Sat Oct 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.13-alt1
- 0.1.13

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.12-alt1
- 0.1.12
- new lib%name-{gir,gir-devel,vala} subpackages

* Tue Aug 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Thu Apr 14 2011 Victor Forsiuk <force@altlinux.org> 0.1.5-alt1
- Initial build.

