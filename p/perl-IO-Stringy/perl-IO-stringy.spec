%define dist IO-Stringy
Name: perl-%dist
Version: 2.113
Release: alt1

Summary: Filehandle-like I/O support for Perl in-core objects
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DS/DSKOLL/IO-Stringy-%{version}.tar.gz

BuildArch: noarch

# renamed by new upstream
Provides: perl-IO-stringy = %version
Conflicts: perl-IO-stringy < 2.113
Obsoletes: perl-IO-stringy < 2.113

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-devel

%description
This toolkit primarily provides modules for performing both traditional
and object-oriented I/O) on things other than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/IO

%changelog
* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 2.113-alt1
- new version
- renamed to perl-IO-Stringy following upstream

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 2.111-alt1
- automated CPAN update

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 2.110-alt2
- rebuilt

* Thu Mar 03 2005 Alexey Tourbin <at@altlinux.ru> 2.110-alt1
- 2.109 -> 2.110
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.109-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Mar 15 2004 Alexey Tourbin <at@altlinux.ru> 2.109-alt1
- 2.109

* Sat Jun 21 2003 Alexey Tourbin <at@altlinux.ru> 2.108-alt3
- specfile cleanup

* Tue Nov 05 2002 Alexey Tourbin <at@altlinux.ru> 2.108-alt2
- rebuilt for perl-5.8 with new rpm macros

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 2.108-alt1
- New version released.

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.220-alt3
- Rebuilt with perl-5.6.1

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 1.220-alt2
- Rewrite spec for compatible with new police

* Fri Jun 08 2001 Grigory Milev <week@altlinux.ru> 1.220-alt1
- new version (1.220)

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation
- cleanup spec
