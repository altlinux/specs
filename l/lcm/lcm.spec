%set_verify_elf_method rpath=relaxed

Name: lcm
Version: 0.9.2
Release: alt2

Summary: Lightweight Communications and Marshalling (LCM)
License: GPLv2
Group: Networking/Other

Url: http://code.google.com/p/lcm/

BuildRequires: glib2-devel
BuildRequires: /proc rpm-build-java java-devel-default
BuildRequires: python-devel

Requires: lib%name = %version-%release

Source0: %name-%version.tar

%description
LCM is a set of libraries and tools for message passing and data marshalling,
targeted at real-time systems where high-bandwidth and low latency are
critical. It provides a publish/subscribe message passing model and automatic
marshalling/unmarshalling code generation with bindings for applications in a
variety of programming languages. It was originally designed and used by the
MIT DARPA Urban Challenge Team as its message passing system.

LCM is designed for tightly-coupled systems connected via a dedicated
local-area network. It is not intended for message passing over the Internet.
LCM has been developed for soft real-time systems: its default messaging model
permits dropping messages in order to minimize the latency of new messages.


%package -n lib%name
Summary: LCM libraries
Group: System/Libraries

%description -n lib%name
LCM libraries.


%package -n lib%name-devel
Summary: LCM development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
LCM development files.


%package -n lib%name-java
Summary: Java bindings for LCM
Group: Development/Java
Requires: lib%name = %version-%release
BuildArch: noarch

%description -n lib%name-java
Java bindings for LCM.


%package -n python-module-%name
Summary: Python bindings for LCM
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
Python bindings for LCM.


%package gui
Summary: Graphical tools for LCM
Group: Networking/Other
Requires: lib%name-java = %version-%release
BuildArch: noarch

%description gui
Graphical tools for LCM.
Lightweight Communications and Marshalling traffic
inspection utility and log playback tool.


%prep
%setup

%build
autoreconf --install
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/lcm-gen
%_bindir/lcm-logger
%_bindir/lcm-logplayer
%_mandir/man1/lcm-gen.1.gz
%_mandir/man1/lcm-logger.1.gz
%_mandir/man1/lcm-logplayer.1.gz

%files -n lib%name
%_libdir/liblcm.so.*

%files -n lib%name-devel
%_libdir/liblcm.so
%_libdir/pkgconfig/*.pc
%_includedir/lcm/
%_datadir/aclocal/lcm.m4

%files -n lib%name-java
%_javadir/*.jar

%files -n python-module-%name
%python_sitelibdir/lcm

%files gui
%_bindir/lcm-logplayer-gui
%_bindir/lcm-spy
%_mandir/man1/lcm-logplayer-gui.1.gz
%_mandir/man1/lcm-spy.1.gz

%changelog
* Tue Feb 05 2013 Timur Aitov <timonbl4@altlinux.org> 0.9.2-alt2
- liblcm-java and lcm-gui noarch now

* Tue Feb 05 2013 Timur Aitov <timonbl4@altlinux.org> 0.9.2-alt1
- [0.9.2]

