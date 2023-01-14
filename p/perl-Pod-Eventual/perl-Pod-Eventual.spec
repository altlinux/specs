## SPEC file for Perl module Pod-Eventual

Name: perl-Pod-Eventual
Version: 0.094003
Release: alt1

Summary: Perl module to read a POD document

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Pod-Eventual/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Pod-Eventual
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sun Dec 01 2013
# optimized out: perl-Data-OptList perl-IO-String perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-devel
BuildRequires: perl-Encode perl-Mixin-Linewise perl-Test-Deep

%description
Perl module Pod::Eventual reads line-based input and produces
events describing each POD paragraph or directive it finds.
Once complete events are immediately passed to the handle_event
method. This method should be implemented by Pod::Eventual
subclasses. If it isn't, Pod::Eventual's own handle_event
will be called, and will raise an exception.


%prep
%setup  -n %real_name-%version

# Fix test
/bin/sed -e 's~A#!perl~A#!/usr/bin/perl~' -i t/non-pod.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Eventual*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.094003-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.094002-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.094001-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.093330-alt1
- Initial build for ALT Linux Sisyphus

