%define dist Apache-DBI

Name: perl-%dist
Version: 1.11
Release: alt1

Summary: Persistent database connections for mod_perl
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jul 17 2011
BuildRequires: perl-DBI perl-Digest-SHA1 perl-devel

%set_perl_req_method relaxed

%description
Apache::DBI and Apache::AuthDBI modules are supposed to be used with the
Apache server together with an embedded perl interpreter like mod_perl.
They provide support for basic authentication and authorization as well
as support for persistent database connections via Perl's Database
Independent Interface (DBI).

%prep
%setup -n %dist-%version

%build
%ifdef __buildreqs
# avoid build dependency on MySQL-server
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README traces.txt eg
%perl_vendor_privlib/Apache

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 1.11-alt1
- 1.11

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.10-alt1
- 1.10

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.09-alt1
- 1.09

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 1.08-alt1
- 1.08

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1.07-alt1
- 1.07

* Tue Nov 06 2007 Victor Forsyuk <force@altlinux.org> 1.06-alt2
- Drop build-time (and therefore run-time) requirement for apache-mod_perl
  to allow use of this module with either apache1- and apache2- flavours of
  mod_perl.
- Set relaxed method for perl requires finder to allow build in environment
  without mod_perl.

* Wed Apr 11 2007 Victor Forsyuk <force@altlinux.org> 1.06-alt1
- 1.06

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 1.05-alt1
- 1.05

* Thu Dec 23 2004 Alexey Tourbin <at@altlinux.ru> 0.94-alt1
- NMU: 0.91 -> 0.94
- manual pages not packaged (use perldoc)
- BuildArch: noarch
- specfile cleanup

* Wed Jul 28 2004 Maxim Tkachenko <tma@altlinux.ru> 0.91-alt1
- build for AltLinux
