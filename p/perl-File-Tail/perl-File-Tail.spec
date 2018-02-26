%define dist File-Tail
Name: perl-%dist
Version: 0.99.3
Release: alt2

Summary: Perl extension for reading from continously updated files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-devel

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the "tail -f" directive). Usualy such files
are logfiles of some description.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
chmod -x logwatch select_demo

%files
%doc Changes README
%doc logwatch select_demo
%perl_vendor_privlib/File

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.99.3-alt2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.99.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 0.99.3-alt1
- 0.99.3

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.98-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Oct 07 2003 Igor Homyakov <homyakov at altlinux dot ru> 0.98-alt3
- fixed build with hasher
- fixed spec filename s/Fail/File/

* Wed Nov 06 2002 Sergey V Turchin <zerg at altlinux dot org> 0.98-alt2
- rebuild with new perl

* Wed Nov 28 2001 Igor Homyakov <homyakov at altlinux dot ru> alt1
- first build for ALTLinux distribution
