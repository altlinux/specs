## SPEC file for Perl module Path::Iterator::Rule

%define real_name Path-Iterator-Rule

Name: perl-Path-Iterator-Rule
Version: 1.012
Release: alt1

Summary: Iterative, recursive file finder

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Path-Iterator-Rule/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-Parse-CPAN-Meta perl-Path-Tiny perl-devel perl-parent python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-File-pushd perl-Number-Compare perl-PerlIO-utf8_strict perl-Test-Deep perl-Test-Filename perl-Text-Glob perl-Try-Tiny

%description
Perl module Path::Iterator::Rule iterates over files and
directories to identify ones matching a user-defined set
of rules. The API is based heavily on File::Find::Rule,
but with more explicit distinction between matching rules
and options that influence how directories are searched.
A "Path::Iterator::Rule" object is a collection of rules
(match criteria) with methods to add additional criteria.
Options that control directory traversal are given as
arguments to the method that generates an iterator.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Path/Iterator/Rule*
%perl_vendor_privlib/PIR*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 1.012-alt1
- Initial build for ALT Linux Sisyphus
