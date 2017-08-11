%define module_version 1.28
%define module_name VM-EC2
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/CacheDNS.pm) perl(AnyEvent/HTTP.pm) perl(Digest/SHA.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Path.pm) perl(FindBin.pm) perl(HTTP/Request/Common.pm) perl(JSON.pm) perl(LWP.pm) perl(LWP/UserAgent.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(String/Approx.pm) perl(Test/More.pm) perl(URI.pm) perl(URI/Escape.pm) perl(URI/URL.pm) perl(XML/Simple.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.28
Release: alt2.1
Summary: Control the Amazon EC2 and Eucalyptus Clouds
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LD/LDS/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc DISCLAIMER.txt Changes README LICENSE
%perl_vendor_privlib/V*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Fri Aug 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2.1
- rebuild with new perl

* Sat May 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2
- to Sisyphus

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- regenerated from template by package builder

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- initial import by package builder

