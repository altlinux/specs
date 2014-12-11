
Name:           pcsc-perl
Version:        1.4.13
Release:        alt1.1
Summary:        Perl interface to the PC/SC smart card library

Group:          Development/Perl
License:        GPLv2+
URL:            http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source0:        http://ludovic.rousseau.free.fr/softwares/pcsc-perl/%{name}-%{version}.tar.bz2

BuildRequires:  perl-devel
BuildRequires:  libpcsclite-devel >= 1.3.0
Provides:       perl-pcsc = %version-%release

%description
This library allows to communicate with a smart card using PC/SC
interface (pcsc-lite) from a Perl script.

%prep
%setup -q
chmod 644 examples/* # avoid dependencies

%build
%def_without test
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changelog LICENCE README examples/
%perl_vendor_archlib/Chipcard
%perl_vendor_autolib/Chipcard

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.13-alt1.1
- rebuild with new perl 5.20.1

* Wed Feb 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.13-alt1
- Initial build for ALT Linux (thans Fedora for spec)
