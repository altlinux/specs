Name: libsigrokdecode
Version: 0.5.0
Release: alt1.1

Summary: sigrok -- signal analysis software suite
License: GPLv3
Group: System/Libraries
Url: https://sigrok.org/

Source: %name-%version-%release.tar

BuildRequires: glib2-devel libcheck-devel python3-dev

%package devel
Summary: sigrok -- signal analysis software suite
Group: Development/C

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

libsigrokdecode is a shared library written in C which provides the basic
API for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

%description devel
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source signal analysis software suite that supports various
device types (such as logic analyzers, oscilloscopes, multimeters, and more).

libsigrokdecode is a shared library written in C which provides the basic
API for running sigrok protocol decoders. The protocol decoders themselves
are written in Python.

this package provides development part of libsigrokdecode.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
make check

%add_findreq_skiplist %_datadir/libsigrokdecode/decoders/*

%files
%_libdir/libsigrokdecode.so.*
%_datadir/libsigrokdecode/decoders

%files devel
%_libdir/libsigrokdecode.so
%_includedir/libsigrokdecode
%_pkgconfigdir/libsigrokdecode.pc

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
