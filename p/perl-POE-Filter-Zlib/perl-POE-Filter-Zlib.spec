%define module POE-Filter-Zlib

Name: perl-POE-Filter-Zlib
Version: 2.02
Release: alt2

Summary: A POE filter wrapped around Compress::Zlib

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: perl-Compress-Zlib perl-POE perl-Test-Pod perl-Test-Pod-Coverage

%description
POE::Filter::Zlib provides a POE filter for performing compression/uncompression using Compress::Zlib. It is suitable for use with POE::Filter::Stackable.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/Filter/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.02-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 2.02-alt1
- 2.02

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.01-alt1
- initial build for ALT Linux Sisyphus

