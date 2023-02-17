Name: libwiringpi-devel-static
Version: 2.61
Release: alt1

Summary: GPIO library for Raspberry Pee
License: LGPLv3
Group: Development/C
Url: https://github.com/WiringPi/WiringPi

Source: %name-%version-%release.tar

%description
%summary

%prep
%setup

%build
make -C wiringPi static

%install
make -C wiringPi install DESTDIR=%buildroot PREFIX=%_prefix
install -pm0644 -D wiringPi/libwiringPi.a %buildroot%_libdir/libwiringPi.a

%files
%_includedir/*
%_libdir/libwiringPi.a


%changelog
* Fri Feb 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.61-alt1
- initial

