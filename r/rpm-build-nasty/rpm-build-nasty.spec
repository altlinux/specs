Name: rpm-build-nasty
Version: 1.0
Release: alt1
Summary: Adjust the RPM build process nice level to zero
License: GPL
Group: Development/Other
Url: http://git.altlinux.org/gears/r/%name

BuildArch: noarch

%description
You can use the supplied RPM configuration file to run the building
process at ordinary (zero) nice level.

%install
mkdir -p -m0755 %buildroot%_sysconfdir/rpm/macros.d
echo "%%nice_change 0" >%buildroot%_sysconfdir/rpm/macros.d/build-it-nasty

%files
%_sysconfdir/rpm/macros.d/build-it-nasty

%changelog
* Tue Oct 16 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release for ALT Linux.
