# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt2-build-tools
Version: 2.1.0
Release: alt1

Summary: Various packaging tools and scripts for LXQt applications
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/lxqt/lxqt-build-tools
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qt6-base-devel qt6-tools-devel glib2-devel

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
%cmake
%cmake_build

%install
%cmake_install

%files
%doc BSD-3-Clause AUTHORS CHANGELOG README.md
%_datadir/cmake/lxqt2-build-tools
%_bindir/lxqt2-transupdate

%changelog
* Fri Nov 08 2024 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version
- Fix typo in License tag

* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- initial build
