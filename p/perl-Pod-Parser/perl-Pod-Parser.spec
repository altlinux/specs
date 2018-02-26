%define dist Pod-Parser
Name: perl-%dist
Version: 1.51
Release: alt1

Summary: Modules for parsing/translating POD format documents
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-IO-String perl-devel perl-podlators

%description
B<Pod::Find> provides a set of functions to locate POD files.  Note that
no function is exported by default to avoid pollution of your namespace,
so be sure to specify them in the B<use> statement if you need them:

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%_bindir/pod*
%perl_vendor_privlib/Pod

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.38 -> 1.51

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- initial revision, for perl-5.12
