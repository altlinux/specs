%define soversion 1

Name:    QXlsx
Version: 1.5.0
Release: alt2

Summary: Excel file(*.xlsx) reader/writer library
License: MIT
Group:   Development/KDE and QT
Url:     https://qtexcel.github.io/QXlsx
Vcs:     https://github.com/QtExcel/QXlsx

Source: %name-%version.tar

# Search for GuiPrivate package with Qt 6.10
Patch: 90d762625750c6b2c73f6cd96b633e9158aed72e.patch

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
%patch -p1

%build
pushd QXlsx
%cmake -DBUILD_SHARED_LIBS=ON \
       -DQT_NO_PRIVATE_MODULE_WARNING=ON
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
* Thu Feb 19 2026 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt2
- Fixed FTBFS.

* Tue Jan 14 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.5.0-alt1
- 1.4.9 -> 1.5.0.

* Tue Nov 05 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.4.9-alt1
- Initial build for Sisyphus.
