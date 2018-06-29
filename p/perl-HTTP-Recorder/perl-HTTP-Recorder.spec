%define _unpackaged_files_terminate_build 1
%define dist HTTP-Recorder
Name: perl-%dist
Version: 0.07
Release: alt2

Summary: record interaction with websites
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SE/SEMUELF/HTTP-Recorder-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-HTTP-Request-Params perl-Test-Pod perl-libwww perl-podlators

%description
This is a browser-independent recorder for recording interactions with
web sites.

%if_with scripts
%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %EVR

# for scripts
BuildRequires: perl(HTTP/Proxy.pm)

%description scripts
scripts for %name
%endif

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/HTTP*
%exclude %_bindir/*
%exclude %_man1dir/*

%if_with scripts
%files scripts
%_bindir/*
%_man1dir/*
%endif

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- fixed unpackaged files

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2
- updated build dependencies

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
