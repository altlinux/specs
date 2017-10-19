Name: GpsTrip
Version: 1.1.6
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
* Thu Oct 19 2017 Grigory Milev <week@altlinux.ru> 1.1.6-alt1
- Port detection for Windows fixed.
- Change default serial speed to 4800

* Wed Oct 19 2016 Grigory Milev <week@altlinux.ru> 1.1.5-alt1
- Fix portports numbers for Win version

* Mon Nov 17 2008 Grigory Milev <week@altlinux.ru> 1.1.4-alt1
- Fixed GPS port select for Windos XP/NT/95/98
- Fixed multiply event call
- fix description
- Fix bug #37401

* Tue Sep 09 2008 Grigory Milev <week@altlinux.ru> 1.1.3-alt1
- Initial build for ALT Linux
