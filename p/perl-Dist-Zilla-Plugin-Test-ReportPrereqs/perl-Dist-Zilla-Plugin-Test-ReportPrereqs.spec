## SPEC file for Perl module Dist::Zilla::Plugin::Test::ReportPrereqs

%define real_name Dist-Zilla-Plugin-Test-ReportPrereqs

Name: perl-Dist-Zilla-Plugin-Test-ReportPrereqs
Version: 0.029
Release: alt1

Summary: Report on prerequisite versions during automated testing

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Test-ReportPrereqs/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Data-Section perl-Encode perl-File-pushd perl-Moose perl-Parse-CPAN-Meta perl-Path-Tiny perl-Sub-Exporter-ForMethods perl-devel python-base python-modules python3-base
BuildRequires: perl-Dist-Zilla

%description
Perl module Dist::Zilla::Plugin::Test::ReportPrereqs is a Dist::Zilla
plugin that adds a t/00-report-prereqs.t test file and an accompanying
t/00-report-prereqs.dd data file. It reports the version of all
modules listed in the distribution metadata prerequisites (including
'recommends', 'suggests', etc.). However, any 'develop' prereqs are
not reported (unless they show up in another category).

%prep
%setup -q -n %real_name-%version

rm -f -- t/report.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Test/ReportPrereqs*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.029-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.028-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.027-alt1
- New version

* Sat May 06 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.026-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.025-alt1
- Initial build for ALT Linux Sisyphus
