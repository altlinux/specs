## SPEC file for Perl module Config::MVP::Reader::INI

Name: perl-Config-MVP-Reader-INI
Version: 2.101461
Release: alt1

Summary: an MVP config reader for .ini files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Config-MVP/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Config-MVP-Reader-INI
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-IO-String perl-List-MoreUtils perl-MRO-Compat perl-Mixin-Linewise perl-Module-Runtime perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Role-HasMessage perl-Role-Identifiable perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-Config-INI perl-Config-MVP perl-devel

%description
Perl module Config::MVP::Reader::INI reads .ini files containing
MVP-style configuration.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/MVP/Reader/INI*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.101461-alt1
- Initial build for ALT Linux Sisyphus

