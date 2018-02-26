%define dist XML-RSS
Name: perl-%dist
Version: 1.49
Release: alt2

Summary: Creates and updates RSS files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-DateTime-Format-Mail perl-DateTime-Format-W3CDTF perl-HTML-Parser perl-Module-Build perl-Test-Differences perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage perl-XML-Parser

%description
This module was created to help those who need to manage
RDF Site Summary (RSS) files. It makes quick work of
creating, updating, and saving RSS files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/XML

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.49-alt2
- disabled build dependency on perl-XML-RSS

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- 1.48 -> 1.49
- rebuilt as plain src.rpm

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 1.48-alt1
- 1.46 -> 1.48

* Tue Oct 20 2009 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.44 -> 1.46

* Thu Apr 23 2009 Alexey Tourbin <at@altlinux.ru> 1.44-alt1
- 1.41 -> 1.44

* Fri Dec 12 2008 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.38 -> 1.41

* Sat Nov 29 2008 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- 1.37 -> 1.38

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.35 -> 1.37

* Sun Sep 14 2008 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.33 -> 1.35

* Sun Jun 08 2008 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.32 -> 1.33

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.31 -> 1.32

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.22 -> 1.31

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.05 -> 1.22

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.05-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.05-alt1
- 1.05
- Added missing BuildReqs

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 1.04-alt1
- 1.04

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt2
- Url and Summary was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt1
- First build for ALTLinux.

