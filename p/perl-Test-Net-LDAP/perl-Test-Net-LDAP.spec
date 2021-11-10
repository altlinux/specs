%define module_version 0.07
%define module_name Test-Net-LDAP
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Socket.pm) perl(Net/LDAP.pm) perl(Net/LDAP/Bind.pm) perl(Net/LDAP/Constant.pm) perl(Net/LDAP/Entry.pm) perl(Net/LDAP/Filter.pm) perl(Net/LDAP/FilterMatch.pm) perl(Net/LDAP/RootDSE.pm) perl(Net/LDAP/Search.pm) perl(Net/LDAP/Util.pm) perl(Scalar/Util.pm) perl(Test/Builder.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: A Net::LDAP subclass for testing
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MAHIRO/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 0.07-alt2
- Rebuild by human.

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

