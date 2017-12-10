%define _unpackaged_files_terminate_build 1
Name: perl-Wx
Version: 0.9932
Release: alt2

Summary: wxPerl - Perl bindings for wxWindows
License: GPL
Group: Development/Perl

URL: http://wxperl.sourceforge.net/
Source0: http://www.cpan.org/authors/id/M/MD/MDOOTSON/Wx-%{version}.tar.gz
# Work around BOM_UTF8 clash between wxGTK and Perl. Should be fixed in newer
# wxGTK, CPAN RT#121464, <http://trac.wxwidgets.org/ticket/13599>.
Patch0:         Wx-0.9932-Undefine-BOM_UTF8.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: gcc-c++ libwxGTK-contrib-stc-devel libwxGTK-devel perl-Alien-wxWidgets perl-Encode perl-ExtUtils-CBuilder perl-ExtUtils-XSpp perl-IO-String perl-autodie perl-threads xvfb-run

%description
wxPerl is a Perl module wrapping the awesome wxWindows library
for cross-platform GUI developement.

%package devel
Summary: Wx Perl development files
Group: Development/Perl
Requires: %name = %version-%release

%description devel
Development files useful for building Perl applications depending on Wx.

%prep
%setup -q -n Wx-%{version}
%patch0 -p1

%ifdef __buildreqs
# these tests open /usr/share/applications/*.desktop
rm t/08_ovl_func.t
rm ext/filesys/t/03_threads.t
%endif

%ifndef _build_display
%def_without test
%endif

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

# need DISPLAY for perl.req
%{expand:%%global __find_requires xvfb-run -a %__find_requires}

%files
%doc README.txt wxpl.ico wxpl.xpm Changes docs
%perl_vendor_archlib/Wx*
%perl_vendor_autolib/Wx
%exclude %perl_vendor_archlib/Wx/Overload
%exclude %perl_vendor_archlib/Wx/build
%exclude %perl_vendor_archlib/Wx/cpp
%exclude %perl_vendor_archlib/Wx/typemap

%files devel
%doc Changes samples
%_bindir/wx*
%_man1dir/wxperl_overload.*
%dir %perl_vendor_archlib/Wx
%perl_vendor_archlib/Wx/Overload
%perl_vendor_archlib/Wx/build
%perl_vendor_archlib/Wx/cpp
%perl_vendor_archlib/Wx/typemap

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.9932-alt2
- added patch for perl 5.26

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.9932-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.9928-alt1.1
- rebuild with new perl 5.24.1

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.9928-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.9927-alt2.1
- rebuild with new perl 5.22.0

* Sun Nov 01 2015 Vladimir Lettiev <crux@altlinux.ru> 0.9927-alt2
- added man(1) for wxperl_overload

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.9927-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.9923-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.9923-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.9922-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.9922-alt1
- automated CPAN update

* Thu Oct 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.9914-alt1
- 0.9913 -> 0.9914

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.9913-alt1
- 0.9911 -> 0.9913
- built as plain srpm

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.9911-alt1
- 0.9902 -> 0.9911
- built for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9902-alt1
- 0.9901 -> 0.9902
- built for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.9901-alt1
- automated CPAN update
- manually dropped ExtUtils-ParseXS hack due to new perl.

* Mon Feb 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.98-alt1
- 0.98
- used bundled ExtUtils::ParseXS = 2.2206 to hackaround old
  ExtUtils::ParseXS inside perl-devel
- optimised dependencies by buildreq
- dropped noop patch
- relaxed _perl_req_method

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt1.1
- rebuilt with perl 5.12
- fixed build

* Fri Jan 29 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.96-alt1
- 0.96
- Fix bug (ALT #22841)

* Thu Dec 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.89-alt1
- 0.89

* Fri Sep 12 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.86-alt1
- 0.86

* Fri Mar 14 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.81-alt1
- 0.81

* Tue Nov 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.80-alt1
- 0.80
- Add perl-Wx-open.patch
- Remove perl-Wx-0.26-alt-SetConstants.patch
- Split "devel" subpackage
- Update spec and BuildRequires
- Switch off tests (not work xvfb-run)

* Wed Jun 21 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.26-alt0
- 0.26
- Update spec

* Sat May 13 2006 Valentyn Solomko <val@pere.org.ua> 0.2.0.060513
- First build for ALTLinux.
