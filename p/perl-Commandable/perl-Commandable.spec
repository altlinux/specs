%define _unpackaged_files_terminate_build 1
%define module_name Commandable
%set_perl_req_method relaxed
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Attribute/Storage.pm) perl(Convert/Color.pm) perl(Module/Build.pm) perl(Module/Pluggable/Object.pm) perl(String/Tagged.pm) perl(String/Tagged/Terminal.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt1.1
Summary: utilities for commandline-based programs
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This distribution contains a collection of utilities extracted from various
commandline-based programs I have written, in the hope of trying to find a
standard base to build these from in future.

Note that "commandline" does not necessarily mean "plain-text running in a
terminal"; simply that the mode of operation is that the user types a textual
representation of some action, and the program parses this text in order to
perform it. This could equally apply to a command input text area in a GUI
program.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/C*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.09-alt1
- automated CPAN update

* Wed Nov 30 2022 Igor Vlasenko <viy@altlinux.org> 0.08-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Thu Jul 14 2022 Igor Vlasenko <viy@altlinux.org> 0.08-alt1
- updated by package builder

* Thu Apr 28 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt1
- updated by package builder

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 0.06-alt1
- updated by package builder

* Wed Oct 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Thu Feb 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Mon Oct 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Fri Jun 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

