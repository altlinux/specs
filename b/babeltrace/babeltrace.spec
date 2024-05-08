%define _unpackaged_files_terminate_build 1

Name: babeltrace
Version: 1.5.11
Release: alt1
Summary: Trace conversion program
License: LGPLv2
Group: System/Libraries
Url: http://www.efficios.com/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: elfutils-devel flex glib2-devel glibc-kernheaders-generic libpopt-devel libuuid-devel
BuildRequires: python3-dev python3-module-setuptools swig >= 2.0

%description
Babeltrace provides trace reading and writing libraries, as well as a trace
converter. Plugins can be created for any trace format to allow its conversion
to/from any other supported format

%package -n lib%name
Summary: Babeltrace conversion libraries
Group: System/Libraries

%description -n lib%name
This package provides the babeltrace trace reading and conversion library

%package -n lib%name-devel
Summary: Babeltrace development files
Group: Development/C
Provides: lib%name-ctf-devel = %EVR
Obsoletes: lib%name-ctf-devel < %EVR

%description -n lib%name-devel
This package provides the development headers for linking applications against
libbabeltrace

%package -n lib%name-ctf
Summary: Common Trace Format (CTF) library
Group: System/Libraries

%description -n lib%name-ctf
The Common Trace Format (CTF) aims at specifying a trace format based on the
requirements of the industry (through collaboration with the Multicore
Association) and the Linux community

%package -n python3-module-%name
Summary: Common Trace Format Babel Tower
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-%name
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf

export PYTHON=%__python3
export PYTHON_CONFIG=%__python3-config

%configure \
	--disable-static \
	--enable-python-bindings
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_datadir/doc

%check
%make check

%files
%doc doc/lttng-live.txt
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/lib%name.so.*
%_libdir/lib%name-dummy.so.*
%_libdir/lib%name-lttng-live.so.*

%files -n lib%name-devel
%doc doc/API.txt doc/debug-info.txt doc/development.txt
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-ctf
%_libdir/lib%name-ctf*.so.*

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Wed May 08 2024 Alexey Shabalin <shaba@altlinux.org> 1.5.11-alt1
- 1.5.11

* Thu Jun 30 2022 Alexey Shabalin <shaba@altlinux.org> 1.5.8-alt2
- fix obsoletes in devel subpackage

* Tue Mar 22 2022 Alexey Shabalin <shaba@altlinux.org> 1.5.8-alt1
- 1.5.8
- build python bindings
- package babeltrace and babeltrace-log to main package
- add %%check section
- merge libbabeltrace-ctf-devel to libbabeltrace-devel

* Thu Sep 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Jul 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.2-alt1
- initial release

