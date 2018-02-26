%define dist DateTime-Locale
Name: perl-%dist
Version: 0.45
Release: alt2

Summary: Localization support for DateTime.pm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid rpmdb bloat
%add_findreq_skiplist */DateTime/Locale/[a-z]*.pm
%add_findprov_skiplist */DateTime/Locale/[a-z]*.pm

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-List-MoreUtils perl-Module-Build perl-Params-Validate perl-Test-Output

%description
DateTime::Locale is primarily a factory for the various locale
subclasses.  It also provides some functions for getting information
on available locales.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DateTime

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt2
- rebuilt as plain src.rpm

* Tue Mar 30 2010 Alexey Tourbin <at@altlinux.ru> 0.45-alt1
- 0.44 -> 0.45

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.43 -> 0.44

* Thu Jul 02 2009 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.42 -> 0.43

* Wed Nov 05 2008 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- 0.41 -> 0.42

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.41-alt1
- 0.4001 -> 0.41

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.35 -> 0.4001

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.34 -> 0.35

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- 0.22 -> 0.34

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- initial revision
