# BEGIN SourceDeps(oneline):
BuildRequires: perl(CGI.pm) perl(ExtUtils/MakeMaker.pm) perl(FCGI.pm) perl(Test/More.pm) perl(if.pm)
# END SourceDeps(oneline)
%define module_version 2.00
%define module_name CGI-Fast
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.00
Release: alt2
Summary: unknown
Group: Development/Perl
License: perl
URL: https://metacpan.org/module/CGI::Fast

Source0: http://cpan.org.ua/authors/id/L/LE/LEEJO/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
CGI::Fast is a subclass of the CGI object created by CGI.pm.  It is
specialized to work well FCGI module, which greatly speeds up CGI
scripts by turning them into persistently running server processes.
Scripts that perform time-consuming initialization processes, such as
loading large modules or opening persistent database connections, will
see large performance improvements.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/C*

%changelog
* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2
- moved to Sisyphus as dependency

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- initial import by package builder

