%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module Data::HexDump

%define real_name Data-HexDump

Name: perl-Data-HexDump
Version: 0.04
Release: alt1

Summary: Hexadecial Dumper

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/~ftassin/Data-HexDump/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: http://www.cpan.org/authors/id/N/NE/NEILB/Data-HexDump-%{version}.tar.gz

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses
BuildRequires: perl-devel

%description
Perl module Data::HexDump dumps in hexadecimal the content of a scalar.
The result is returned in a string. Each line of the result consists of
the offset in the source  in the leftmost column of each line, followed
by one  or more columns  of data  from the source  in hexadecimal.  The 
rightmost column of each line shows the printable characters (all 
others are shown as single dots)


%prep
%setup -q -n Data-HexDump-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_bindir/
mv -f -- eg/hexdump %buildroot%_bindir/hexdump.pl

%files
%doc README Changes

%perl_vendor_privlib/Data/HexDump*
%_bindir/hexdump.pl

%changelog
* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 0.04-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt1
- Initial build for ALT Linux Sisyphus
