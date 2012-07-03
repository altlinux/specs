%define dist SVN-Notify
Name: perl-%dist
Version: 2.83
Release: alt1

Summary: Perl module for Subversion activity notification
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

Provides: svnnotify = %version
Obsoletes: svnnotify < %version

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-IO-stringy perl-Module-Build perl-Net-SMTP-TLS perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Trac

%description
SVN::Notify is a Perl module for Subversion activity notification.

%prep
%setup -q -n %dist-%version

%build
export SENDMAIL=/usr/sbin/sendmail
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/svnnotify
%_man1dir/svnnotify.*
%perl_vendor_privlib/SVN

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.83-alt1
- 2.81 -> 2.83

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 2.81-alt1
- 2.80 -> 2.81
- merged svnnotify into perl-SVN-Notify

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.80-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 2.80-alt1
- 2.80

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 2.79-alt1
- 2.79

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 2.78-alt1
- 2.78

* Fri Aug 29 2008 Victor Forsyuk <force@altlinux.org> 2.77-alt1
- 2.77

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 2.75-alt1
- 2.75

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 2.70-alt1
- 2.70

* Wed Jul 25 2007 Victor Forsyuk <force@altlinux.org> 2.66-alt1
- 2.66

* Thu Jun 14 2007 Victor Forsyuk <force@altlinux.org> 2.65-alt1
- 2.65

* Tue Nov 14 2006 Andrei Bulava <abulava@altlinux.ru> 2.64-alt1
- 2.64

* Tue Jun 06 2006 Andrei Bulava <abulava@altlinux.ru> 2.59-alt1
- first build for ALT Linux Sisyphus
