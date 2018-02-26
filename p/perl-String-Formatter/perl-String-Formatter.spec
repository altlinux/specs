## SPEC file for Perl module String-Formatter

Name: perl-String-Formatter
Version: 0.102082
Release: alt1

Summary: Perl module to build sprintf-like functions of your own

License: %gpl2only
Group: Development/Perl
URL: http://search.cpan.org/dist/String-Formatter/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name String-Formatter
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-Params-Util perl-Sub-Install
BuildRequires: perl-Sub-Exporter perl-devel

%description
Perl module String::Formatter is a tool for building sprintf-like
formatting routines. It supports named or positional formatting,
custom conversions, fixed string interpolation, and simple
width-matching out of the box. It is easy to alter its behavior
to write new kinds of format string expanders. For most cases,
it should be easy to build all sorts of formatters out of the
options built into String::Formatter.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/String/Formatter*

%exclude %perl_vendor_privlib/String/bench.pl

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.102082-alt1
- Initial build for ALT Linux Sisyphus

