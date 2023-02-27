%global repo dpa-ext-gnomekeyring

Name: deepin-polkit-agent-ext-gnomekeyring
Version: 5.0.11
Release: alt1
Summary: GNOME keyring extension for Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/%repo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildPreReq: rpm-build-ninja
BuildRequires: gcc-c++ cmake qt5-base-devel qt5-tools-devel libsecret-devel deepin-polkit-agent-devel

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_qt5_bindir:$PATH
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
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
* Mon Feb 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- New version (5.0.11).

* Thu Mar 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.4-alt1
- Initial build for ALT Sisyphus.
