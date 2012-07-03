%define dist AppConfig
Name: perl-%dist
Version: 1.66
Release: alt2

Summary: Perl module for reading configuration files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-devel

%description
AppConfig is a Perl5 module for managing application configuration
information.  It maintains the state of any number of variables and
provides methods for parsing configuration files, command line
arguments and CGI script parameters.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/AppConfig*

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.66-alt2
- rebuilt as plain src.rpm

* Wed Jul 18 2007 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.64 -> 1.66 (File::HomeDir dependency removed)
- changed src.rpm packaging to keep pristine tarball

* Sun Feb 25 2007 Alexey Tourbin <at@altlinux.ru> 1.64-alt1
- 1.63 -> 1.64

* Mon Oct 23 2006 Alexey Tourbin <at@altlinux.ru> 1.63-alt2
- imported sources into git and built with gear
- AppConfig/File.pm: localize $_ for while(<>) loop (cpan #22430)

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 1.63-alt1
- 1.56 -> 1.63

* Fri Mar 11 2005 Alexey Tourbin <at@altlinux.ru> 1.56-alt1
- 1.55 -> 1.56
- specfile cleanup and policy enforcement
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.55-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu May 01 2003 Alexey Gladkov <legion@altlinux.ru> 1.55-alt1
- First build for ALTLinux
- spec modifications for Sisyphus
- new verssion 1.55

* Tue Jan 21 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.52-4mdk
- fix requires error

* Fri Oct 18 2002 Clic-dev <clic-dev-public@mandrakesoft.com> 1.52-3mdk
- build with perl 5.8
- add perl version define

* Thu Jul 11 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.52-2mdk
- Build on 8.2 with perl 5.6

* Thu Apr 4 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.52-1mdk
- first release for Mandrakesoft
