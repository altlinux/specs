%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

%define _libexecdir %_prefix/libexec

Name: libusermetrics
Version: 1.4.2
Release: alt1

Summary: library for retrieving anonymous metrics about users
License: GPL-3.0 and LGPL-3.0 and LGPL-2.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/libusermetrics

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(qdjango-db)
BuildRequires: ayatana-cmake-modules
BuildRequires: doxygen
BuildRequires: intltool
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(gtest)

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: python3(dbusmock)
%endif

%description
Libusermetrics enables apps to locally store interesting numerical data
for later presentation.  For example in the Ubuntu Greeter "flower"
infographic.

- All data is stored locally in /var/usermetrics/.
- No data is centrally collected via a web-serivice or otherwise, and
no data is sent over the internet.

The only data that can be stored is numerical, for example "number of
e-mails" or "number of pictures taken". No personally identifying
information is stored using this library.

The Libusermetrics components are used by the Lomiri Operating
Environment.

%package -n %{name}input
Summary: input library for exporting anonymous metrics about users
Group: System/Libraries

%description -n %{name}input
Libusermetrics enables apps to locally store interesting numerical data
for later presentation.  For example in the Ubuntu Greeter "flower"
infographic.

- All data is stored locally in /var/usermetrics/.
- No data is centrally collected via a web-serivice or otherwise, and
no data is sent over the internet.

The only data that can be stored is numerical, for example "number of
e-mails" or "number of pictures taken". No personally identifying
information is stored using this library.

The Libusermetrics components are used by the Lomiri Operating
Environment.

This package contain the libusermetricsinput shared library to be
used by applications.

%package -n %{name}output
Summary: output library for retrieving anonymous metrics about users
Group: System/Libraries

%description -n %{name}output
Libusermetrics enables apps to locally store interesting numerical data
for later presentation.  For example in the Ubuntu Greeter "flower"
infographic.

- All data is stored locally in /var/usermetrics/.
- No data is centrally collected via a web-serivice or otherwise, and
no data is sent over the internet.

The only data that can be stored is numerical, for example "number of
e-mails" or "number of pictures taken". No personally identifying
information is stored using this library.

The Libusermetrics components are used by the Lomiri Operating
Environment.

This package contain the libusermetricsoutput shared library to be
used by applications.

%package -n %{name}-devel
Summary: libraries for exporting anonymous metrics about users (header files)
Group: Development/Other
Requires: %{name}input = %{version}-%{release}
Requires: %{name}output = %{version}-%{release}

%description -n %{name}-devel
Libusermetrics enables apps to locally store interesting numerical data
for later presentation.  For example in the Ubuntu Greeter "flower"
infographic.
.
- All data is stored locally in /var/usermetrics/.
- No data is centrally collected via a web-serivice or otherwise, and
no data is sent over the internet.
.
The only data that can be stored is numerical, for example "number of
e-mails" or "number of pictures taken". No personally identifying
information is stored using this library.
.
The Libusermetrics components are used by the Lomiri Operating
Environment.

This package contains libusermetricsinput and libusermetricsoutput header
files that are needed to build applications.

%package doc
Summary: API documentation for libusermetrics
Group: Documentation
BuildArch: noarch

%description doc
Libusermetrics enables apps to locally store interesting numerical data
for later presentation.  For example in the Ubuntu Greeter "flower"
infographic.

- All data is stored locally in /var/usermetrics/.
- No data is centrally collected via a web-serivice or otherwise, and
no data is sent over the internet.

The only data that can be stored is numerical, for example "number of
e-mails" or "number of pictures taken". No personally identifying
information is stored using this library.

The Libusermetrics components are used by the Lomiri Operating
Environment.

This package installs the libusermetrics API documentation.

%prep
%setup

%build
%cmake \
       -W no-dev \
%if_with check
       -DENABLE_TESTS=ON
%else
       -DENABLE_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL LICENSE.LGPL-3 README.md
%_bindir/usermetricsinput
%_bindir/usermetricsinput-increment
%_datadir/dbus-1/system-services/com.lomiri.UserMetrics.service
%_datadir/glib-2.0/schemas/com.lomiri.UserMetrics.gschema.xml
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/libusermetrics.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/libusermetrics.mo
%dir %_datadir/%name
%_datadir/%name/*
%dir %_qt5_qmldir/UserMetrics
%_qt5_qmldir/UserMetrics/*
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_datadir/dbus-1/system.d/com.lomiri.UserMetrics.conf

%files -n %{name}input
%_libdir/%{name}input.so.1*

%files -n %{name}output
%_libdir/%{name}output.so.1*

%files -n %{name}-devel
%dir %_includedir/%{name}-1
%_includedir/%{name}-1/*
%_libdir/%{name}input.so
%_libdir/%{name}output.so
%_libdir/pkgconfig/%{name}input-1.pc
%_libdir/pkgconfig/%{name}output-1.pc
%_datadir/dbus-1/interfaces/*.xml

%files doc
%dir %_docdir/%{name}-doc
%_docdir/%{name}-doc/*


%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.2-alt1
- New version 1.4.2.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.1-alt1
- New version 1.4.1.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus
