%global repo dpa-ext-gnomekeyring

Name: deepin-polkit-agent-ext-gnomekeyring
Version: 6.0.1
Release: alt1
Summary: GNOME keyring extension for Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++ cmake dqt5-base-devel dqt5-tools-devel libsecret-devel deepin-polkit-agent-devel

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DAPP_VERSION=%version \
  -DVERSION=%version \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %repo

%files -f %repo.lang
%dir %_libexecdir/polkit-1-dde/
%dir %_libexecdir/polkit-1-dde/plugins/
%_libexecdir/polkit-1-dde/plugins/lib%repo.so
%_datadir/%repo/

%changelog
* Thu May 23 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.1-alt1
- New version 6.0.1.
- Built via separate qt5 instead system (ALT #48138).

* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- New version (5.0.11).

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus.
