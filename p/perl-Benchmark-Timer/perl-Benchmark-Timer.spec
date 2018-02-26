%define module Benchmark-Timer

Name: perl-%module
Version: 0.7102
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Benchmarking with statistical confidence
License: GPLv2
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 22 2010
BuildRequires: perl-Module-Install perl-Statistics-TTest

%description
The Benchmark::Timer class allows you to time portions of code conveniently, as
well as benchmark code by allowing timings of repeated trials. It is perfect
for when you need more precise information about the running time of portions
of your code than the Benchmark module will give you, but don't want to go all
out and profile your code.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Benchmark

%changelog
* Mon Nov 22 2010 Victor Forsiuk <force@altlinux.org> 0.7102-alt1
- Initial build.
