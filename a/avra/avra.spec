Name: avra
Version: 1.4.2
Release: alt1
Summary: AVRA is an assembler for Atmel AVR microcontrollers
License: GPLv2
Group: Development/C
Url: https://github.com/Ro5bert/avra
Source0: %name.tar
%description
AVRA is an assembler for Atmel AVR microcontrollers, and it is almost
compatible with Atmel's own assembler, AVRASM32. AVRA is written in C99.

%prep
%setup -n %name

%build
export CFLAGS='%optflags'
export LDFLAGS='%optflags'
%make PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%check
%make check

%files
%_bindir/*
%_includedir/*

%changelog
* Thu Sep 23 2021 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2
- enabled tests
- fixed Licence according SPDX
- updated homepage URL and description

* Wed Jan 12 2011 Sergey Alembekov <rt@altlinux.ru> 1.3.0-alt1
- Initial build
