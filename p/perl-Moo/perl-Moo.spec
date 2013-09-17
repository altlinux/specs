Name: perl-Moo
Version: 1.003001
Release: alt1

Summary: Moo - Minimalist Object Orientation (with Moose compatiblity)
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Moo.git
Url: %CPAN Moo
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-Dist-CheckConflicts perl-MRO-Compat perl-devel perl-Class-Method-Modifiers perl-strictures perl-Test-Fatal perl-Text-Balanced perl-Filter-Simple perl-Module-Runtime perl-Role-Tiny perl-Devel-GlobalDestruction
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
%exclude %_bindir/moo-outdated
%perl_vendor_privlib/Moo*
%perl_vendor_privlib/Method/Generate/*
%perl_vendor_privlib/Method/Inliner.pm
%perl_vendor_privlib/Sub/*
%perl_vendor_privlib/oo.pm
%doc Changes

%changelog
* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 1.003001-alt1
- 1.002000 -> 1.003001

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.002000-alt1
- 1.002000

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000004-alt1
- 1.000003 -> 1.000004
- don't require Moose

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000003-alt1
- 0.009014 -> 1.000003

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.009014-alt1
- 0.009014

* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.009011-alt1
- initial build
