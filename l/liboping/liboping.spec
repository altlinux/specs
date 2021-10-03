Name: liboping
Version: 1.10.0
Release: alt2

Summary: Liboping library
License: LGPLv2.1
Group: System/Libraries

Url: https://github.com/octo/liboping
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: /usr/bin/pod2man

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
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for liboping library.


%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --with-perl-bindings=no \
	   --disable-static \
#
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%_libdir/*.so.*

%files -n oping
%_bindir/oping
%_man8dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*

# TODO:
# - package perl modules
# - scrap gear repo, redo with git://git.verplant.org/liboping.git

%changelog
* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.10.0-alt2
- cleanup spec
- disabled static library build
- added pkgconfig file to the devel package

* Tue Feb 18 2020 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.10.0
- removed suid bit for oping binary and this tool now work only under
  privileged user

* Wed Dec 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt2
- Fixed FTBFS (Disabled Werror).

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
