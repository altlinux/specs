%define _unpackaged_files_terminate_build 1

Name: zathura-ps
Version: 0.2.8
Release: alt1

Summary: PostScript support for zathura
License: Zlib
Group: Office

URL: https://pwmt.org/projects/%name/
Vcs: https://github.com/pwmt/zathura-ps.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: libgirara-devel zathura-devel
BuildRequires: intltool libcairo-devel libspectre-devel
# For tests
%{?!_without_check:%{?!_disable_check:BuildRequires: desktop-file-utils libappstream-glib}}

Requires: zathura

%description
The zathura-ps plugin adds PostScript support to zathura by using
the libspectre library.

%prep
%setup
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc AUTHORS LICENSE
%_libdir/zathura/*.so
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml

%changelog
* Wed Aug 14 2024 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1
- Updated Vcs tag.
- Enabled tests.
- Updated to 0.2.8.

* Wed Dec 13 2023 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt3
- Rebuild with zatura-0.5.4.

* Tue Nov 29 2022 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt2
- Rebuild with zatura-0.5.2.

* Thu Jul 15 2021 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt2
- Used Vcs tag.
- Fixed license.
- Fixed URL.

* Thu Apr 19 2018 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Wed Dec 23 2015 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Updated to 0.2.3.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt3
- Rebuild with libgirara-0.2.4.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2
- Rebuild with new libgirara and zathura for GTK+3.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Package LICENSE.
- Updated to 0.2.2.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Fri Jun 15 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt2
- Rebuild with zathura-0.1.2.

* Wed Mar 21 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

