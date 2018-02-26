%define dist CPAN-Meta-YAML
Name: perl-%dist
Version: 0.004
Release: alt1

Summary: Read and write a subset of YAML for CPAN Meta files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-YAML perl-YAML-Syck perl-devel

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like META.yml and MYMETA.yml.
It should not be used for any other general YAML parsing or generation
task.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CPAN

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.004-alt1
- initial revision
