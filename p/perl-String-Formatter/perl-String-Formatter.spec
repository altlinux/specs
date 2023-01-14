## SPEC file for Perl module String-Formatter
%define _unpackaged_files_terminate_build 1
%define real_name String-Formatter

Name: perl-String-Formatter
Version: 1.235
Release: alt1

Summary: Perl module to build sprintf-like functions of your own

License: %gpl2only
Group: Development/Perl
URL: https://metacpan.org/dist/String-Formatter/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sun Nov 07 2021
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-JSON-PP perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Install perl-parent python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Sub-Exporter perl-devel

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

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.235-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.234-alt1
- New version
- Update URL

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.102084-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.102082-alt1
- Initial build for ALT Linux Sisyphus

