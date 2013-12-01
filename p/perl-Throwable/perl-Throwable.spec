## SPEC file for Perl module Throwable

Name: perl-Throwable
Version: 0.200009
Release: alt1

Summary: Perl role for classes that are meant to be thrown as exceptions

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Throwable/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Throwable
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Aug 03 2013
# optimized out: perl-Class-Load perl-Class-Method-Modifiers perl-Data-OptList perl-Devel-GlobalDestruction perl-IPC-Run3 perl-Module-Implementation perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Role-Tiny perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-devel perl-strictures
BuildRequires: perl-Devel-StackTrace perl-Moo perl-MooX-Types-MooseLike perl-Test-Pod perl-Test-Script

%description
Perl module Throwable is a role for classes that are meant to be
thrown as exceptions to standard program flow. It is very simple
and does only two things: saves any previous value for $@ and
calls die $self.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Throwable*
%perl_vendor_privlib/StackTrace*

%changelog
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.200009-alt1
- New version

* Sat Aug 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.200008-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.102080-alt1
- Initial build for ALT Linux Sisyphus

