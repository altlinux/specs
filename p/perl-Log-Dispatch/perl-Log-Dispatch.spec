%define _unpackaged_files_terminate_build 1
%define dist Log-Dispatch

Name: perl-%dist
Version: 2.63
Release: alt1

Summary: Dispatches messages to one or more outputs
License: Artistic 2.0
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: apache-mod_perl-base perl-MIME-Lite perl-Mail-Sender perl-Mail-Sendmail perl-Params-Validate perl(Class/Load.pm) perl(Test/Fatal.pm) perl(Test/Requires.pm) perl(Devel/GlobalDestruction.pm) perl(Test/Needs.pm) perl(namespace/autoclean.pm) perl(Specio/Exporter.pm) perl(Params/ValidationCompiler.pm)

%description
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level. It is
designed to be easily subclassed, both for creating a new dispatcher object
and particularly for creating new outputs.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# Exclude file that will generate mod_perl requirement:
%add_findreq_skiplist %perl_vendor_privlib/Log/Dispatch/ApacheLog.pm

%files
%doc README.md Changes CONTRIBUTING.md
%perl_vendor_privlib/Log/

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.63-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.62-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.58-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.57-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.56-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.54-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.51-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.44-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.43-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.42-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.41-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 2.29-alt1
- 2.29

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 2.27-alt1
- 2.27
- License is now Artistic 2.0.

* Thu Mar 25 2010 Victor Forsiuk <force@altlinux.org> 2.26-alt2
- Disable install time requirement for mod_perl.

* Fri Nov 20 2009 Victor Forsyuk <force@altlinux.org> 2.26-alt1
- 2.26

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt1
- new version 2.22 (with rpmrb script)

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 2.21-alt1
- 2.21

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 2.20-alt1
- 2.20

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 2.18-alt1
- 2.18
- Run buildreq to get modern build requirements.

* Wed Aug 24 2005 Alexey Morozov <morozov@altlinux.org> 2.11-alt1
- Initial build for ALT Linux.
