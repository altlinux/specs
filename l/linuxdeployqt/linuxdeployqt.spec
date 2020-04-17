%define commit d091be1aef7bee247a763537cd23b9a3a24b373c
%define commit_short %(echo %commit | head -c 5)

Name: linuxdeployqt
Summary: Tool to make a bundle from application for AppImage
Group: Development/C
Version: 6
Release: alt0.%{commit_short}.2
License: GPLv3 or LGPLv3
Source0: %name-%version.tar
Patch0:	no-fail-with-system-glibc.patch
BuildRequires: qt5-base-devel
BuildRequires: rpm-macros-qt5
Requires: patchelf

%description
This Linux Deployment Tool, linuxdeployqt, takes an application
as input and makes it self-contained by copying in the resources
that the application uses (like libraries, graphics, and plugins)
into a bundle. The resulting bundle can be distributed as an AppDir or
as an AppImage to users, or can be put into cross-distribution packages

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt5
%make

%install
mkdir -p %buildroot/%_bindir
install -m 0755 bin/linuxdeployqt %buildroot/%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Apr 17 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 6-alt0.d091b.2
- Initial build
- Patch: do not exit with error if system glibc is too new
  for production AppImages from the point of view of upstream authors

