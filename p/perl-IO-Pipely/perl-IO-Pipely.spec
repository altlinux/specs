# BEGIN SourceDeps(oneline):
BuildRequires: perl(Errno.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(IO/Socket.pm) perl(Scalar/Util.pm) perl(Symbol.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.005
%define module_name IO-Pipely
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt2
Summary: Portably create pipe() or pipe-like handles, one way or another.
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/IO-Pipely/

Source0: http://cpan.org.ua/authors/id/R/RC/RCAPUTO/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README README.mkdn LICENSE
%perl_vendor_privlib/I*

%changelog
* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- initial import by package builder

