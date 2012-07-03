%define m_distro X10
Name: perl-%m_distro
Version: 0.03
Release: alt1.1
Summary: X10 - Perl extension for X10 'ActiveHome' Controller
Group: Development/Perl
License: Artistic/GPL
Url: http://search.cpan.org/dist/X10-0.03/
Source: %m_distro-%version.tar.gz
Packager: Alex Negulescu <alecs@altlinux.org>
BuildRequires: perl-Astro-SunTime perl-Device-SerialPort perl-Storable perl-devel
Requires: perl-Astro-SunTime

%description
X10 - Perl extension for X10 'ActiveHome' Controller

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%clean
%__rm -rf %buildroot

%files
%_bindir/*
%_datadir/perl5/X10.pm
%_datadir/perl5/X10/*
%dir %perl_vendor_autolib/X10
%doc Changes MANIFEST README TODO devices macros.config ports scheduler.config

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.03-alt1.1
- redundant buildreq dropped

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 0.03-alt1
- initial build

