%define _unpackaged_files_terminate_build 1

Name: sigviewer
Version: 0.7.2
Release: alt1
Summary: SigViewer is a viewing application for biosignals
Group: Sciences/Medicine
License: GPL-3.0+
Url: https://github.com/cbrnr/sigviewer
VCS: https://github.com/cbrnr/sigviewer.git
Source: %name-%version.tar

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt6 rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++
BuildRequires: qt6-base-devel qt6-svg-devel qt6-tools-devel
BuildRequires: biosig-devel libxdf-devel zlib-devel

%description
SigViewer is a viewing application for biosignals such as EEG or MEG time series.
In addition to viewing raw data, SigViewer can also create, edit,
and display event information (such as annotations or artifact selections).

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
%find_lang --with-qt %name

%check
QT_QPA_PLATFORM=offscreen ctest --test-dir %_cmake__builddir --output-on-failure

%files -f %name.lang
%doc LICENSE
%doc README.md
%_bindir/%name
%_pixmapsdir/%{name}128.png
%_pixmapsdir/%{name}.svg
%_desktopdir/%{name}.desktop

%changelog
* Thu Sep 03 2026 Anton Farygin <rider@altlinux.org> 0.7.2-alt1
- 0.6.4 -> 0.7.2
- Switched to CMake build system and Qt6.
- Build against system libbiosig and libxdf instead of bundled ones.
- Power Spectrum/Mean: show one warning for events too close to the start
  of the file instead of a modal box per event and channel (closes: 40696).

* Tue Sep 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt5.git.f62f8d9
- Fixed typo in translation.

* Tue Sep 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt4.git.f62f8d9
- Added translation by Sergey Kazorin.
- Fixed issues related to translation.

* Mon Aug 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt3.git.f62f8d9
- Installed and enabled translations.

* Mon Aug 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt2.git.f62f8d9
- Fixed crashes in Power Spectrum tool.

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.4-alt1.git.f62f8d9
- Initial build for ALT.
