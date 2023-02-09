%define _unpackaged_files_terminate_build 1
%define module_name String-Tagged-Terminal
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Convert/Color.pm) perl(Convert/Color/XTerm.pm) perl(Module/Build.pm) perl(String/Tagged.pm) perl(Test/More.pm) perl(Test2/V0.pm) perl(constant.pm) perl(experimental.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt1
Summary: format terminal output using String::Tagged
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This subclass of the String::Tagged manpage provides a method, `build_terminal',
for outputting the formatting tags embedded in the string as terminal escape
sequences, to render the the output in the appropriate style.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/S*

%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 0.06-alt1
- automated CPAN update

* Thu Dec 01 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Sat Aug 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

