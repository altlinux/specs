%define _unpackaged_files_terminate_build 1

# Tests disabled for now: they cause hasher-priv to freeze
%define _disable_check 1

%if %{expand:%%{!?_without_check:%%{!?_disable_check:1}}0}
%define tests enabled
%else
%define tests disabled
%endif

Name: zathura
Version: 0.5.8
Release: alt1

Summary: A lightweight document viewer
License: Zlib
Group: Office
Url: https://pwmt.org/projects/%name/
Vcs: https://github.com/pwmt/zathura.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: libgirara-devel >= 0.4.4-alt1
BuildRequires: intltool libgtk+3-devel libsqlite3-devel python3-module-docutils libmagic-devel zlib-devel
BuildRequires: libsynctex-devel
BuildRequires: libseccomp-devel
BuildRequires: libjson-glib-devel
# For man pages
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
# To create icons
BuildRequires: librsvg-utils
#For tests
%{?!_without_check:%{?!_disable_check:BuildRequires: xvfb-run libappstream-glib desktop-file-utils}}

Conflicts: zatura-pdf-poppler < 0.3.3-alt1
Conflicts: zatura-djvu < 0.2.10-alt1
Conflicts: zatura-ps < 0.2.8-alt1
Conflicts: zatura-cb < 0.1.11-alt1

%description
zathura is a highly customizable and functional document viewer based on
the girara user interface library and several document libraries.

This package contains ALT-specific changes so it is NOT original software
from https://pwmt.org.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+3-devel libgirara-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson \
	-Dtests=%tests

%meson_build -v

%install
%meson_install
#  Create directory for plugins
mkdir -p %buildroot%_libdir/zathura
%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc LICENSE AUTHORS README.md
%_bindir/%{name}*
%dir %_libdir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/*.xml
%_man1dir/*
%_man5dir/*
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%_datadir/fish/vendor_completions.d/*

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc
%_datadir/dbus-1/interfaces/org.pwmt.*

%changelog
* Wed Aug 14 2024 Mikhail Efremov <sem@altlinux.org> 0.5.8-alt1
- Updated to 0.5.8.

* Mon May 13 2024 Mikhail Efremov <sem@altlinux.org> 0.5.6-alt1
- Updated Vcs tag.
- Updated to 0.5.6.

* Sun Jan 14 2024 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt2
- Disabled tests.

* Wed Dec 13 2023 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- tests: Don't run xvfb tests in parallel.
- Enabled tests.
- Updated to 0.5.4.

* Tue Nov 29 2022 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Wed Sep 14 2022 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Moved DBus interface xml files to devel subpackage.
- Updated to 0.5.1.

* Tue Feb 15 2022 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1
- Dropped patch for old libmagic.
- Updated to 0.4.9.

* Thu Jul 15 2021 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt1
- Updated to 0.4.8.

* Wed Sep 09 2020 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt1
- Updated to 0.4.7.

* Mon Aug 03 2020 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1
- Updated to 0.4.6.

* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt1
- Added ALT-specific note to description.
- Used Vcs tag.
- Fixed licensde
- Updated to 0.4.5.

* Tue Sep 24 2019 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt2
- Enable libseccomp support.
- Generate and package icons.
- Enable libsynctex support.

* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Fix URL.
- Updated to 0.4.4.

* Mon Dec 24 2018 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Updated to 0.4.3.

* Tue Sep 25 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Install zsh completions to site-functions.

* Fri Sep 21 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Fri May 25 2018 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.3.8-alt1
- Fixed appdata location.
- Updated to 0.3.8.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1
- Updated to 0.3.6.

* Mon Feb 15 2016 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Drop obsoleted patch.
- Updated to 0.3.5.

* Mon Dec 21 2015 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Fix build without libsynctex.
- Updated to 0.3.4.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Nov 17 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt2
- Fix BR.

* Tue Nov 11 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Oct 24 2014 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Fri Oct 17 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Package appdata file.
- Updated to 0.3.0.

* Thu Jul 03 2014 Mikhail Efremov <sem@altlinux.org> 0.2.9-alt1
- Updated to 0.2.9.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Build with GTK+3.
- Re-fix build with current libmagic.
- Updated to 0.2.7.

* Tue Nov 26 2013 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Fri Aug 16 2013 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Fix build with current libmagic.
- Package LICENSE.
- Updated to 0.2.3.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Wed Jan 09 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Enable strict aliasing rules.
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.
- Disable strict aliasing rules.

* Fri Mar 16 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Wed Mar 09 2011 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.2-alt1
- 0.0.8.2-26-ga01ab17

* Tue Aug 10 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.1-alt1
- 0.0.8.1

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.7-alt1.1
- rebuilt with new poppler

* Tue Jun 22 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.7-alt1
- 0.0.7

* Thu Jun 03 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.5-alt1
- First build for ALT Linux Sisyphus

