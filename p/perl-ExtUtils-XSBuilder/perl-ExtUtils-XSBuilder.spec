## SPEC file for Perl module ExtUtils-XSBuilder

%define version    0.28
%define release    alt1

Name: perl-ExtUtils-XSBuilder
Version: %version
Release: alt1.1

Summary: Perl extension for automatic Perl XS glue code generation

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~grichter/ExtUtils-XSBuilder/

BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name ExtUtils-XSBuilder
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Dec 13 2008
BuildRequires: perl-Parse-RecDescent perl-Tie-IxHash

%description
ExtUtils::XSBuilder is a set modules to parse C header files and
create XS glue code and documentation out of it. Idealy this 
allows to "write" an interface to a C library without coding a 
line. Since no C-API is ideal, some adjuments are necessary most
of the time. So to use this module you must still be familar
with C and XS programming, but it removes a lot of stupid work
and copy&paste from you.

# These files contains references to user-defined module
%add_findreq_skiplist */ExtUtils/XSBuilder/CallbackMap.pm
%add_findreq_skiplist */ExtUtils/XSBuilder/FunctionMap.pm
%add_findreq_skiplist */ExtUtils/XSBuilder/TypeMap.pm
%add_findreq_skiplist */ExtUtils/XSBuilder/StructureMap.pm

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/ExtUtils/XSBuilder*
%perl_vendor_privlib/ExtUtils/xsbuilder.osc2002.pod

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Dec 13 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.28-alt1
- Initial build for ALT Linux Sisyphus
