%define _name bytesize

Name: lib%_name
Version: 0.8
Release: alt1

Summary: A library for working with sizes in bytes
Group: System/Libraries
License: LGPLv2+
Url: https://github.com/rhinstaller/%name

Source: %url/archive/%name-%version.tar.gz

BuildRequires(pre): rpm-build-python rpm-build-python3

BuildRequires: gtk-doc
BuildRequires: glib2-devel libgmp-devel libmpfr-devel libpcre-devel
BuildRequires: python-devel python3-devel

%description
The %name is a C library that facilitates work with sizes in bytes.
Be it parsing the input from users or producing a nice human readable
representation of a size in bytes this library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files and pkg-config files needed for
development with the %name library.

%package -n python-module-%_name
Summary: Python 2 bindings for %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%_name
This package contains Python 2 bindings for %name making the use of
the library from Python 2 easier and more convenient.

%package -n python3-module-%_name
Summary: Python 3 bindings for %name
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-%_name
This package contains Python 3 bindings for %name making the use of
the library from Python 3 easier and more convenient.

%prep
%setup -n %name-%name-%version

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags libpcre`"
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_libdir/%name.so.*
%doc README.rst LICENSE

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_datadir/gtk-doc/html/%name/

%files -n python-module-%_name
%python_sitelibdir/%_name/*

%files -n python3-module-%_name
%python3_sitelibdir/%_name/*


%changelog
* Thu Dec 22 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Mon Oct 03 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- first build for Sisyphus

