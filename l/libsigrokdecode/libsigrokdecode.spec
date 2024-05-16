Name: libsigrokdecode
Version: 0.6.0
Release: alt0.202403040

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
%_libdir/libirmp.so
%_libdir/libsigrokdecode.so.*
%_datadir/libsigrokdecode/decoders

%files devel
%_libdir/libsigrokdecode.so
%_includedir/libsigrokdecode
%_pkgconfigdir/libsigrokdecode.pc

%changelog
* Thu May 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.0-alt0.202403040
- git snapshot libsigrokdecode-unreleased-738-g0235970

* Thu Apr 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.202212300
- git snapshot libsigrokdecode-unreleased-709-g73cb546

* Mon Jun 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.202204220
- git snapshot libsigrokdecode-unreleased-691-ge556e11

* Thu Jan 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt0.202010729.1
- Add patch for building with python3.10.

* Tue Aug 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.202010729
- git snapshot libsigrokdecode-unreleased-670-g02aa01a

* Wed Jan 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt2
- Add patch for building with python3.9.

* Thu Feb 06 2020 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt1
- 0.5.3 released
- Build for python3.8.

* Tue Oct 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt1
- 0.5.2 released

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jun 19 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- initial
