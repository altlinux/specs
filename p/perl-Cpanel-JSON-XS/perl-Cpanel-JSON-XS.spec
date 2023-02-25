%define _unpackaged_files_terminate_build 1
%define module_name Cpanel-JSON-XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Carp.pm) perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Test.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(common/sense.pm) perl(overload.pm) perl(charnames.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 4.35
Release: alt1
Summary: JSON::XS for Cpanel, fast and correct serialising, also for 5.6.2
Group: Development/Perl
License: perl
URL: http://software.schmorp.de/pkg/JSON-XS.html

Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/%{module_name}-%{version}.tar.gz

%description
This module converts Perl data structures to JSON and vice versa. Its.primary goal is to be *correct* and its secondary goal is to be
*fast*. To reach the latter goal it was written in C.

As this is the n-th-something JSON module on CPAN, what was the reason
to write yet another JSON module? While it seems there are many JSON
modules, none of them correctly handle all corner cases, and in most cases
their maintainers are unresponsive, gone missing, or not listening to bug
reports for other reasons.

See below for the Cpanel fork.

See MAPPING, below, on how Cpanel::JSON::XS maps perl values to JSON
values and vice versa.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release
BuildArch: noarch

%description scripts
scripts for %module_name


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 4.35-alt1
- automated CPAN update

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 4.32-alt1
- automated CPAN update

* Thu Aug 11 2022 Igor Vlasenko <viy@altlinux.org> 4.31-alt1
- automated CPAN update

* Mon Jun 20 2022 Igor Vlasenko <viy@altlinux.org> 4.30-alt1
- automated CPAN update

* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 4.29-alt1
- automated CPAN update

* Fri May 06 2022 Igor Vlasenko <viy@altlinux.org> 4.28-alt1
- automated CPAN update

* Fri Oct 15 2021 Igor Vlasenko <viy@altlinux.org> 4.27-alt1
- automated CPAN update

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 4.26-alt1
- automated CPAN update

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 4.25-alt1
- automated CPAN update

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 4.24-alt1
- automated CPAN update

* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 4.23-alt2
- fixed warning: scripts should be .noarch

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.23-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 4.21-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 4.19-alt1
- automated CPAN update

* Wed Dec 25 2019 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1
- automated CPAN update

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 4.17-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 4.15-alt1
- automated CPAN update

* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1
- automated CPAN update

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1
- automated CPAN update

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 4.10-alt1
- automated CPAN update

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 4.09-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.08-alt1.1
- rebuild with new perl 5.28.1

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.08-alt1
- automated CPAN update

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 4.07-alt1
- automated CPAN update

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1
- automated CPAN update

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 4.05-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- automated CPAN update

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.0239-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 3.0239-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.0237-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0233-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.0231-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.0230-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.0227-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.0225-alt1.1
- rebuild with new perl 5.24.1

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 3.0225-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.0223-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 3.0222-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.0218-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.0217-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 3.0216-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.0214-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.0213-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.0211-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.0210-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.0204-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.0115-alt1.1
- rebuild with new perl 5.22.0

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 3.0115-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 3.0114-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.0113-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.0106-alt1.1
- rebuild with new perl 5.20.1

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 3.0106-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 3.0104-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 3.0103-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.3404-alt1
- automated CPAN update

* Sat Nov 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.3403-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.3401-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.3401-alt1
- initial import by package builder

