Name: zathura-pdf-mupdf
Version: 0.4.4
Release: alt1

Summary: PDF support for zathura (mupdf)
License: Zlib
Group: Office

URL: https://pwmt.org/projects/zathura-pdf-mupdf
Vcs: https://github.com/pwmt/zathura-pdf-mupdf.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: libgirara-devel zathura-devel >= 0.5.2
BuildRequires: libcairo-devel
BuildRequires: libmupdf-devel >= 1.24
# For tests
%{?!_without_check:%{?!_disable_check:BuildRequires: desktop-file-utils libappstream-glib}}

Requires: zathura

%define _unpackaged_files_terminate_build 1

%description
The zathura-pdf-mupdf plugin adds PDF support to zathura by using
the mupdf rendering library.

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
%_desktopdir/*.desktop
%_libdir/zathura/*.so
%_datadir/metainfo/*.xml

%changelog
* Sun Jan 12 2025 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Fixed build with mupdf >= 1.18.
- Enabled tests.
- Added Vcs tag.
- Fixed License tag.
- Updated Url tag.
- Updated to 0.4.4.

* Tue Feb 15 2022 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Tue Oct 23 2018 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Updated to 0.3.4.

* Thu Jul 24 2014 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Initial build.
