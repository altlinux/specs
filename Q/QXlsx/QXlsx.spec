%define soversion 0
%define abiversion 1.4.4
# It seems, upstream still choose correct versioning of ABI
# so we fill soversion as package name suffix.

Name:    QXlsx
Version: 1.4.9
Release: alt1

Summary: Excel file(*.xlsx) reader/writer library
License: MIT
Group:   Development/KDE and QT
Url:     https://qtexcel.github.io/QXlsx
Vcs:     https://github.com/QtExcel/QXlsx

Source: %name-%version.tar
Patch0: QXlsx-1.4.9-alt-private-str.patch
# Fix string comparison with Latin1 encoded slash (thx Fedora).

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel

%description
%summary using Qt 5 or 6. Descendant of QtXlsxWriter.

%package -n lib%name%soversion
Summary: %summary
Group: Development/KDE and QT

%description -n lib%name%soversion
%summary using Qt 5 or 6. Descendant of QtXlsxWriter.

%package -n lib%name-devel
Summary: %summary
Group: Development/KDE and QT
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
%summary development files.

%prep
%setup
%patch0

%build
pushd QXlsx
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build
popd

%install
pushd QXlsx
%cmake_install
popd

%files -n lib%name%soversion
%_libdir/lib%{name}Qt6.so.%abiversion
%_libdir/lib%{name}Qt6.so.%soversion.%abiversion

%files -n lib%name-devel
%doc *.md
%_libdir/lib%{name}Qt6.so
%_includedir/%{name}Qt6
%_cmakedir/%{name}Qt6

%changelog
* Tue Nov 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.4.9-alt1
- Initial build for Sisyphus.
