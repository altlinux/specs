%define _unpackaged_files_terminate_build 1
BuildRequires: perl-podlators
%define dist File-MimeInfo
Name: perl-%dist
Version: 0.28
Release: alt1

Summary: Determine file type
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-File-DesktopEntry perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This module can be used to determine the mime type of a file; it's
a replacement for File::MMagic trying to implement the freedesktop
specification for using the shared mime-info database.  The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/File

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Fri Feb 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update
- script installation is disabled by author.

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update
- dropped File-MimeInfo-0.15-rt-66841.patch (in upstream)

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt3
- patch tests from rt.cpan.org #66841

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt2
- fixed unpackaged directory

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- remove man3 pages instead exclude ones

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt0.1
- New version 0.15
- Spec fila cleanup

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus
