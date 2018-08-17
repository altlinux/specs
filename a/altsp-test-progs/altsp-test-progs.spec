Name:     altsp-test-progs
Version:  1.0
Release:  alt1

Summary:  Programs for tests for ALT SP OS
License:  GPLv2+
Group:    Other
Url:      http://git.altlinux.org/gears/a/altsp-test-progs.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ make

%description
A set of progs for testing ALT SP OS
and tuning its features

%prep
%setup

%build
cd testIsol
make

%install
mkdir -p %buildroot%_libdir/%name-%version
cp -ar testIsol %buildroot%_libdir/%name-%version
cp -ar *.tgz %buildroot%_libdir/%name-%version

%files
%_libdir/%name-%version/*
%doc AUTHORS NEWS README

%changelog
* Fri Aug 17 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt1
- build for Sisyphus

* Wed May 30 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt0.M80C.5
- testIsol now allows compile with lower version of C compilator.

* Wed Apr 18 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt0.M80C.4
- wrong script extension

* Wed Apr 18 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt0.M80C.3
- fixed adding scripts

* Wed Apr 18 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt0.M80C.2
- additional scripts added

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt0.M80C.1
- c8 version

* Wed Jan 17 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt1
Initial release
