%def_enable clang

Name: startdde
Version: 6.1.6
Release: alt4
Epoch: 1

Summary: Starter of deepin desktop environment

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Vcs: https://github.com/linuxdeepin/startdde

# Source-url: https://github.com/linuxdeepin/startdde/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-golang /proc
BuildRequires: glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel libsecret-devel

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup -a1
%autopatch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
export GOPATH="$(pwd)/vendor:%go_path"
%make

%install
export GOPATH="%go_path"
%makeinstall DESTDIR=%buildroot
# fix conflicts with deepin-daemon 6.1.44
rm -rf %buildroot%_libexecdir/deepin-daemon/
rm -rf %buildroot%_datadir/glib-2.0/schemas/com.deepin.dde.display.gschema.xml
rm -rf %buildroot%_userunitdir/dde-display-task-refresh-brightness.service
rm -rf %buildroot%_userunitdir/dde-session-initialized.target.wants/
rm -rf %buildroot%_datadir/lightdm/lightdm.conf.d/60-deepin.conf
# package localization files
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_sbindir/deepin-fix-xauthority-perm
%dir %_datadir/%name/
%_datadir/%name/filter.conf
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.startdde/
%dir %_datadir/dsg/configs/org.deepin.startdde/org.deepin.XSettings.json
%dir %_datadir/dsg/configs/org.deepin.startdde/org.deepin.Display.json

%changelog
* Mon Apr 27 2026 Leontiy Volodin <lvol@altlinux.org> 1:6.1.6-alt4
- Built via clang (failed on gcc15).

* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.1.6-alt3
- Removed subpackage: lightdm-deepin-greeter-settings.

* Fri Jul 18 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.1.6-alt2
- Fixed conflicts with deepin-daemon 6.1.44.

* Thu Apr 17 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.1.6-alt1
- New version 6.1.6.

* Tue Feb 18 2025 Leontiy Volodin <lvol@altlinux.org> 1:6.1.2-alt1
- New version 6.1.2.
- Added vcs tag.
- Packaged the lightdm config as subpackage.

* Thu Apr 04 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.14-alt1
- New version 6.0.14.

* Thu Feb 29 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.13-alt1
- New version 6.0.13.
- Used system lightdm instead lightdm-deepin-greeter again (ALT #49028).

* Fri Nov 24 2023 Leontiy Volodin <lvol@altlinux.org> 1:6.0.11-alt1
- New version 6.0.11.
- Used independent vendoring of submodules again.
- Used own modification of lightdm.

* Wed Jan 25 2023 Leontiy Volodin <lvol@altlinux.org> 1:5.10.2-alt1
- New version (5.10.2).

* Fri Dec 23 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.10.1-alt1
- New version (5.10.1).
- spec:
  + Included org.deepin.Display.json.
- Upstream:
  + Fixed the brightness and broken org.desktopspec.ConfigManager.

* Thu Sep 01 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.9.51-alt1
- New version (5.9.51).
- Fixed UIAppSched detection.

* Thu Feb 17 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.8.31-alt1.gita7a2b88
- Checkout to master branch.
- Updated from commit a7a2b887399d78bc03345ccbaf3f49887d81f604.

* Fri Feb 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.55-alt1
- New version (5.8.55).
- Built with internal golang submodules.

* Fri May 21 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.9-alt1
- New version (5.8.9) with rpmgs script.

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.7-alt2
- Fixed build with deepin-polkit-agent.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.7-alt1
- New version (5.8.7) with rpmgs script.

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.4-alt1
- New version (5.8.4) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.35.1-alt1
- New version (5.6.0.35.1) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.0.35-alt1
- New version (5.6.0.35) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.34-alt1
- New version (5.6.0.34) with rpmgs script.
- Fixed paths.

* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.30-alt1
- New version (5.6.0.30) with rpmgs script.

* Tue Oct 13 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt2
- Fixed conflict with lightdm.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.11-alt1
- New version (5.6.0.11) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.0.0-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
