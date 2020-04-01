%define _unpackaged_files_terminate_build 1
%define dist JSON-XS3

Name: perl-%dist
Version: 3.04
Release: alt1

Summary: JSON serialising/deserialising, done correctly and fast
License: GPLv2+ or Artistic-2.0
Group: Development/Perl

URL: https://metacpan.org/author/MLEHMANN
Source0: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Encode perl-common-sense perl-devel perl(Types/Serialiser.pm) perl(Canary/Stability.pm)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be *correct* and its secondary goal is to be
*fast*. To reach the latter goal it was written in C.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/json_xs3
%perl_vendor_archlib/JSON
%perl_vendor_autolib/JSON

%changelog
* Wed Apr 01 2020 Igor Vlasenko <viy@altlinux.ru> 3.04-alt1
- compat version

