%define dist Log-Dispatch

Name: perl-%dist
Version: 2.29
Release: alt1

Summary: Dispatches messages to one or more outputs
License: Artistic 2.0
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: apache-mod_perl-base perl-MIME-Lite perl-Mail-Sender perl-Mail-Sendmail perl-Params-Validate

%description
Log::Dispatch is a suite of OO modules for logging messages to multiple
outputs, each of which can have a minimum and maximum log level. It is
designed to be easily subclassed, both for creating a new dispatcher object
and particularly for creating new outputs.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# Exclude file that will generate mod_perl requirement:
%add_findreq_skiplist %perl_vendor_privlib/Log/Dispatch/ApacheLog.pm

%files
%doc README Changes
%perl_vendor_privlib/Log/

%changelog
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
