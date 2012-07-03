## SPEC file for Perl module Pod-Eventual

Name: perl-Pod-Eventual
Version: 0.093330
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


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-IO-String perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-devel
BuildRequires: perl-Mixin-Linewise perl-Test-Deep

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
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.093330-alt1
- Initial build for ALT Linux Sisyphus

