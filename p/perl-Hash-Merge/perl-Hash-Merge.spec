%define _unpackaged_files_terminate_build 1
%define dist Hash-Merge
Name: perl-%dist
Version: 0.299
Release: alt1

Summary: Merges arbitrarily deep hashes into a single hash
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HE/HERMES/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Clone perl-devel perl(Clone/Choose.pm)

%description
Hash::Merge merges two arbitrarily deep hashes into a single hash.  That
is, at any level, it will add non-conflicting key-value pairs from one
hash to the other, and follows a set of specific rules when there are key
value conflicts (as outlined below).  The hash is followed recursively,
so that deeply nested hashes that are at the same level will be merged 
when the parent hashes are merged.  B<Please note that self-referencing
hashes, or recursive references, are not handled well by this method.>

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes MAINTAINER.md README.md
%perl_vendor_privlib/Hash*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.299-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.200-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision, for DBIx::Class
