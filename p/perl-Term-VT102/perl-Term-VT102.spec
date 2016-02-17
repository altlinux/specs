# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(Net/Telnet.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(IO/Pty.pm)
%define upstream_name    Term-VT102
%define upstream_version 0.91

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_6

Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Source44: import.info


%description
The VT102 class provides emulation of most of the functions of a
DEC VT102 terminal. Once initialised, data passed to a VT102
object is processed and the in-memory screen modified accordingly.
This screen can be interrogated by the external program in a
variety of ways.

This allows your program to interface with full-screen console
programs by running them in a subprocess and passing their output
to a VT102 class. You can then see what the application has
written on the screen by querying the class appropriately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendor_privlib}/Term/VT102
%dir %{perl_vendor_privlib}/Term/VT102/examples
%{perl_vendor_privlib}/Term/VT102.pm
%{perl_vendor_privlib}/Term/VT102/examples/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_6
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- mageia import by cas@ requiest

