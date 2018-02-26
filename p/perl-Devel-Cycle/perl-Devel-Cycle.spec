%define module Devel-Cycle

Name: perl-%module
Version: 1.11
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Devel::Cycle - Find memory cycles in objects
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Devel/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Dec 11 2009
BuildRequires: perl-PadWalker perl-devel

%description
This is a simple developer's tool for finding circular references in objects and
other types of references. Because of Perl's reference-count based memory
management, circular references will cause memory leaks.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Devel

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Dec 11 2009 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Tue Aug 05 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- Initial build.
