%define _unpackaged_files_terminate_build 1
%define module_name Getopt-Kingpin
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Digest/MD5.pm) perl(Module/Build/Tiny.pm) perl(Object/Simple.pm) perl(Path/Tiny.pm) perl(Test/Exception.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.11
Release: alt1
Summary: command line options parser (like golang kingpin)
Group: Development/Perl
License: perl
URL: https://github.com/sago35/Getopt-Kingpin

Source0: http://www.cpan.org/authors/id/T/TA/TAKASAGO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Getopt::Kingpin is a command line parser.
It supports flags and positional arguments.

=over

=item *

Simple to use

=item *

Automatically generate help flag (--help).

=back


This module is inspired by Kingpin written in golang.
https://github.com/alecthomas/kingpin


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/G*

%changelog
* Tue Aug 22 2023 Igor Vlasenko <viy@altlinux.org> 0.11-alt1
- automated CPAN update

* Wed Jul 13 2022 Igor Vlasenko <viy@altlinux.org> 0.10-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Mon Nov 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated by package builder

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Mon Aug 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

