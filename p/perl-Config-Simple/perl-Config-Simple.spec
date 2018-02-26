%define dist Config-Simple

Name: perl-%dist
Version: 4.59
Release: alt1.1

Summary: Simple configuration file class
Group: Development/Perl
License: GPL or Artistic

Url: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Config/SHERZODR/Config-Simple-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Jan 20 2007
BuildRequires: perl-devel

%description
Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Config
%perl_vendor_privlib/auto/Config

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 4.59-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 4.59-alt1
- 4.59

* Sat Feb 19 2005 Leonid Shalupov <shalupov@altlinux.ru> 4.58-alt1
- 4.58

* Tue Nov 09 2004 Leonid Shalupov <shalupov@altlinux.ru> 4.57-alt1
- Initial build
