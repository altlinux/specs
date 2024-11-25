Name: libcyaml
Version: 1.4.2
Release: alt1

Summary: YAML C library
License: ISC
Group: System/Libraries
Url: https://github.com/tlsa/libcyaml

Source: %name-%version.tar

BuildRequires: libyaml-devel

%package devel
Summary: YAML C library
Group: Development/C

%description
LibCYAML is a C library for reading and writing structured YAML documents.
It is written in ISO C11 and licensed under the ISC licence.

%description devel
LibCYAML is a C library for reading and writing structured YAML documents.
It is written in ISO C11 and licensed under the ISC licence.
This package contains development part of LibCYAML.

%prep
%setup

%build
CC='gcc %optflags' \
make VARIANT=release

%install
make install VARIANT=release DESTDIR=%buildroot PREFIX=%_prefix LIBDIR=%_lib
rm -v %buildroot%_libdir/*.a

%files
%doc CHANGES* LICENSE README*
%_libdir/libcyaml.so.*

%files devel
%_includedir/cyaml
%_libdir/libcyaml.so
%_pkgconfigdir/libcyaml.pc

%check
make test VARIANT=release

%changelog
* Mon Nov 25 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- initial
