Name: perl-Role-Tiny
Version: 1.003002
Release: alt1

Summary: Role::Tiny - minimalist role composition tool
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Role-Tiny.git
Url: %CPAN Role-Tiny
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-MRO-Compat perl-devel perl-Class-Method-Modifiers perl-Test-Fatal
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
%perl_vendor_privlib/Role/Tiny*
%doc Changes

%changelog
* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 1.003002-alt1
- 1.002005 -> 1.003002

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.002005-alt1
- 1.001005 -> 1.002005

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.001005-alt1
- 1.000000 -> 1.001005

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000000-alt1
- initial build

