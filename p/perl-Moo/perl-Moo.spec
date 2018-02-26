Name: perl-Moo
Version: 0.009014
Release: alt1

Summary: Moo - Minimalist Object Orientation (with Moose compatiblity)
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Moo.git
Url: %CPAN Moo
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-MRO-Compat perl-devel perl-Class-Method-Modifiers perl-strictures perl-Test-Fatal perl-Text-Balanced perl-Filter-Simple perl-Module-Runtime perl-Role-Tiny
BuildArch: noarch

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Moo*
%perl_vendor_privlib/Method/Generate/*
%perl_vendor_privlib/Method/Inliner.pm
%perl_vendor_privlib/Sub/*
%perl_vendor_privlib/oo.pm
%doc Changes

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.009014-alt1
- 0.009014

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.009011-alt1
- initial build
