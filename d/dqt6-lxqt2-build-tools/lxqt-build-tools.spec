# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: dqt6-lxqt2-build-tools
Version: 2.4.0
Release: alt0.dde.1

Summary: Various packaging tools and scripts for LXQt applications
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/lxqt/lxqt-build-tools
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: dqt6-base-devel dqt6-tools-devel glib2-devel

%description
%summary.
That used to lurk in liblxqt or got spread over other subprojects.

%prep
%setup
%patch -p1

%ifarch %e2k
# lcc has -fwhole, to be tested though
sed -i '/-flto/d' cmake/modules/LXQtCompilerSettings.cmake
%endif

%build
%cmake \
  -DCMAKE_PREFIX_PATH=%_dqt6_libdir/cmake \
  -DCMAKE_INSTALL_BINDIR=%_dqt6_bindir \
  -DCMAKE_INSTALL_DATAROOTDIR=%_dqt6_datadir \
#
%cmake_build

%install
%cmake_install

%files
%doc BSD-3-Clause AUTHORS CHANGELOG README.md
%_dqt6_datadir/cmake/lxqt2-build-tools
%_dqt6_bindir/lxqt2-transupdate

%changelog
* Thu Sep 17 2026 Leontiy Volodin <lvol@altlinux.org> 2.4.0-alt0.dde.1
- Forked for independent deepin buildings (for deepin-qt6integration).

* Mon Apr 20 2026 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Wed Nov 05 2025 Anton Midyukov <antohami@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Sat Jun 21 2025 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- New version 2.2.1.

* Thu Apr 17 2025 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1
- New version 2.2.0.

* Fri Nov 08 2024 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version
- Fix typo in License tag

* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- initial build
