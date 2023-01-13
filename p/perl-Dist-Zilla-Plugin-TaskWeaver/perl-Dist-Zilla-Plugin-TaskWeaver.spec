## SPEC file for Perl module Dist::Zilla::Plugin::TaskWeaver

%define real_name Dist-Zilla-Plugin-TaskWeaver

Name: perl-Dist-Zilla-Plugin-TaskWeaver
Version: 0.101629
Release: alt1

Summary: a PodWeaver plugin used to build Task distributions

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-TaskWeaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Dist-Zilla perl-Encode perl-Moose perl-Parse-CPAN-Meta perl-Pod-Elemental perl-Pod-Weaver perl-devel perl-namespace-autoclean python-base python-modules python3-base
BuildRequires: perl-Dist-Zilla-Plugin-PodWeaver

%description
Perl module Dist::Zilla::Plugin::TaskWeaver acts just like the
PodWeaver plugin, but gets its claws just a bit into your
Pod::Weaver configuration and then uses them to figure out
prerequisites and grouping for building a Task distribution.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/TaskWeaver*
%perl_vendor_privlib/Pod*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.101629-alt1
- New version

* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.101628-alt2
- Initial build for ALT Linux Sisyphus
