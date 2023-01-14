## SPEC file for Perl module Dist::Zilla::PluginBundle::RJBS

%define real_name Dist-Zilla-PluginBundle-RJBS

Name: perl-Dist-Zilla-PluginBundle-RJBS
Version: 5.022
Release: alt1

Summary: BeLike::RJBS when you build your dists

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-PluginBundle-RJBS/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Dist-Zilla perl-Encode perl-Moose perl-Parse-CPAN-Meta perl-Pod-Elemental perl-Pod-Elemental-PerlMunger perl-Pod-Weaver perl-devel python-base python-modules python3-base
BuildRequires: perl-Dist-Zilla-Plugin-CheckChangesHasContent perl-Dist-Zilla-Plugin-CheckExtraTests perl-Dist-Zilla-Plugin-CheckPrereqsIndexed perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-Git-Contributors perl-Dist-Zilla-Plugin-GithubMeta perl-Dist-Zilla-Plugin-PodWeaver perl-Dist-Zilla-Plugin-PromptIfStale perl-Dist-Zilla-Plugin-TaskWeaver perl-Dist-Zilla-Plugin-Test-ReportPrereqs perl-Pod-Elemental-Transformer-List perl-Pod-Weaver-Section-Contributors

%description
Perl module Dist::Zilla::PluginBundle::RJBS is a Dist::Zilla plugin
to bundle settings that RJBS uses.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/PluginBundle/RJBS*
%exclude %perl_vendor_privlib/Dist/Zilla/App/Command/*
%perl_vendor_privlib/Pod*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 5.022-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.020-alt1
- New version

* Sat Jul 03 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.019-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.018-alt1
- New version

* Tue Jun 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.017-alt1
- New version

* Sat May 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.015-alt1
- New version

* Thu Mar 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.013-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 5.012-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 5.010-alt2
- Initial build for ALT Linux Sisyphus
