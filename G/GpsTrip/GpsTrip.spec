Name: GpsTrip
Version: 1.1.3
Release: alt1

Summary: GpsTrip - trip computer for car sprotmans, who use legend for racing.
Summary(ru_RU.UTF-8): GpsTrip - штурманский компьютер для автогонщиков, использующих легенду.

License: GPL

Group: Sciences/Geosciences
Url: http://sourceforge.net/projects/gpstrip/

BuildArch: noarch

Source0: %name-%version.tar.bz2

%description
GpsTrip - trip computer for car sprotmans,
who use legend for racing.

%description -l ru_RU.UTF-8
GpsTrip - штурманский компьютер для автогонщиков, использующих легенду.

%prep
%setup -q -n %name-%version

%build

%install
#__install -d -m0775 %buildroot%_bindir
%__install -D -m0755 %name.tcl %buildroot%_bindir/%name

%files
%_bindir/*
%doc Readme ChangeLog ToDo

%changelog
* Tue Sep 09 2008 Grigory Milev <week@altlinux.ru> 1.1.3-alt1
- Initial build for ALT Linux
