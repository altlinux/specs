%define m_distro ORLite
Name: perl-ORLite
Version: 1.50
Release: alt1
Summary: ORLite - Extremely light weight SQLite-specific ORM

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/ORLite/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Params-Util perl-DBI perl-DBD-SQLite perl-File-Remove perl-Test-Script

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ORLite*
%doc Changes README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.48-alt1
- New version 1.48

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 1.47-alt1
- New version 1.47

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.46-alt1
- New version 1.46

* Wed Aug 11 2010 Vladimir Lettiev <crux@altlinux.ru> 1.45-alt1
- New version 1.45

* Mon Jul 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.44-alt1
- New version 1.44

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.43-alt1
- New version 1.43

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- New version 1.42

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.32-alt1
- initial build
