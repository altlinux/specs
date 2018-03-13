# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# spec file for package asl
# 
# Copyright (c) 2006 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Spec file for Fedora modified by Eric Smith <brouhaha@fedoraproject.org>

%global patchlevel bld126

Name:           asl
URL:            http://john.ccac.rwth-aachen.de:8000/as/index.html
Version:        1.42
Release:        alt2_0.35.%{patchlevel}
Group:          Development/Other
License:        GPLv2+
Summary:        Macro Assembler AS
Source:         http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-%{patchlevel}.tar.bz2
Patch0:         asl-Makefile.def.patch
Patch1:         asl-sysdefs.h.patch
Patch2:         asl-install.sh.patch
Patch3:         asl-Makefile-DESTDIR.patch
BuildRequires:  tex(latex)
%if 0%{?fedora} > 18 || 0%{?rhel} > 6
BuildRequires:  tex(german.sty)
%endif
Source44: import.info


%description
AS is a portable macro cross-assembler for a variety of
microprocessors and controllers. Although it is mainly targeted at
embedded processors and single-board computers, CPU families that are
used in workstations and PCs in the target list.

%prep
# It's a shame that the directory name has 142 instead of 1.42, and Bld82
# instead of bld82. Makes use of variable substitution difficult.
# Also, sometimes the directory name is just "asl-current"
#%setup -q -n asl-142-Bld82
%setup -q -n asl-current

%patch0 -p0 -b .m-def
%patch1 -p0 -b .sysdefs
%patch2 -p1 -b .install
%patch3 -p1 -b .destdir

%build
# make seems to have problems with %{_smp_mflags}
make CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
# make docs isn't SMP-safe, so can't use %{_smp_mflags}
make docs

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

# convert doc files from ISO-8859-1 to UTF-8 encoding
for f in changelog doc/as-EN.txt doc/as-DE.txt
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done

%files
%{_bindir}/asl
%{_bindir}/alink
%{_bindir}/p2bin
%{_bindir}/p2hex
%{_bindir}/pbind
%{_bindir}/plist
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/include/
%{_datadir}/%{name}/lib/
%{_mandir}/man1/asl.1*
%{_mandir}/man1/p2bin.1*
%{_mandir}/man1/p2hex.1*
%{_mandir}/man1/pbind.1*
%{_mandir}/man1/plist.1*
%{_mandir}/man1/alink.1*
%doc --no-dereference COPYING
%doc README README.LANGS TODO BENCHES changelog
%doc doc/as-EN.html doc/as-EN.txt doc/as-EN.ps doc/as-EN.pdf doc/as-EN.dvi
%lang(de) %doc doc/as-DE.html doc/as-DE.txt doc/as-DE.ps doc/as-DE.pdf doc/as-DE.dvi

%changelog -n asl
* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.35.bld126
- fixed build

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.33.bld115
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.31.bld115
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.27.bld110
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.26.bld97
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.25.bld97
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.23.bld93
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.21.bld92
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.20.bld92
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.19.bld92
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.16.bld89
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.15.bld88
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.14.bld88
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.13.bld84
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.11.bld83
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2_0.10.bld82
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_0.10.bld82
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_0.9.bld81
- update to new release by fcimport

* Wed Nov 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_0.8.bld81
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1_0.5.bld77
- initial release by fcimport

