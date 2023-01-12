## SPEC file for Perl module Config::MVP::Reader::INI

Name: perl-Config-MVP-Reader-INI
Version: 2.101465
Release: alt1

Summary: an MVP config reader for .ini files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Config-MVP-Reader-INI/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Config-MVP-Reader-INI
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Aug 31 2014
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-IO-String perl-Import-Into perl-List-MoreUtils perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Runtime perl-Moo perl-MooX-Types-MooseLike perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures
BuildRequires: perl-Config-INI perl-Config-MVP perl-Encode perl-Variable-Magic perl-devel perl-unicore

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
* Thu Jan 12 2023 Nikolay A. Fetisov <naf@altlinux.org> 2.101465-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.101464-alt2
- New version

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.101463-alt2
- NMU: fixed Url: (was set to Config-MVP, not Config-MVP-Reader-INI)

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.101463-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.101462-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.101461-alt1
- Initial build for ALT Linux Sisyphus

