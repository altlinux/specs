%define module Mail-SPF

Name: perl-%module
Version: 2.8.0
Release: alt1

Summary: Perl module that implements Sender Policy Framework
License: BSD
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Mail/%module-v%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-Error perl-Mail-SPF-Test perl-Module-Build perl-Net-DNS-Resolver-Programmable perl-Test-Pod perl-URI

%description
Mail::SPF is an object-oriented Perl implementation of the Sender Policy
Framework (SPF) e-mail sender authentication system.

%prep
%setup -n %module-v%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# For now we exclude spfquery and spfd in favor of perl-Mail-SPF-Query.
# Will change this later?

%files
%exclude %_bindir/spfquery
%exclude %_sbindir/spfd
%perl_vendor_privlib/Mail/

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.8.0-alt1
- 2.8.0

* Sun Jan 30 2011 Victor Forsiuk <force@altlinux.org> 2.007-alt2
- Rebuild without man3 pages (fixes build with our new perl).

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 2.007-alt1
- 2.007

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 2.006-alt1
- 2.006

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 2.005-alt1
- 2.005

* Thu Aug 16 2007 Victor Forsyuk <force@altlinux.org> 2.004-alt2
- Fix build environment to ensure build tests will succeed.

* Tue May 22 2007 Victor Forsyuk <force@altlinux.org> 2.004-alt1
- Initial build.
