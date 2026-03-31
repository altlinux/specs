%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

# TODO do something related to C++17 support in gtest and this code
%def_without check

Name: lomiri-polkit-agent
Version: 0.3.3
Release: alt1

Summary: Service to prompt for policy kit permissions in Lomiri
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-polkit-agent

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(gtest)

%filter_from_requires /^.usr.bin.sleep/d

%description
Connects to the Policy Kit daemon for the session and responds
to requests for authentication. It then creates a Lomiri
snap decision to request the password from the user, returning
it back to PolicyKit.

%prep
%setup
%patch -p1

%build
%cmake \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%post
%systemd_user_post lomiri-polkit-agent.service

%preun
%systemd_user_preun lomiri-polkit-agent.service

%postun
%systemd_user_postun lomiri-polkit-agent.service

%files
%doc AUTHORS ChangeLog COPYING
%_userunitdir/lomiri-polkit-agent.service
%dir %_libexecdir/lomiri-polkit-agent
%_libexecdir/lomiri-polkit-agent/policykit-agent

%changelog
* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.3-alt1
- Initial build for Sisyphus
