Name: babeltrace
Version: 1.5.3
Release: alt1
Summary: Trace conversion program
License: LGPLv2
Group: System/Libraries
Url: http://www.efficios.com/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: elfutils-devel flex glib2-devel glibc-kernheaders-generic libpopt-devel libuuid-devel

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

%package -n lib%name-ctf-devel
Summary: Common Trace Format (CTF) development files
Group: Development/C

%description -n lib%name-ctf-devel
This package provides the development headers to link applications directly
against libbabeltrace-ctf

%prep
%setup -q
%patch0 -p1

%build
%autoreconf

%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%doc LICENSE doc/lttng-live.txt
%_libdir/lib%name.so.*
%_libdir/lib%name-dummy.so.*
%_libdir/lib%name-lttng-live.so.*

%files -n lib%name-devel
%_includedir/%name/*.h
%_libdir/lib%name.so
%_libdir/lib%name-dummy.so
%_libdir/lib%name-lttng-live.so
%_pkgconfigdir/%name.pc

%files -n lib%name-ctf
%_libdir/lib%name-ctf*.so.*

%files -n lib%name-ctf-devel
%doc doc/API.txt doc/debug-info.txt doc/development.txt
%_includedir/%name/ctf*
%_libdir/lib%name-ctf*.so
%_pkgconfigdir/%name-ctf.pc

%changelog
* Thu Sep 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Jul 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.2-alt1
- initial release

