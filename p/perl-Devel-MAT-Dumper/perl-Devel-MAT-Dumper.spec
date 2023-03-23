%define _unpackaged_files_terminate_build 1
%define module_name Devel-MAT-Dumper
%set_perl_req_method relaxed
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(File/Spec.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.47
Release: alt1
Summary: write a heap dump file for later analysis
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides the memory-dumping function that creates a heap dump file
which can later be read by the Devel::MAT::Dumpfile manpage. It provides a single
function which is not exported, which writes a file to the given path.

The dump file will contain a representation of every SV in Perl's arena,
providing information about pointers between them, as well as other
information about the state of the process at the time it was created. It
contains a snapshot of the process at that moment in time, which can later be
loaded and analysed by various tools using `Devel::MAT::Dumpfile'.

This module used to be part of the main the Devel::MAT manpage distribution but is now
in its own one so that it can be installed independently on servers or other
locations where perl processes need to inspected but analysis tools can be run
elsewhere.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README doc
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.47-alt1
- automated CPAN update

* Thu Dec 01 2022 Igor Vlasenko <viy@altlinux.org> 0.46-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Tue Sep 13 2022 Igor Vlasenko <viy@altlinux.org> 0.46-alt1
- updated by package builder

* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 0.45-alt1
- updated by package builder

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.44-alt1
- updated by package builder

* Tue Mar 01 2022 Igor Vlasenko <viy@altlinux.org> 0.43-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.42-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.42-alt2
- rebuild with perl 5.30

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- updated by package builder

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- updated by package builder

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- regenerated from template by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.39-alt1.1
- rebuild with perl 5.28.1

* Thu Jan 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- regenerated from template by package builder

* Wed Jan 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Wed Jul 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- regenerated from template by package builder

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- initial import by package builder

