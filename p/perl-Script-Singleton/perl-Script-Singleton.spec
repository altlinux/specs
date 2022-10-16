%define module_name Script-Singleton
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(IPC/Shareable.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: Ensure only a single instance of a script can run
Group: Development/Perl
License: artistic_2
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/ST/STEVEB/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Using shared memory, this distribution ensures only a single instance of any
script can be running at any one time.

There are no functions or methods. All the work is performed in the use
line. `LOCK' is the glue that identifies the shared memory segment. If a
second parameter with a true value is sent in, we'll output a warning if the
same script is run at the same time and it exits:

    use Script::Singleton 'LOCK', 1;

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/S*

%changelog
* Sun Oct 16 2022 Igor Vlasenko <viy@altlinux.org> 0.03-alt2
- to Sisyphus as perl-IPC-Shareable dep

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Mon Jul 19 2021 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

