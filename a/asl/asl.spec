# spec file for package asl
# 
# Copyright (c) 2006 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Spec file for Fedora modified by Eric Smith <eric@brouhaha.com>

%global patchlevel bld82

Name:           asl
URL:            http://john.ccac.rwth-aachen.de:8000/as/index.html
Version:        1.42
Release:        alt2_0.10.bld82
Group:          Development/Tools
License:        GPLv2+
Summary:        Macro Assembler AS
Source:         http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-%{patchlevel}.tar.bz2
Patch0:         asl-Makefile.def.patch
Patch1:         asl-sysdefs.h.patch
Patch2:         asl-install.sh.patch
Patch3:         asl-Makefile-DESTDIR.patch
BuildRequires:  /usr/bin/latex texlive-latex-recommended
Source44: import.info

%description
AS is a portable macro cross-assembler for a variety of
microprocessors and controllers. Although it is mainly targeted at
embedded processors and single-board computers, CPU families that are
used in workstations and PCs in the target list.

%prep
# It's a shame that the directory name has 142 instead of 1.42, and Bld82
# instead of bld82. Makes use of variable substitution difficult.
%setup -q -n asl-142-Bld82

%patch0 -p0 -b .m-def
%patch1 -p0 -b .sysdefs
%patch2 -p1 -b .install
%patch3 -p0 -b .destdir

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
%doc COPYING README README.LANGS TODO BENCHES changelog
%doc doc/as-EN.html doc/as-EN.txt doc/as-EN.ps doc/as-EN.pdf doc/as-EN.dvi
%lang(de) %doc doc/as-DE.html doc/as-DE.txt doc/as-DE.ps doc/as-DE.pdf doc/as-DE.dvi

%changelog -n asl
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

