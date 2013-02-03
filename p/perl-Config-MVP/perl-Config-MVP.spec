## SPEC file for Perl module Config::MVP

Name: perl-Config-MVP
Version: 2.200003
Release: alt1

Summary: Perl module to work with multivalue-property INI files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Config-MVP/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Config-MVP
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Feb 03 2013
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Config-INI perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-IO-String perl-IPC-Run3 perl-List-MoreUtils perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Role-HasMessage perl-Role-Identifiable perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean
BuildRequires: perl-Config-MVP-Reader-INI perl-Devel-StackTrace perl-Test-Fatal perl-Test-Pod perl-Test-Script

%description
Perl module Config::MVP provides read and write access to the
multivalue-property .ini-file format. MVP is a mechanism for
loading configuration (or other information) for libraries.
It doesn't read a file or a database. It's a helper for
things that do.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/MVP*

%changelog
* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.200003-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.200002-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.200001-alt1
- Initial build for ALT Linux Sisyphus

