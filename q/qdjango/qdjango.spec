%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_skiplist %_datadir/qt5/tests/*/tst_*

%def_with check

Name: qdjango
Version: 0.6.2
Release: alt1

Summary: QDjango, a Qt-based C++ web framework
License: LGPL-2.1
Group: System/Libraries
Url: https://github.com/jlaine/qdjango

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: doxygen

%description
QDjango is a cross-platform C++ web development framework built upon Qt.
Where possible it tries to follow django's API, hence its name.

%package -n lib%{name}
Summary: Development files for the QDjango framework
Group: System/Libraries

%description -n lib%{name}
QDjango is a cross-platform C++ web development framework built upon Qt.
Where possible it tries to follow django's API, hence its name.

This package contains the database object relational model and HTTP
library.

%package -n lib%{name}-devel
Summary: Development files for the QDjango framework
Group: Development/KDE and QT
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
QDjango is a cross-platform C++ web development framework built upon Qt.
Where possible it tries to follow django's API, hence its name.

This package contains the development headers and libraries.

%package -n lib%{name}-doc
Summary: Development files for the QDjango framework
Group: Documentation
BuildArch: noarch

%description -n lib%{name}-doc
QDjango is a cross-platform C++ web development framework built upon Qt.
Where possible it tries to follow django's API, hence its name.

This package contains the HTML documentation.

%prep
%setup
%patch -p1

%build
%qmake_qt5 \
           PREFIX=%_prefix \
           CONFIG+=nostrip \
           QMAKE_CXXFLAGS="%optflags"

%make_build
%make_build docs

%install
%makeinstall_std INSTALL_ROOT=%buildroot
%makeinstall_std INSTALL_ROOT=%buildroot docs

%ifnarch i586
mkdir -pv %{buildroot}%{_libdir}/
mv -vf %{buildroot}/usr/lib/* %{buildroot}%{_libdir}/
%endif

%check
%make -j1 check

%files -n lib%{name}
%doc AUTHORS ChangeLog LICENSE.LGPL README.md
%_libdir/libqdjango-db.so.0*
%_libdir/libqdjango-http.so.0*

%files -n lib%{name}-devel
%dir %_includedir/qdjango
%_includedir/qdjango/*
%_libdir/libqdjango-*.so
%_libdir/pkgconfig/*.pc

%if_with check
%exclude %_datadir/qt5/tests
%endif

%files -n lib%{name}-doc
%dir %_datadir/doc/qdjango
%_datadir/doc/qdjango/*

%changelog
* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
