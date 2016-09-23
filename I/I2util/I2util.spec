Name:           I2util
Version:        1.6
Release:        alt1
Summary:        I2 Utility Library & Tools
License:        free/libre, see copyright file
Group:          Networking/Other
URL:            http://software.internet2.edu
# git:          https://github.com/perfsonar/i2util
Source0:        I2util-%{version}.tar.gz
Source1:        watch
Source2:        copyright
Patch1:         002-manpages-debian-specific.patch

%package tools
Summary:        I2 Utility Tools
Group:          Networking/Other

%package -n lib%name-devel
Summary:        I2 Utility Library
Group:          Development/C

%global common_desc I2utils is a small support library with a set of command line tools\
needed by several software projects from Internet2, most notably bwctl.\
\
I2 Utility library currently contains:\
	* error logging\
	* command-line parsing\
	* threading\
	* random number support\
	* hash table support\
\
The error logging and command-line parsing are taken from a utility library\
that is distributed with the "volsh" code from UCAR.\
\
        http://www.scd.ucar.edu/vets/vg/Software/volsh

%description
%common_desc

%description tools
%common_desc

This package contains the command line tools.

%description -n lib%name-devel
%common_desc

This is the development package which contains headers files and the
static %name library.

%prep
%setup -q
%patch1 -p1
cp %SOURCE2 -t ./

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files tools
# LICENSE has disappeared:
#%doc Changes LICENSE README
# instead, we put the Debian copyright file:
%doc copyright
# The other files are mostly like in Debian:
%doc README
%{_bindir}/*
%{_mandir}/man1/*

%files -n lib%name-devel
%doc copyright
# The other files are mostly like in Debian:
%doc README
%{_libdir}/lib%name.a
%{_includedir}/*

%changelog
* Fri Sep 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1
- initial build for ALT Sisyphus (based on the Debian package)

* Fri Aug 20 2010 Tom Throckmorton <throck@mcnc.org> 1.1-1
- minor spec changes only

* Fri Jan 11 2008 aaron@internet2.edu 1.0-1
- Initial RPM
