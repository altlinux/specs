%define _unpackaged_files_terminate_build 1
%define dist Glib
Name: perl-%dist
Version: 1.326
Release: alt1.1

Summary: Perl module for the glib-2.x library
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/X/XA/XAOC/%{dist}-%{version}.tar.gz
Patch: perl-Glib-1.224-alt-glib_version.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: glib2-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-devel

%package devel
Summary: Perl module for the glib-2.x library (development files)
Group: Development/Perl
Requires: %name = %version-%release
Requires: glib2-devel

%description
This module provides perl access to Glib and GLib's GObject libraries.
GLib is a portability and utility library; GObject provides a generic
type system with inheritance and a powerful signal system.  Together
these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

%description devel
This module provides perl access to Glib and GLib's GObject libraries.
GLib is a portability and utility library; GObject provides a generic
type system with inheritance and a powerful signal system.  Together
these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

This package contains GLib development files and documentation
for developers (overview of internals and internal API reference).

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

# disable build dependency on perl-podlators
sed -i- '/MAN3PODS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS NEWS README ChangeLog.pre-git copyright.pod
	%perl_vendor_archlib/Glib.pm
%dir	%perl_vendor_archlib/Glib
%dir	%perl_vendor_archlib/Glib/Object
	%perl_vendor_archlib/Glib/Object/Subclass.pm
%dir	%perl_vendor_autolib/Glib
	%perl_vendor_autolib/Glib/Glib.so

%files devel
%dir	%perl_vendor_archlib/Glib
	%perl_vendor_archlib/Glib/*.pm
%doc	%perl_vendor_archlib/Glib/*.pod
%dir	%perl_vendor_archlib/Glib/Install
	%perl_vendor_archlib/Glib/Install/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.326-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.326-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.325-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.324-alt1.1
- rebuild with new perl 5.24.1

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.324-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.323-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.321-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.320-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.308-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.307-alt1.1
- rebuild with new perl 5.22.0

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.307-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.306-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.305-alt1.1
- rebuild with new perl 5.20.1

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.305-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.304-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.303-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.302-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.301-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.301-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.262-alt1
- 1.242 -> 1.262
- built for perl-5.16

* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.242-alt1
- 1.224 -> 1.242

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.224-alt3
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.224-alt2
- rebuilt as plain src.rpm

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.224-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.223-alt1.1
- rebuilt with perl 5.12

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 1.223-alt1
- 1.222 -> 1.223

* Fri Jul 17 2009 Alexey Tourbin <at@altlinux.ru> 1.222-alt1
- 1.221 -> 1.222

* Thu Apr 02 2009 Alexey Tourbin <at@altlinux.ru> 1.221-alt1
- 1.220 -> 1.221

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt1
- 1.200 -> 1.220

* Mon Sep 29 2008 Alexey Tourbin <at@altlinux.ru> 1.200-alt1
- 1.132 -> 1.200
- removed mdk-exception-trapping.patch

* Tue Aug 15 2006 Alexey Tourbin <at@altlinux.ru> 1.132-alt1
- 1.131 -> 1.132

* Wed Aug 02 2006 Alexey Tourbin <at@altlinux.ru> 1.131-alt1
- 1.120 -> 1.131

* Sat Mar 18 2006 LAKostis <lakostis@altlinux.ru> 1.120-alt1
- NMU.
- 1.101 -> 1.120
- update Buildreq.

* Thu Oct 06 2005 Alexey Tourbin <at@altlinux.ru> 1.101-alt1
- 1.093 -> 1.101

* Fri Sep 02 2005 Alexey Tourbin <at@altlinux.ru> 1.093-alt1
- 1.082 -> 1.093

* Thu Jun 23 2005 Alexey Tourbin <at@altlinux.ru> 1.082-alt1
- 1.081 -> 1.082
- license: LGPL, not GPL

* Thu Apr 14 2005 Alexey Tourbin <at@altlinux.ru> 1.081-alt1
- 1.080 -> 1.081
- alt-glib_version.patch: don't warn on glib_micro_version change

* Mon Mar 21 2005 Alexey Tourbin <at@altlinux.ru> 1.080-alt1
- 1.072 -> 1.080
- alt-Tester.patch merged upstream

* Fri Jan 14 2005 Alexey Tourbin <at@altlinux.ru> 1.072-alt1
- 1.071 -> 1.072
- new subpackage: %name-devel

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 1.071-alt1
- 1.061 -> 1.071
- fixed Test::More::eq_array() issue in t/c.t
- manual pages not packaged (use perldoc)

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 1.061-alt1
- 1.053 -> 1.061

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 1.053-alt1
- 1.042 -> 1.053

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.042-alt1
- 1.022 -> 1.042
- skip ExtUtils::MakeMaker dependency

* Wed Feb 18 2004 Alexey Tourbin <at@altlinux.ru> 1.022-alt1
- 1.022

* Wed Jan 14 2004 Alexey Tourbin <at@altlinux.ru> 1.020-alt1
- 1.020

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 1.012-alt1
- 1.012

* Tue Oct 14 2003 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 1.00

* Thu Aug 28 2003 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- initial revision; mdk-exception-trapping.patch applied
