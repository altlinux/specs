%define _unpackaged_files_terminate_build 1
%define dist Test-Object
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: Thoroughly testing objects via registered handlers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-devel

%description
"Test::Object" is a testing package designed to allow you to easily test
what you believe is a valid object against the expected behaviour of all
of the classes in its inheritance tree in one single call.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt3
- disabled build dependency on perl-Module-Install

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2
- rebuilt

* Sat Jun 16 2007 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- initial revision (for PPI)
