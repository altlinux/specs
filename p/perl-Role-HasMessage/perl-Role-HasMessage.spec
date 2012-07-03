## SPEC file for Perl module Role-HasMessage

Name: perl-Role-HasMessage
Version: 0.005
Release: alt1

Summary: Perl module to provide a thing with an message method

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Role-HasMessage/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Role-HasMessage
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-String-Formatter perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Time-Piece perl-Try-Tiny perl-Variable-Magic perl-parent
BuildRequires: perl-MooseX-Role-Parameterized perl-String-Errf perl-devel perl-namespace-clean

%description
Perl module Role::HasMessage provides a thing with an message method.
This is another extremely simple role. A class that includes 
Role::HasMessage is promising to provide a message method that returns
a string summarizing the message or event represented by the object.
It does not provide any actual behavior.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Role/HasMessage*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- Initial build for ALT Linux Sisyphus

