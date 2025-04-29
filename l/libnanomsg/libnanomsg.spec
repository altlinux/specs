Name:           libnanomsg
Version:        1.2.1
Release: alt2

Summary:        nanomsg is a socket library that provides several common communication patterns
Group:          System/Libraries
License:        MIT/X11
URL:            http://nanomsg.org/
# VCS:		https://github.com/nanomsg/nanomsg

Source0:        %name-%version.tar
# https://github.com/nanomsg/nanomsg/issues/1111#issuecomment-2113151297
Patch: libnanomsg-1.2.1-upstream-fix-chunkref.patch

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: /proc

%description
nanomsg is a socket library that provides several common communication
patterns. It aims to make the networking layer fast, scalable, and easy
to use. Implemented in C, it works on a wide range of operating systems
with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you can
create a vast array of distributed applications. The following
scalability protocols are currently available:

PAIR - simple one-to-one communication
BUS - simple many-to-many communication
REQREP - allows to build clusters of stateless services to process user
requests
PUBSUB - distributes messages to large sets of interested subscribers
PIPELINE - aggregates messages from multiple sources and load balances
them among many destinations
SURVEY - allows to query state of multiple applications in a single go

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %name = %version-%release

%description    devel
Development files for the %{name} library. nanomsg is a socket library
that provides several common communication patterns.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%doc AUTHORS README.md COPYING
%doc doc/
%_bindir/*
%_libdir/lib*.so.*

%files devel
%dir %_includedir/nanomsg
%_includedir/nanomsg/*
%_libdir/lib*.so
%_pkgconfigdir/nanomsg.pc

%changelog
* Tue Apr 29 2025 Constantin Sunzow <protvin@altlinux.org> 1.2.1-alt2
- NMU: apply patch for fix bug.
- Enable tests.

* Wed Feb 07 2024 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Tue Apr 19 2022 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version.

* Mon Oct 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Tue Dec 01 2015 Andrey Cherepanov <cas@altlinux.org> 0.8-alt1.beta
- Initial build in Sisyphus

