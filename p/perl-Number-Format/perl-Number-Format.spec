%define module Number-Format

Name: perl-%module
Version: 1.73
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module converts numbers to strings with pretty formatting
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/W/WR/WRW/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jun 14 2007
BuildRequires: perl-devel

%description
Number::Format is a library for formatting numbers. Functions are provided for
converting numbers to strings in a variety of ways, and to convert strings that
contain numbers back into numeric form. The output formats may include thousands
separators - characters inserted between each group of three characters counting
right to left from the decimal point. The characters used for the decimal point
and the thousands separator come from the locale information or can be specified
by the user.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files 
%perl_vendor_privlib/Number*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 1.73-alt1
- 1.73

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 1.72-alt1
- 1.72

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 1.61-alt1
- 1.61

* Thu Jun 14 2007 Victor Forsyuk <force@altlinux.org> 1.52-alt1
- 1.52

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.45-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.45-alt1
- rebuild with new perl

* Sat Mar 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.44-alt1
- First build for Sisyphus.
