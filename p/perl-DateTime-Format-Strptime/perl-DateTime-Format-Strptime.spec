%define module DateTime-Format-Strptime

Name: perl-%module
Version: 1.5000
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module to parse and format strp and strf time patterns
License: Artistic 2.0
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-DateTime perl-devel

%description
This module replicates most of Strptime for DateTime. Strptime is the unix
command that is the reverse of Strftime. While Strftime takes a DateTime and
outputs it in a given format, Strptime takes a DateTime and a format and
returns the DateTime object associated.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/DateTime

%changelog
* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 1.5000-alt1
- 1.5000

* Tue Jul 06 2010 Victor Forsiuk <force@altlinux.org> 1.4000-alt1
- 1.4000

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 1.2000-alt1
- 1.2000

* Thu Jul 16 2009 Victor Forsyuk <force@altlinux.org> 1.1000-alt1
- 1.1000

* Tue Mar 24 2009 Victor Forsyuk <force@altlinux.org> 1.0900-alt1
- 1.0900

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 1.0800-alt1
- 1.0800

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 1.0702-alt1
- Initial build.
