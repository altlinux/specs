Summary: data metering tool
Name: pipemeter
Version: 1.1.2
Release: alt1
License: GPL
Group: System/Base
URL: http://spamaps.org/pipemeter.php
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source0: %name-%version.tar.gz
Patch0: pipemeter.patch

%description
This program can be used in a shell pipe to display speed and progress (if
size of stream is available).

%prep
%setup -q
%patch0 -p0

%build
%configure
%make

%install
mkdir -p %buildroot%_bindir \
	%buildroot%_man1dir
%make_install PREFIX=%buildroot/usr DESTDIR="%buildroot" install


%files
%doc Changelog LICENSE README results.txt testscript.sh
%_man1dir/*
%_bindir/%name

%changelog
* Wed Jul 12 2006 Mikhail Pokidko <pma@altlinux.ru> 1.1.2-alt1
- Initial build
