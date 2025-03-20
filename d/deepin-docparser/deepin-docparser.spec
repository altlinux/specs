%define repo docparser
%define soname 1

Name: deepin-docparser
Version: 1.0.16
Release: alt1

Summary: Document parser library by deepin
Summary(ru): Библиотека синтаксического анализа документов от deepin

License: LGPL-3.0-or-later and GPL-3.0-or-later
Group: Text tools
Url: https://github.com/linuxdeepin/docparser
Vcs: https://github.com/linuxdeepin/docparser.git

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake libpoppler-cpp-devel libzip-devel libpugixml-devel libxml2-devel libuuid-devel libtinyxml2-devel libfreetype-devel

%description
The file content analysis library is provided for the full-text search function
of document management.

%description -l ru
Библиотека анализа содержимого файлов предоставляет функции полнотекстового
поиска в системе управления документами.

%package common
Summary: Common files for %name
Summary(ru): Общие файлы для %name
Group: Text tools
BuildArch: noarch
Provides: lib%repo-common

%description common
Common files for %name.

%description common -l ru
Общие файлы для %name.

%package -n lib%repo%soname
Summary: Document parser library by deepin
Summary(ru): Библиотека синтаксического анализа документов от deepin
Group: System/Libraries

%description -n lib%repo%soname
The file content analysis library is provided for the full-text search function
of document management.

%description -n lib%repo%soname -l ru
Библиотека анализа содержимого файлов предоставляет функции полнотекстового
поиска в системе управления документами.

%package -n lib%repo-devel
Summary: Development package for %name
Summary(ru): Пакет разработки для %name
Group: Development/C++

%description -n lib%repo-devel
Header files and libraries for %name.

%description -n lib%repo-devel -l ru
Заголовочные файлы и библиотеки для %name.

%prep
%setup -n %repo-%version

%build
%cmake \
    -GNinja \
    -DLIB_INSTALL_DIR=%_libdir \
#
%cmake_build

%install
%cmake_install

%files common
%doc LICENSE* README*

%files -n lib%repo%soname
%_libdir/lib%repo.so.%{soname}*

%files -n lib%repo-devel
%dir %_includedir/%repo/
%_includedir/%repo/%repo.h
%_libdir/lib%repo.so
%_pkgconfigdir/%repo.pc

%changelog
* Thu Mar 20 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.16-alt1
- New version 1.0.16.
- Added vcs tag.
- Updated license tag.
- Packaged the docs separately.

* Tue Sep 10 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- New version 1.0.11.
- Built via separate qt5 instead system (ALT #48138).

* Tue Jun 21 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1
- New version.
- Upstream:
  + fix: Full text search leads to the death/collapse of the documentary tube.

* Thu Apr 07 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.
- Built as require for deepin-file-manager.

