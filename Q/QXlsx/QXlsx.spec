%define soversion 1

Name:    QXlsx
Version: 1.5.0
Release: alt1

Summary: Excel file(*.xlsx) reader/writer library
License: MIT
Group:   Development/KDE and QT
Url:     https://qtexcel.github.io/QXlsx
Vcs:     https://github.com/QtExcel/QXlsx

Source: %name-%version.tar

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
%_libdir/lib%{name}Qt6.so.%soversion
%_libdir/lib%{name}Qt6.so.%soversion.*

%files -n lib%name-devel
%doc *.md
%_libdir/lib%{name}Qt6.so
%_includedir/%{name}Qt6
%_cmakedir/%{name}Qt6

%changelog
* Tue Jan 14 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.5.0-alt1
- 1.4.9 -> 1.5.0.

* Tue Nov 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.4.9-alt1
- Initial build for Sisyphus.
