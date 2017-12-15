
Name:           perl-pcsc
Version:        1.4.14
Release:        alt2.1.1
Summary:        Perl interface to the PC/SC smart card library

Group:          Development/Perl
License:        GPLv2+
URL:            http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source0:        http://ludovic.rousseau.free.fr/softwares/pcsc-perl/pcsc-perl-%{version}.tar.bz2
Source1:        %name.watch

BuildRequires:  perl-devel
BuildRequires:  libpcsclite-devel >= 1.3.0
Provides:       pcsc-perl = %version-%release
Obsoletes:      pcsc-perl <= 1.4.14-alt1

%description
This library allows to communicate with a smart card using PC/SC
interface (pcsc-lite) from a Perl script.

%prep
%setup -n pcsc-perl-%version
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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.14-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.14-alt2.1
- rebuild with new perl 5.24.1

* Thu Dec 08 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.14-alt2
- rename package to perl-pcsc (ALT bug #32852)

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.14-alt1
- New version
- Add watch file

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.4.13-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.13-alt1.1
- rebuild with new perl 5.20.1

* Wed Feb 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.13-alt1
- Initial build for ALT Linux (thanks Fedora for spec)
