Name: swatch
Version: 3.2.3
Release: alt1

Summary: Simple log watcher
License: GPLv2+
Group: Monitoring

Url: http://swatch.sourceforge.net
Source: http://download.sourceforge.net/swatch/%name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-Date-Calc perl-Date-Manip perl-File-Tail perl-TimeDate perl-devel perl-podlators

%description
Swatch was originally written to actively monitor messages as they are written
to a log file via the UNIX syslog utility. For a simple demonstration type
"perl swatch --examine=FILENAME" with FILENAME being the file that you would
like to see the contents of. All this example will do is demonstrate the
different text modes that are available with to the echo action.

%prep
%setup

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README KNOWN_BUGS
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/Swatch/
%perl_vendor_privlib/auto/Swatch/

%changelog
* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 3.2.2-alt1.1
- rebuilt with perl 5.12

* Mon Mar 10 2008 Slava Semushin <php-coder@altlinux.ru> 3.2.2-alt1
- NMU
- Updated to 3.2.2

* Fri Jun 22 2007 Slava Semushin <php-coder@altlinux.ru> 3.2.1-alt1
- NMU
- Updated to 3.2.1 (also should fix #12101)
- Use macros from perl-devel package for building and installation
- Exclude COPYING and COPYRIGHT files from package
- Spec cleanup:
  + Replaced tabs to one space
  + Updated Url tag
  + Set Packager tag to previous maintainer
  + Updated url in Source tag
  + Updated BuildRequires
  + Don't use %%name macros in %%description
  + s|%%setup -q -n %%name-%%version|%%setup|
  + s|%%_mandir|man1/%%_man1dir|

* Fri May 16 2003 Igor Homyakov <homyakov at altlinux dot ru> 3.0.8-alt1
- 3.0.8

* Mon Apr 15 2002 Igor Homyakov <homyakov at altlinux dot ru> 3.0.4-alt3
- spec cleanup

* Thu Jan 31 2002 Igor Homyakov <homyakov at altlinux dot ru> alt2
- spec file cleanup

* Sun Dec  2 2001 Igor Homyakov <homyakov at altlinux dot ru> alt1
- build 3.0.4 package
