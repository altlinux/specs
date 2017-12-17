Name: perl-Cflow
Version: 1.053
Release: alt4.1.1.1.1
Summary: Find flows in raw IP flow files
Group: Development/Perl
License: GPLv2+
Url: http://net.doit.wisc.edu/~plonka/Cflow/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://net.doit.wisc.edu/~plonka/Cflow/Cflow-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: libflow-tools-ng-devel perl-devel perl-podlators

%description
Cflow with flow-tools support.  This module implements an API for
processing IP flow accounting information which as been collected from
routers and written into flow files.

%prep
%setup -q -n Cflow-%version

%build
%perl_vendor_build DEFINE=-DOSU LIBS=-lft INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc COPYING README Changes
%_bindir/flowdumper
%_man1dir/flowdumper.1*
%perl_vendor_archlib/Cflow*
%perl_vendor_autolib/Cflow

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.053-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.053-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.053-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.053-alt4.1
- rebuild with new perl 5.20.1

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.053-alt4
- fixed build

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.053-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.053-alt2
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 1.053-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.053-alt1.1
- rebuilt with perl 5.12

* Mon Dec 01 2008 Boris Savelev <boris@altlinux.org> 1.053-alt1
- initial build
