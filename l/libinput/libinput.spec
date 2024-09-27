%def_disable snapshot

%define _libexecdir %_prefix/libexec
%def_enable libwacom
%def_enable debug_gui
%def_disable documentation
%def_enable tests
%def_enable install_tests

Name: libinput
Version: 1.26.2
Release: alt2.1

Summary: Input devices library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libinput/

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/%name/%name/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.freedesktop.org/libinput/libinput.git
Source: %name-%version.tar
%endif
# https://gitlab.freedesktop.org/rautyrauty/libinput/-/commit/8f6e08d8e5835dea8ae73a7ad86d22dc9403236c.patch
Patch10: libinput-1.26.2-up-ICL.patch
# https://gitlab.freedesktop.org/rautyrauty/libinput/-/commit/9305056bdf81cb1965f7edf3b458b665eb427f4f.patch
Patch11: libinput-1.26.2-up-N15i.patch

%add_python3_path %_libexecdir/%name

%define mtdev_ver 1.1.0
%define evdev_ver 1.10

BuildRequires(pre): rpm-macros-meson rpm-build-python3 pkgconfig(udev)
# for %%valgrind_arches
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: meson gcc-c++
BuildRequires: libmtdev-devel >= %mtdev_ver libevdev-devel >= %evdev_ver
BuildRequires: libudev-devel pkgconfig(systemd)
BuildRequires: libcheck-devel
%{?_enable_libwacom:BuildRequires: libwacom-devel}
%{?_enable_debug_gui:BuildRequires: wayland-protocols
%ifarch %e2k
BuildRequires: libgtk+3-devel
%else
BuildRequires: libgtk4-devel
%endif
}
%{?_enable_documentation:BuildRequires: doxygen graphviz}
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc gdb  python3-module-pytest python3-module-pytest-xdist
BuildRequires: python3-module-pyparsing
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input code
the user of libinput need to provide the common set of functionality
that users expect.

Input event processing includes scaling touch coordinates, generating
pointer events from touchpads, pointer acceleration, etc.

%package devel
Summary: libinput development package
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package tools
Summary: tools for %name
Group: Development/Tools
Requires: %name = %EVR

%description tools
This package contains commandline tools from %name package.

%package tools-gui
Summary: libinput visual debug helper
Group: Development/Tools
Requires: %name = %EVR
Requires: %name-tools = %EVR

%description tools-gui
This package contains visual debug helper for %name.

%package tests
Summary: Tests for libinput
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed libinput library.

%prep
%setup
%patch10 -p1
%patch11 -p1

%build
%meson %{subst_enable_meson_bool libwacom libwacom} \
       %{subst_enable_meson_bool debug_gui debug-gui} \
       %{subst_enable_meson_bool documentation documentation} \
       %{subst_enable_meson_bool tests tests} \
       %{subst_enable_meson_bool install_tests install-tests} \
       -Dudev-dir=%_udevdir
%meson_build

%install
%meson_install

%check
%__meson_test -t 4 --no-suite hardware --no-suite root

%files
%dir %_sysconfdir/%name
%_libdir/%name.so.*
%_udevdir/%name-device-group
%_udevdir/%name-fuzz-extract
%_udevdir/%name-fuzz-to-zero
%_datadir/%name/
%_udevrulesdir/80-%name-device-groups.rules
%_udevrulesdir/90-%name-fuzz-override.rules
%doc COPYING README*

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files tools
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name-analyze
%_libexecdir/%name/%name-analyze-buttons
%_libexecdir/%name/%name-analyze-per-slot-delta
%_libexecdir/%name/%name-analyze-recording
%_libexecdir/%name/%name-analyze-touch-down-state
%_libexecdir/%name/%name-debug-events
%_libexecdir/%name/%name-debug-tablet
%_libexecdir/%name/%name-list-devices
%_libexecdir/%name/%name-list-kernel-devices
%_libexecdir/%name/%name-measure
%_libexecdir/%name/%name-measure-fuzz
%_libexecdir/%name/%name-measure-touchpad-pressure
%_libexecdir/%name/%name-measure-touchpad-size
%_libexecdir/%name/%name-measure-touchpad-tap
%_libexecdir/%name/%name-measure-touch-size
%_libexecdir/%name/%name-quirks
%_libexecdir/%name/%name-record
%_libexecdir/%name/%name-replay
%_libexecdir/%name/%name-test
%_man1dir/%name.1.*
%_man1dir/%name-analyze.1*
%_man1dir/%name-analyze-buttons.1*
%_man1dir/%name-analyze-per-slot-delta.1*
%_man1dir/%name-analyze-recording.1*
%_man1dir/%name-analyze-touch-down-state.1*
%_man1dir/%name-debug-events.1.*
%_man1dir/%name-debug-tablet.1.*
%_man1dir/%name-list-devices.1.*
%_man1dir/%name-list-kernel-devices.1.*
%_man1dir/%name-measure.1.*
%_man1dir/%name-measure-fuzz.1.*
%_man1dir/%name-measure-touchpad-pressure.1.*
%_man1dir/%name-measure-touchpad-size.1*
%_man1dir/%name-measure-touchpad-tap.1.*
%_man1dir/%name-measure-touch-size.1.*
%_man1dir/%name-quirks.1.*
%_man1dir/%name-quirks-list.1.*
%_man1dir/%name-quirks-validate.1.*
%_man1dir/%name-record.1.*
%_man1dir/%name-replay.1.*
%_man1dir/%name-test.1.*
%_datadir/zsh/site-functions/_%{name}

%if_enabled debug_gui
%files tools-gui
%_libexecdir/%name/%name-debug-gui
%_man1dir/%name-debug-gui.1.*
%endif

%if_enabled install_tests
%files tests
%_libexecdir/%name/%name-test-suite
%_libexecdir/%name/%name-test-utils
%_man1dir/%name-test-suite.1.*
%endif

%changelog
* Fri Sep 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt2.1
- applied patch for Graviton N15i

* Fri Sep 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt2
- applied patch for ICL Si1516/Si1512 proposed in mr1054 (ALT ##44766,51497)

* Mon Aug 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt1
- 1.26.2

* Thu Jun 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.1-alt1
- 1.26.1

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1.1
- rebuilt with new systemd macros

* Thu Jun 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.25.0-alt1.1
- fixed build with disable=debug_gui

* Mon Jan 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.25.0-alt1
- 1.25.0

* Sun Oct 22 2023 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1.1
- fixed build debug-gui for %%e2k

* Fri Aug 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- 1.23.0

* Mon Jan 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1

* Sun Nov 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0
- new tests subpackage

* Sun Jun 12 2022 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1
- 1.21.0

* Wed Apr 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1 (fixed CVE-2022-1215)

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Mon Dec 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.19.3-alt1
- 1.19.3

* Thu Oct 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.19.2-alt1
- 1.19.2

* Tue Sep 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Tue Sep 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0

* Tue Aug 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Wed Jun 02 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Wed May 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1.17.3-alt1
- 1.17.3

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.17.2-alt1
- 1.17.2

* Wed Mar 24 2021 Yuri N. Sedunov <aris@altlinux.org> 1.17.1-alt1
- 1.17.1

* Tue Feb 23 2021 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.4-alt1
- 1.16.4

* Tue Nov 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Fri Oct 23 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Aug 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.6-alt1
- 1.15.6

* Sat Apr 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.5-alt1
- 1.15.5

* Wed Mar 18 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.4-alt1
- 1.15.4

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.3-alt1
- 1.15.3

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Mon Feb 03 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Mon Oct 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Thu Oct 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Mon Aug 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Aug 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Fri Jun 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.4-alt1
- 1.13.4

* Tue Jun 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.13.3-alt2
- Fixed build with disabled check.
- Enabled build of testsuite by default.

* Mon Jun 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.3-alt1
- 1.13.3

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt3
- glebfm@: Fixed testsuite on architectures not supported by valgrind,
           dropped redundant BR: libvalgrind-devel

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 1.13.2-alt2
- move to rpm-macros-valgrind

* Thu May 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.12.6-alt1
- 1.12.6

* Mon Jan 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.12.5-alt1
- 1.12.5

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- updated to 1.12.3-6-g4e469291

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Thu Oct 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Tue Sep 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Jul 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.7-alt1
- 1.10.7

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.6-alt1
- 1.10.6

* Thu Apr 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.5-alt1
- 1.10.5

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Wed Mar 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Tue Nov 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.3-alt1
- 1.9.3

* Wed Nov 15 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Jul 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0
- new tools-gui subpackage

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Apr 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Feb 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Feb 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Jan 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Aug 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Feb 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Feb 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Dec 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Aug 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jul 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Thu Jun 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Sep 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu May 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus



