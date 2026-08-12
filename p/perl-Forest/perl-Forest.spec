%define real_name Forest

Name: perl-%real_name
Version: 0.10
Release: alt1

Summary: A collection of n-ary tree related modules

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/S/ST/STEVAN/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Moose perl-MooseX-Clone perl-Path-Class perl-Test-Exception perl-Test-LongString

%description
Forest is a collection of n-ary tree related modules for Perl, built on top
of Moose. It provides a flexible tree abstraction with pure and mutable tree
implementations, readers, writers, indexers and loaders for serializing trees
to and from various formats (ASCII, HTML, JSON, text files).

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Forest*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for Sisyphus
