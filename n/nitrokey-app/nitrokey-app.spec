%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_disable ubuntuicons

Name: nitrokey-app
Version: 1.4.2
Release: alt1
License: GPLv3+
Summary: Application for Nitrokey devices management
Url: https://www.nitrokey.com/
Vcs: https://github.com/Nitrokey/nitrokey-app.git
Group: System/Configuration/Other

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-xdg
BuildRequires: cmake bash-completion
BuildRequires: cppcodec-devel libnitrokey-devel
BuildRequires: qt5-base-devel qt5-tools-devel qt5-svg-devel

%description
Nitrokey App is a cross-platform application created to manage
Nitrokey devices. Underneath it uses libnitrokey communicate with
the supported devices.

%prep
%setup
%patch -p1
# Qt5 forces c++11 while libnitrokey needs at least c++14
sed 's/(COMPILE_FLAGS "-Wall/(COMPILE_FLAGS "-std=gnu++17 -Wall/' -i CMakeLists.txt

%build
%cmake -DADD_GIT_INFO=off
%cmake_build

%install
%cmake_install

%find_lang %name

%files -f %name.lang
%_bindir/nitrokey-app
%_datadir/bash-completion/completions/%name
%_datadir/applications/nitrokey-app.desktop
%_datadir/icons/hicolor/*/apps/nitrokey-app.*
%if_enabled ubuntuicons
%_datadir/icons/ubuntu-mono-*/apps/*/nitrokey-app.*
%else
%exclude %_datadir/icons/ubuntu-mono-*/apps/*/nitrokey-app.*
%endif
%_datadir/pixmaps/nitrokey-app.png
%_datadir/metainfo/*.appdata.xml
%doc OTP_full_specification.txt *.md

%changelog
* Sun Nov 10 2024 Andrew Savchenko <bircoph@altlinux.org> 1.4.2-alt1
- Major update to 1.4.2.
- Hardware management is moved to libnitrokey.
- Udev rules no longer require a separate user (neither upstream or
  downstream).
- More docs are available.

* Thu Sep 12 2024 Andrew Savchenko <bircoph@altlinux.org> 0.6.3-alt3
- Fix ftbfs after usrmerge.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 0.6.3-alt2.1
- NMU: spec: adapted to new cmake macros.

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt2
- Updated build dependencies.

* Mon Feb 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3.

* Thu Dec 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.1-alt1
- Updated to 0.6.1.

* Wed Oct 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.1-alt1
- Initial build.
