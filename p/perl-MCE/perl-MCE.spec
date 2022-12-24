%define _unpackaged_files_terminate_build 1
%define module_name MCE
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MMCE::Util'
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Input*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Manager*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Validation*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Worker*
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(DBD/SQLite.pm) perl(DBI.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Path.pm) perl(Getopt/Long.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(Inline.pm) perl(Net/Ping.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(Symbol.pm) perl(Sys/Mmap.pm) perl(Test/More.pm) perl(Thread/Queue.pm) perl(Time/HiRes.pm) perl(base.pm) perl(bytes.pm) perl(constant.pm) perl(open.pm) perl(threads.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.882
Release: alt1.1
Summary: Many-Core Engine for Perl. Provides parallel processing capabilities.
Group: Development/Perl
License: perl
URL: http://code.google.com/p/many-core-engine-perl/

Source0: http://www.cpan.org/authors/id/M/MA/MARIOROY/%{module_name}-%{version}.tar.gz
BuildArch: noarch
# recommended by author
Requires: perl(Sereal/Decoder.pm) perl(Sereal/Encoder.pm)

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes Copying
%perl_vendor_privlib/M*

#%files scripts
#%_bindir/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.882-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 1.882-alt1
- automated CPAN update

* Fri Oct 14 2022 Igor Vlasenko <viy@altlinux.org> 1.881-alt1
- automated CPAN update

* Wed Oct 12 2022 Igor Vlasenko <viy@altlinux.org> 1.880-alt1
- automated CPAN update

* Wed May 25 2022 Igor Vlasenko <viy@altlinux.org> 1.879-alt1
- automated CPAN update

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 1.878-alt1
- automated CPAN update

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 1.876-alt1
- automated CPAN update

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 1.875-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.874-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.872-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.868-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.866-alt1
- automated CPAN update

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.865-alt1
- automated CPAN update

* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.864-alt1
- automated CPAN update

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.863-alt1
- automated CPAN update

* Sat Sep 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.862-alt1
- automated CPAN update

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.860-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.850-alt1
- automated CPAN update

* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.846-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.844-alt1
- automated CPAN update

* Wed Jul 31 2019 Igor Vlasenko <viy@altlinux.ru> 1.843-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.841-alt1
- automated CPAN update

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.838-alt1
- automated CPAN update

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.837-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.836-alt1
- automated CPAN update

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.835-alt1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.834-alt1
- automated CPAN update

* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.833-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.832-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.831-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.830-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.829-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.826-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.821-alt2
- added Requires (on Sereal::* ...) as suggested by author

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.821-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.820-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.813-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.811-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.810-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.809-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.808-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.806-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.805-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.804-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.803-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.708-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.707-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.706-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.705-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.703-alt1
- automated CPAN update

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.608-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.415-alt1
- initial import by package builder

