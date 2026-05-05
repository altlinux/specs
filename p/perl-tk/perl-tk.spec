%define        _unpackaged_files_terminate_build 1
%define        dist tk
%def_with      xft

Name:          perl-%dist
Version:       804.036.28
Release:       alt0.3
Summary:       Perl modules providing the Tk graphics library
License:       Artistic-1.0 or GPL-2.0-or-later
Group:         Development/Perl
Url:           %CPAN %dist
Vcs:           https://github.com/eserte/perl-tk.git

Source:        %name-%version.tar
BuildRequires: perl-devel >= 5.38.4-alt2
BuildRequires: libXft-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: perl-Devel-Leak
BuildRequires: perl-Encode
BuildRequires: imake
BuildRequires: xprop
BuildRequires: xvfb-run
BuildRequires: libXcursor
BuildRequires: fonts-ttf-dejavu
BuildRequires: fonts-type1-urw
Provides:      cpan(tk) = %version

Provides:      perl-Tk = %EVR
Provides:      perl-Tk-JPEG = %EVR
Obsoletes:     perl-Tk < %EVR
Obsoletes:     perl-Tk-JPEG < %EVR
# provides for demos are useless
%add_findprov_skiplist %perl_vendor_archlib/Tk/demos/*/*.pl
%add_findreq_skiplist %perl_vendor_archlib/Tk/demos/widget_lib/*.pl
%add_findreq_skiplist %perl_vendor_archlib/Tk/demos/widtrib/*.pl

# fix for deparse failure
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -MTk'
%define _perl_lib_path %perl_vendor_archlib/Tk/demos/widget_lib

%description
This is a set of Perl modules which provide access to the Tk library,
a Graphical User Interface ToolKit.


%package       demos
Summary:       Perl modules providing the Tk graphics library
Group:         Development/Perl
Requires:      %name = %EVR

%description   demos
This is a set of Perl modules which provide access to the Tk library,
a Graphical User Interface ToolKit.


%package       devel
Summary:       Perl modules providing the Tk graphics library
License:       TCL and Artistic-1.0 or GPL-2.0-or-later
Group:         Development/Perl
Requires:      %name = %EVR
Provides:      cpan{tk} = %version
Provides:      perl-Tk-devel = %EVR
Obsoletes:     perl-Tk-devel < %EVR

%description   devel
This is a set of Perl modules which provide access to the Tk library,
a Graphical User Interface ToolKit.


%prep
%setup -q
rm -r PNG/zlib/ PNG/libpng/

# font-dependent tests, see README
rm t/entry.t t/listbox.t

%ifdef __buildreqs
rm t/dirtree.t
%endif

# XXX fails under Xvfb in hasher
rm t/fileevent2.t

cd pTk
for f in license.*; do
mv "$f" "Tk.$f"
done
cd -

%build
%perl_vendor_build %{?_with_xft:XFT=1} X11LIB=%_x11libdir

%install
%perl_vendor_install

%check
xvfb-run -a make test


%files
%doc README README.linux Funcs.doc ToDo Changes README-ActiveState.txt README-Strawberry.txt README.AIX README.HPUX README.IRIX README.OSF README.OpenBSD README.SCO README.SVR4 README.Solaris README.cygwin README.darwin README.os2 README.ultrix examples
	%_bindir/ptked
	%_bindir/ptksh
	%_bindir/tkjpeg
	%perl_vendor_archlib/Tie*
	%perl_vendor_archlib/Tk*
	%perl_vendor_autolib/Tk*
%exclude %perl_vendor_archlib/Tk/demos
%exclude %perl_vendor_archlib/Tk/pTk*
%exclude %perl_vendor_archlib/Tk/*.def
%exclude %perl_vendor_archlib/Tk/*.[hmt]
%exclude %perl_vendor_archlib/Tk/typemap
%exclude %perl_vendor_archlib/Tk/MakeDepend.pm
%exclude %perl_vendor_archlib/Tk/MMutil.pm

%files devel
%doc README README.linux pTk/*license*
%dir	%perl_vendor_archlib/Tk
	%perl_vendor_archlib/Tk/pTk*
	%perl_vendor_archlib/Tk/*.def
	%perl_vendor_archlib/Tk/*.[hmt]
	%perl_vendor_archlib/Tk/typemap
	%perl_vendor_archlib/Tk/MakeDepend.pm
	%perl_vendor_archlib/Tk/MMutil.pm

%files demos
%doc	demos/README
	%_bindir/gedi
	%_bindir/widget
%dir	%perl_vendor_archlib/Tk
%dir	%perl_vendor_archlib/Tk/demos
	%perl_vendor_archlib/Tk/demos/*.pm
	%perl_vendor_archlib/Tk/demos/images/
	%perl_vendor_archlib/Tk/demos/widget_lib/
	%perl_vendor_archlib/Tk/demos/widtrib/


%changelog
* Sun May 03 2026 Pavel Skrylev <majioa@altlinux.org> 804.036.28-alt0.3
- !FTBFS fixed old style functionn def and invalid pointer

* Mon Sep 15 2025 Pavel Skrylev <majioa@altlinux.org> 804.036.28-alt0.2
- ! fixed provides/obsolete deps for packages

* Fri Aug 29 2025 Pavel Skrylev <majioa@altlinux.org> 804.036.28-alt0.1
- ^ 804.036 -> 804.036p27
- ! fixed incompatible pointer type compilation error along with others
    (may be) for gcc14

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 804.036-alt1
- new version

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 804.035-alt1
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 804.034-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 804.034-alt1.1
- rebuild with new perl 5.26.1

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 804.034-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 804.033-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 804.033-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 804.033-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 804.032-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 804.032-alt1
- new version 804.032

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 804.031-alt1
- 804.030 -> 804.031
- Fixed build of Tk::PNG (patch from RT#86988)

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 804.030-alt1
- 804.029_500 -> 804.030
- built for perl-5.16
- fixed build

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 804.029_500-alt2
- rebuilt for perl-5.14

* Wed Sep 21 2011 Alexey Tourbin <at@altlinux.ru> 804.029_500-alt1
- 804.029 -> 804.029_500

* Tue Dec 07 2010 Vladimir Lettiev <crux@altlinux.ru> 804.029-alt2
- Fixed build failure with libX11-1.4.0, patch from gentoo
  http://bugs.gentoo.org/show_bug.cgi?id=345987

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 804.029-alt1.1
- rebuilt with perl 5.12

* Wed Jun 09 2010 Alexey Tourbin <at@altlinux.ru> 804.029-alt1
- 804.028_501 -> 804.029

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 804.028_501-alt1.1
- disabled t/fileevent2.t test which fails under Xvfb

* Sat Mar 07 2009 Alexey Tourbin <at@altlinux.ru> 804.028_501-alt1
- 804.028 -> 804.028_501

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 804.028-alt2
- merged two fixes from https://svn.perl.org/modules/Tk
  + fixed a buffer overflow in tkImgGIF.c (CVE-2006-4484)
  + fixed event handling for newer X servers (cpan#38745)
- applied perl-Tk-seg.patch from Fedora (RH#235666, RH#431330)
- disabled t/unicode.t test which fails under Xvfb

* Thu Dec 27 2007 Alexey Tourbin <at@altlinux.ru> 804.028-alt1
- 804.027_500 -> 804.028
- changed src.rpm packaging to keep separate upstream tarball

* Sat Apr 07 2007 Alexey Tourbin <at@altlinux.ru> 804.027.500-alt1
- 804.027 -> 804.027_500
- added '--without xft' switch to specfile (#4951)

* Mon Jan 15 2007 Alexey Tourbin <at@altlinux.ru> 804.027-alt5
- imported into git and adapted for gear
- merged in debian changes from perl-tk_804.027-7.diff.gz
- fixed perl syntax ($#{@$aref} is bad, $#$aref is valid)
- All men are mortal.  Nick Ing-Simmons, the Perl/Tk author,
  died of a heart attack on Monday September 25th 2006.
  http://news.perlfoundation.org/2006/09/thanks_nick.html

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 804.027-alt4
- disabled -Werror build mode
- anicka@suse: workaround segfault in tkEvent.c
- fixed segv in test by running fc-list (cpan #14355)

* Mon May 23 2005 Alexey Tourbin <at@altlinux.ru> 804.027-alt3
- fixed perl syntax in demos

* Sat Mar 12 2005 Alexey Tourbin <at@altlinux.ru> 804.027-alt2
- subpackages: devel, demos
- manual pages not packaged (use perldoc)
- always run tests (by utilizing xvfb-run)
- disabled -Werror mode for x86_64
- fixed gcc-3.4 warnings

* Sun Jun 20 2004 Alexey Tourbin <at@altlinux.ru> 804.027-alt1
- 804.025_beta12 -> 804.027
- alt-syntax.patch dropped because of recent rpm-build-perl enhancements
- enabled XFT support
- test status:
  + JP.t and KR.t skipped because of locale settings
  + entry.t and listbox.t disabled because of XFT font metrics
  + all other tests pass so far

* Mon Dec 22 2003 Alexey Tourbin <at@altlinux.ru> 804.025-alt4
- 804.025_beta12; status: 1/2567 subtests failed, 99.96%% okay
- findprov_skiplist: demos/*/*.pl

* Tue Nov 18 2003 Alexey Tourbin <at@altlinux.ru> 804.025-alt3
- 804.025_beta6; status: 1/2537 subtests failed, 99.96%% okay
- remove zlib and libpng included at %%prep stage

* Thu Oct 23 2003 Alexey Tourbin <at@altlinux.ru> 804.025-alt2
- 804.025_beta3; status: 7/2541 subtests failed, 99.72%% okay
- build with -Werror by default
- alt-syntax.patch updated
- ignore MMutil.pm dependency on MakeMaker

* Wed Oct 01 2003 Alexey Tourbin <at@altlinux.ru> 804.025-alt1
- 804.025 (Sep 27 snapshot)
- Provides, Obsoletes: perl-Tk-JPEG
- Sisyphus release (8/2541 subtests failed, 99.69%% okay)

* Sat Jul 26 2003 Alexey Tourbin <at@altlinux.ru> 804.024-alt1.pl0.1
- moved to 804 branch with unicode support (804.024.patches-0.1)
- general specfile revision/cleanup; License tag corrected
- Daedalus release (2/30 test fail)

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 800.024-alt2
- rebuild with new perl

* Mon Mar 25 2002 Grigory Milev <week@altlinux.ru> 800.024-alt1
- new version release (bug fixes)
- fix build requires
- spec cleanup (optimize perl regexp)

* Thu Mar 21 2002 Mikhail Zabaluev <mhz@altlinux.ru> 800.023-alt2
- Fixed an insanely long perlfix script
- Corrected license information and files
- Compressed Change.log
- Minor fixes in build scripts and file lists

* Tue Jul 17 2001 Grigory Milev <week@altlinux.ru> 800.023-alt1
- First build for Sisyphus
