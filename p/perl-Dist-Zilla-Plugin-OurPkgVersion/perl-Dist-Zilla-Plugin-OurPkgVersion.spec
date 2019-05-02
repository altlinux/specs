%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module Dist::Zilla::Plugin::OurPkgVersion

%define real_name Dist-Zilla-Plugin-OurPkgVersion

Name: perl-Dist-Zilla-Plugin-OurPkgVersion
Version: 0.15
Release: alt1

Summary: Dist::Zilla plugin for package version management

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-OurPkgVersion/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 02 2019
# optimized out: gem-power-assert perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Find-Rule-Perl perl-File-pushd perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS perl-Test-Version

%description
Perl module Dist::Zilla::Plugin::OurPkgVersion provides
an alternative to Dist::Zilla::Plugin::PkgVersion and
uses some code from that module.
It is designed to use a the more readable format our
$VERSION = $version; as well as not change then number
of lines of code in your files, which will keep your
repository more in sync with your CPAN release.
It also allows you slightly more freedom in how you
specify your version.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/OurPkgVersion*

%changelog
* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.15-alt1
- New version

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new version

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.12-alt1
- New version

* Tue Jul 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.11-alt1
- New version

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt2
- Bump release to override package from autoimports/Sisyphus repository

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- Initial build for ALT Linux Sisyphus
