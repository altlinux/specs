Summary: A Z80 cross compiler
Name: z88dk
Version: 1.9
Release: alt2_4
License: Artistic clarified
Group: Development/Tools
Source: http://downloads.sourceforge.net/z88dk/z88dk-src-%{version}.tgz
Patch0: z88dk-1.8-makefile-usr-share.patch
Patch1: z88dk-1.8-makefile-fixes.patch
Patch2: z88dk-1.9-64bit.patch
Patch3: z88dk-1.8-getline-name-conflict.patch
URL: http://z88dk.sourceforge.net/
Source44: import.info

%description
z88dk is a Z80 cross compiler capable of generating binary files for a variety
of Z80 based machines (such as the ZX81, Spectrum, Jupiter Ace and some TI
calculators).

%prep
%setup -q -n z88dk
# Put files in %{_datadir}/z88dk rather than /usr/lib/z88dk
# Also support DESTDIR in install-libs
%patch0 -p1
# Lots of buggy makefiles there
%patch1 -p1
# 64-bit fixes
%patch2 -p1
# Fix name conflict with the getline function in POSIX 2008
%patch3 -p1
%{_bindir}/find . -depth -name CVS -type d -exec %{__rm} -rf {} \;
# Separate manpages from other docs and fix their permissions
%{__mv} doc/netman .
%{__chmod} 644 netman/man3z/*
# Fix files with wrong line endings and bad permissions
/usr/bin/find doc examples src -type f -exec %{__sed} -i -e 's/\r*$//' {} \;
/usr/bin/find doc examples src -type f -exec %{__chmod} 644 {} \;

%build
export Z80_OZFILES=%{_builddir}/z88dk/lib/
export ZCCCFG=%{_builddir}/z88dk/lib/config/
export PATH=%{_builddir}/z88dk/bin:$PATH
export CC=gcc
export CFLAGS="%{optflags}"
# Note: do not use %{?_smp_mflags} with make because the Makefiles don't support parallel builds
%{__make} clean
%{__make} -e
# libs are target libraries, they won't build with host CFLAGS
unset CFLAGS
export CFLAGS
%{__make} -e libs

%install
export Z80_OZFILES=%{_datadir}/z88dk-%{version}/lib/
export ZCCCFG=%{_datadir}/z88dk-%{version}/lib/config/
%{__mkdir} %{buildroot}
%{__make} install install-libs DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}%{_mandir}/man3z
%{__cp} -p netman/man3z/* %{buildroot}%{_mandir}/man3z

%files
%doc doc/*.html doc/*.gif doc/copt.man
%doc doc/compile.txt doc/cpc.txt doc/embedded.txt doc/error.txt doc/farmods.txt
%doc doc/fileio.txt doc/lib3d.txt doc/options.txt doc/packages.txt
%doc doc/platforms.txt doc/retarget.txt doc/stdio.txt doc/ti.txt doc/z80asm.txt
%doc doc/zxscrdrv.txt
%doc EXTENSIONS LICENSE
# Examples might be worth putting in subpackage
%doc examples
%{_bindir}/appmake
%{_bindir}/copt
%{_bindir}/sccz80
%{_bindir}/z*
%{_datadir}/z88dk/
%{_mandir}/man3z/

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_4
- update to new release by fcimport

* Sun Jul 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3
- initial release by fcimport

