%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: click
Version: 0.5.2
Release: alt1

Summary: tool for handling (and building) Click packages
License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/ubports/development/core/click

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-build-python3

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: dbus-test-runner
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: pkgconfig(systemd)
BuildRequires: /usr/bin/g-ir-scanner
BuildRequires: /usr/bin/pod2man
BuildRequires: libgee0.8-gir-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: /usr/bin/sphinx-build

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(unittest)
BuildRequires: /proc
BuildRequires: python3(dbusmock)
BuildRequires: systemd
BuildRequires: python3(debian)
BuildRequires: dpkg
%endif

%filter_from_requires /python3(apt)/d

%description
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package provides common files, including the main click program.

%package -n click-devel
Summary: build Click packages
Group: Development/Other
Requires: click = %{version}-%{release}

%description -n click-devel
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

click-devel provides support for building these packages.

%package -n click-doc
Summary: Click packages (documentation)
Group: Development/Other
BuildArch: noarch

%description -n click-doc
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package provides documentation for click.

%package -n click-service
Summary: Click packages (privileged service)
Group: Development/Other
Requires: click = %{version}-%{release}

%description -n click-service
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package contains click-service, a simple daemon which allows
unprivileged users to install click packages over D-Bus.

%package -n click-gir
Summary: GIR bindings for Click package management library
Group: System/Libraries
Requires: click = %{version}-%{release}
Requires: libclick = %{version}-%{release}
Requires: libgee0.8-gir
Requires: glib2
Requires: libjson-glib-gir

%description -n click-gir
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package can be used by other packages using the GIRepository format
to generate dynamic bindings.

%package -n libclick
Summary: run-time Click package management library
Group: System/Libraries

%description -n libclick
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package provides a shared library for managing Click packages.

%package -n libclick-devel
Summary: development files for Click package management library
Group: Development/Other
Requires: libclick = %{version}-%{release}

%description -n libclick-devel
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package provides development files needed to build programs for
managing Click packages.

%package -n python3-module-click_package
Summary: Click packages (Python 3 interface)
Group: Development/Python
Requires: libclick = %{version}-%{release}
Requires: click-gir = %{version}-%{release}
Requires: python3-module-debian
BuildArch: noarch

%description -n python3-module-click_package
Click is a simplified packaging format that installs in a separate part
of the file system, suitable for third-party applications.

This package provides Python 3 modules used by click, which may also be
used directly.

%prep
%setup -n %name-%version
%patch -p1
%autoreconf
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
           --with-python-interpreters='/usr/bin/python3' \
           --with-default-root=/var/lib/clickpkg
%make

%install
%makeinstall_std \
                 -- PYTHON_INSTALL_FLAGS="--root=%buildroot"

make -C doc subst DEFAULT_ROOT=/var/lib/clickpkg
make -C doc html man

mv -v doc/_build/man/click.1 %buildroot%_man1dir/click.1
mkdir -pv %buildroot%_datadir/doc/click/
mv -v doc/_build/html %buildroot%_datadir/doc/click/

find %buildroot -name "*.la" -print -delete
find %buildroot -name "*.pyc" -print -delete
find %buildroot -name "__pycache__" -print -delete

# remove deb-specific tests
rm -vf click_package/tests/integration/test_signatures.py
rm -vf click_package/tests/test_build.py
rm -vf click_package/tests/test_install.py

%check
%make check

%files
%doc AUTHORS ChangeLog LICENSE README VERSION
%dir %_sysconfdir/%name
%_sysconfdir/%name/*
%_bindir/%name
%_man1dir/click.1*
%_unitdir/*.service
%_userunitdir/*.service
%dir %_libdir/click/
%_libdir/click/libclickpreload.so

%files -n click-devel
%dir %_sysconfdir/schroot/click
%_sysconfdir/schroot/click/fstab
%exclude %_bindir/dh_click
%exclude %_datadir/debhelper
%exclude %_man1dir/dh_click.1*
%exclude %_datadir/perl5/Debian/Debhelper/Sequence/click.pm

%files -n click-doc
%dir %_datadir/doc/click/
%_datadir/doc/click/*

%files -n click-service
%_sysconfdir/dbus-1/system.d/com.lomiri.click.conf
%dir %_libexecdir/%name
%_libexecdir/%name/*
%_datadir/dbus-1/system-services/com.lomiri.click.service

%files -n click-gir
%_typelibdir/Click-0.4.typelib

%files -n libclick
%_libdir/libclick-0.4.so.0*

%files -n libclick-devel
%dir %_includedir/click-0.4
%_includedir/click-0.4/*
%_libdir/pkgconfig/click-0.4.pc
%_libdir/libclick-0.4.so
%_girdir/Click-0.4.gir

%files -n python3-module-click_package
%python3_sitelibdir_noarch/*egg-info
%dir %python3_sitelibdir_noarch/click_package/
%python3_sitelibdir_noarch/click_package/*

%changelog
* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus
