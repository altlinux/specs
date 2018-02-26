## SPEC file for Perl module Throwable

Name: perl-Throwable
Version: 0.102080
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

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-parent
BuildRequires: perl-Devel-StackTrace perl-Moose perl-devel

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
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.102080-alt1
- Initial build for ALT Linux Sisyphus

