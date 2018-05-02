%define _unpackaged_files_terminate_build 1
%define dist File-HomeDir
Name: perl-%dist
Version: 1.004
Release: alt1

Summary: Get the home directory for yourself or other users
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RE/REHSACK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-File-Which perl-Pod-Escapes perl-devel perl-prefork

%description
File::HomeDir is a module for dealing with issues relating to the
location of directories for various purposes that are "owned" by a user,
and to solve these problems consistently across a wide variety of
platforms.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/File

%changelog
* Wed May 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.98-alt2
- disabled build dependency on perl-Module-Install

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.98-alt1
- 0.93 -> 0.98
- rebuild as plain src.rpm

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 0.93-alt1
- 0.80 -> 0.93 (Closes: #24065)
- build with bundled Module::Install (requires version >= 1.0.0)
- new build dep: perl-File-Which

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.80-alt1
- 0.65 -> 0.80

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 0.65-alt1
- 0.63 -> 0.65

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 0.63-alt1
- 0.60_03 -> 0.63

* Thu Oct 26 2006 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.58 -> 0.60_03
- imported sources into git and built with gear

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 0.58-alt1
- initial revision, for AppConfig 1.63
