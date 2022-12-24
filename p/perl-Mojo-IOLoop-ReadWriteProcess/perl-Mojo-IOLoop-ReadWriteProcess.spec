%define _unpackaged_files_terminate_build 1

Name: perl-Mojo-IOLoop-ReadWriteProcess
Version: 0.33
Release: alt1
Summary: Execute external programs or internal code blocks as separate process
License: Artistic-1.0 or GPL-1.0+
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojo-IOLoop-ReadWriteProcess/
Source0: http://www.cpan.org/authors/id/S/SZ/SZARATE/Mojo-IOLoop-ReadWriteProcess-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-devel perl(Test/Exception.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojo/File.pm)

Requires: perl(Mojolicious.pm)

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%setup -q -n Mojo-IOLoop-ReadWriteProcess-%{version}

%ifnarch %ix86 x86_64
# following test may fail on some architectures
rm -f t/12_mocked_container.t
%endif


%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Mojo/IOLoop*
%doc Changes README.md

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.33-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 0.32-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Tue Aug 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.20-alt1
- initial build for ALT
