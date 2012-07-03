%define module Mail-SPF-Query

Name: perl-%module
Version: 1.999.1
Release: alt2.1

Summary: Mail-SPF-Query perl module
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Mail/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 29 2007
BuildRequires: perl-Net-CIDR-Lite perl-Net-DNS perl-Sys-Hostname-Long perl-URI perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This module implements a daemon to query SPF records for email forgery
detection.

%prep
%setup -n %module-%version

%build
# one-liner fix to keep perl.req from panic :)
#subst 's/perl -w-/perl/' spfquery

# Tests depends on DNS queries, so unreliable.
%def_disable test
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

# resolve conflicts with libspf2-tools
mv $RPM_BUILD_ROOT%_bindir/spfd $RPM_BUILD_ROOT%_bindir/spfd.perl
mv $RPM_BUILD_ROOT%_bindir/spfquery $RPM_BUILD_ROOT%_bindir/spfquery.perl
mv $RPM_BUILD_ROOT%_man1dir/spfd.1 $RPM_BUILD_ROOT%_man1dir/spfd.perl.1
mv $RPM_BUILD_ROOT%_man1dir/spfquery.1 $RPM_BUILD_ROOT%_man1dir/spfquery.perl.1

%files
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/*
%exclude /.perl.req
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.999.1-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Dec 29 2007 Victor Forsyuk <force@altlinux.org> 1.999.1-alt2
- Refresh build requirements.

* Wed Sep 06 2006 Victor Forsyuk <force@altlinux.ru> 1.999.1-alt1
- 1.999.1

* Fri Mar 11 2005 Victor Forsyuk <force@altlinux.ru> 1.997-alt1
- Initial build for Sisyphus.
