%def_without clang
%def_with docs

%define repo dde-app-services

Name: deepin-app-services
Version: 1.0.29
Release: alt4
Epoch: 1

Summary: Service collection of DDE applications

License: LGPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dde-app-services
Vcs: https://github.com/linuxdeepin/dde-app-services

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake libdtk6widget-devel libgtest-devel libcups-devel libwayland-client-devel
%if_with docs
BuildRequires: doxygen dqt6-base-doc dqt6-tools-devel
BuildRequires: libdqt6-help
%endif

%description
%summary.

%if_with docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch

%description doc
This package provides %name documantation.
%endif

%prep
%setup -n %repo-%version
%autopatch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%DQ6build \
  -DDTK_VERSION="6" \
  -DDVERSION=%version \
%if_with docs
  -DBUILD_DOCS=ON \
  -DQCH_INSTALL_DESTINATION=%_dqt6_docdir \
%else
  -DBUILD_DOCS=OFF \
%endif
#

%install
%DQ6install
chmod +x %buildroot%_datadir/bash-completion/completions/dde-dconfig
%find_lang --output=%name.lang dde-dconfig dde-dconfig-editor

%files -f %name.lang
%doc LICENSE README.md debian/changelog
%_bindir/dde-dconfig*
%_sysusersdir/dde-dconfig-daemon.conf
%_datadir/dbus-1/interfaces/org.desktopspec.ConfigManager*.xml
%_datadir/dbus-1/system.d/org.desktopspec.ConfigManager.conf
%_datadir/dbus-1/system-services/org.desktopspec.ConfigManager.service
# package translations outside %%find_lang
%dir %_datadir/dde-dconfig/
%dir %_datadir/dde-dconfig/translations/
%_datadir/dde-dconfig/translations/dde-dconfig_zh_CN.qm
%dir %_datadir/dde-dconfig-editor/
%dir %_datadir/dde-dconfig-editor/translations/
%_datadir/dde-dconfig-editor/translations/dde-dconfig-editor_zh_CN.qm
# ---
%_unitdir/dde-dconfig-daemon.service
%_datadir/bash-completion/completions/dde-dconfig
%_datadir/zsh/vendor-completions/_dde-dconfig
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dconfig-example/
%dir %_datadir/dsg/configs/dconfig-example/a/
%dir %_datadir/dsg/configs/overrides/
%dir %_datadir/dsg/configs/overrides/dconfig-example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/a/
%_datadir/dsg/configs/dconfig-example/example.json
%_datadir/dsg/configs/dconfig-example/a/example.json
%_datadir/dsg/configs/example.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.a.json
%_datadir/dsg/configs/overrides/dconfig-example/example/a/dconf-example.override.a.json

%if_with docs
%files doc
%_dqt6_docdir/dde-dconfig-doc.qch
%endif

%changelog
* Mon Jun 15 2026 Leontiy Volodin <lvol@altlinux.org> 1:1.0.29-alt4
- Fixed build on dqt6-declarative 6.10.3.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 1:1.0.29-alt3
- Fixed build on dtk 6.7.31.

* Mon Aug 25 2025 Leontiy Volodin <lvol@altlinux.org> 1:1.0.29-alt2
- Reverted the stable version.
- Fixed dde-dconfig-daemon startup.

* Thu Aug 21 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.35-alt1
- New version 1.0.35.
- Excluded linglong.

* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.34-alt1
- New version 1.0.34.

* Thu Apr 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.29-alt1
- New version 1.0.29.
- Added vcs tag.
- Switched to dqt6.

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt3
- Built via separate qt5 instead system (ALT #48138).

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt2
- Applied usrmerge.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt1
- New version 1.0.25.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.24.0.2.3acd-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.24.0.2.3acd-alt1
- New version 1.0.24-2-g3acd198.

* Fri Oct 20 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.23-alt1
- New version 1.0.23.

* Mon Mar 13 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.22-alt1
- New version.

* Wed Feb 22 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.21-alt1
- New version.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.20-alt2
- Fixed build with dtkgui 5.6.4.

* Tue Dec 13 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.20-alt1
- Initial build for ALT Sisyphus.
