# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/File.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Net-TFTP
%define upstream_version 0.19

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:	Net::TFTP - TFTP Client class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/Warn.pm)

BuildArch:	noarch
Source44: import.info


%description
Net::TFTP is a class implementing a simple Trivial File Transfer Protocol
client in Perl as described in RFC1350. Net::TFTP also supports the
TFTP Option Extension (as described in RFC2347), with the following options

RFC2348 Blocksize Option

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%{perl_vendor_privlib}/Net/TFTP.pm
#%{_mandir}/*/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.19-alt1_1
- mageia import by cas@ requiest

