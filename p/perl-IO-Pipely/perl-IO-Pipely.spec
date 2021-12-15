%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Errno.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(IO/Socket.pm) perl(Scalar/Util.pm) perl(Symbol.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name IO-Pipely
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.006
Release: alt1
Summary: Portably create pipe() or pipe-like handles, one way or another.
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/IO-Pipely/

Source0: http://www.cpan.org/authors/id/R/RC/RCAPUTO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README README.mkdn
%perl_vendor_privlib/I*

%changelog
* Wed Dec 15 2021 Igor Vlasenko <viy@altlinux.org> 0.006-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- initial import by package builder

