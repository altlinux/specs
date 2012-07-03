%define dist Class-Load
Name: perl-%dist
Version: 0.11
Release: alt1

Summary: A working (require "Class::Name") and more
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Data-OptList perl-Module-Runtime perl-Package-Stash perl-Test-Fatal

%description
"require EXPR" only accepts "Class/Name.pm" style module names,
not "Class::Name". How frustrating! For that, we provide
"load_class 'Class::Name'".

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.06 -> 0.11

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- initial revision, for DateTime::TimeZone
