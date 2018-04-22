## SPEC file for Perl module Config::MVP

Name: perl-Config-MVP
Version: 2.200011
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

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-StackTrace perl-Eval-Closure perl-Import-Into perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures
BuildRequires: perl-Class-XSAccessor perl-Config-MVP-Reader-INI perl-Test-Fatal perl-Variable-Magic

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
* Sat Apr 21 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.200011-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.200010-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.200008-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.200007-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.200006-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.200003-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.200002-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.200001-alt1
- Initial build for ALT Linux Sisyphus

