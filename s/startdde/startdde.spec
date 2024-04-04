%def_disable clang
%def_without dlightdm

Name: startdde
Version: 6.0.14
Release: alt1
Epoch: 1
Summary: Starter of deepin desktop environment
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/startdde
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Source1: vendor.tar

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-golang /proc
BuildRequires: jq glib2-devel libgio-devel libgtk+3-devel libXcursor-devel libXfixes-devel libXi-devel libgudev-devel libgnome-keyring-devel libpulseaudio-devel libalsa-devel libsecret-devel

%if_with dlightdm
Requires: deepin-session-shell
%endif

%description
Startdde is used for launching DDE components and invoking user's custom applications which compliant with xdg autostart specification.

%prep
%setup
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
export GOPATH="$(pwd)/vendor:%go_path"
# export GO_BUILD_FLAGS=-trimpath
%make

%install
export GOPATH="%go_path"
%makeinstall DESTDIR=%buildroot
%if_without dlightdm
# conflict with system lightdm
rm -rf %buildroot%_datadir/lightdm/lightdm.conf.d/60-deepin.conf
%endif
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_sbindir/deepin-fix-xauthority-perm
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/greeter-display-daemon
%dir %_datadir/%name/
%_datadir/%name/filter.conf
%_datadir/glib-2.0/schemas/com.deepin.dde.display.gschema.xml
%_userunitdir/dde-display-task-refresh-brightness.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-display-task-refresh-brightness.service
%if_with dlightdm
%_datadir/lightdm/lightdm.conf.d/60-deepin.conf
%endif

%changelog
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
