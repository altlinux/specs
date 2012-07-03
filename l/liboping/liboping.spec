%def_disable static

Name: liboping
Version: 1.6.2
Release: alt1

Summary: Liboping library
License: GPL v2
Group: System/Libraries

Url: http://verplant.org/liboping/
Source0: %url/files/%name-%version.tar.bz2
Source1: oping.control
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed May 13 2009
BuildRequires: perl-devel chrpath

%description
liboping is a C library to generate ICMP echo requests, better known
as "ping packets". It is intended for use in network monitoring
applications or applications that would otherwise need to fork
ping(1) frequently.

liboping was inspired by ping, libping (homepage vanished) and fping:
it differs from these existing solutions in that it can `ping' multiple
hosts in parallel using IPv4 or IPv6 transparently. Other design
principles were an object oriented interface, simplicity and
extensibility: Is simple because there are only a few interface
functions and no external dependencies. It's extensible since all
(internal) data is kept in "opaque data types", so the storage may
change or be extended without applications noticing it.

%package -n oping
Summary: oping ICMP query tool
Group: Networking/Other

%description -n oping
Sample application, which demonstrates the liboping's abilities.
It is like ping, ping6, and fping rolled into one.

%package devel
Summary: Header files for liboping library
Summary(pl.UTF-8): Pliki nagłówkowe biblioteki liboping
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for liboping library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboping.

%if_enabled static
%package devel-static
Summary: Static liboping library
Summary(pl.UTF-8): Statyczna biblioteka liboping
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static liboping library.

%description devel-static -l pl.UTF-8
Statyczna biblioteka liboping.
%endif

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pDm755 %SOURCE1 %buildroot%_controldir/oping
for i in $(find %buildroot%prefix -name '*.so'); do
	chrpath -d $i
done

%pre -n oping
%_sbindir/groupadd -r -f netadmin >/dev/null 2>&1
%pre_control oping

%post -n oping
%post_control -s netadmin oping

%files
%doc AUTHORS ChangeLog README
%_libdir/*.so.*

%files -n oping
%_bindir/oping
%config %_controldir/oping
%_man8dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

# TODO:
# - package perl modules
# - scrap gear repo, redo with git://git.verplant.org/liboping.git

%changelog
* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1.6.2-alt1
- 1.6.2

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- drop RPATH

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.1
- Rebuilt for soname set-versions

* Thu May 14 2009 Michael Shigorin <mike@altlinux.org> 1.1.2-alt2
- fixed control scriptlet packaging

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1.1.2-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- introduced control(8) support
- introduced static subpackage (off by default)
- buildreq
