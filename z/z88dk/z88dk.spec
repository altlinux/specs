Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires: perl(File/Slurp.pm) perl(List/AllUtils.pm) perl(Modern/Perl.pm) perl(Test/Differences.pm)
# END SourceDeps(oneline)
Name: z88dk
Version: 1.10.1
Release: alt1_1
Summary: A Z80 cross compiler
License: Artistic clarified
URL: http://www.z88dk.org/
Source: http://downloads.sourceforge.net/z88dk/z88dk-%{version}.tgz
Patch0: z88dk-1.10-makefile-usr-share.patch
Patch1: z88dk-1.10-64bit.patch
Source44: import.info

%description
z88dk is a Z80 cross compiler capable of generating binary files for a variety
of Z80 based machines (such as the ZX81, Spectrum, Jupiter Ace and some TI
calculators).

%prep
%setup -q -n z88dk
# Put files in %%{_datadir}/z88dk rather than /usr/lib/z88dk
# Also support DESTDIR in install-libs
%patch0 -p1
# 64-bit fixes
%patch1 -p1
find . -depth -name CVS -type d -exec rm -rf {} \;
# Separate manpages from other docs and fix their permissions
mv doc/netman .
chmod 644 netman/man3z/*
# Fix files with wrong line endings and bad permissions
find doc examples src -type f -exec sed -i -e 's/\r*$//' {} \;
find doc examples src -type f -exec chmod 644 {} \;

%build
export Z80_OZFILES=%{_builddir}/z88dk/lib/
export ZCCCFG=%{_builddir}/z88dk/lib/config/
export PATH=%{_builddir}/z88dk/bin:$PATH
export CC=gcc
export CFLAGS="%{optflags}"
%{?__global_ldflags:export LDFLAGS="%{__global_ldflags}"}
# Note: do not use %%{?_smp_mflags} with make because the Makefiles don't support parallel builds
make clean
make -e
# libs are target libraries, they won't build with host CFLAGS/LDFLAGS
unset CFLAGS
export CFLAGS
unset LDFLAGS
export LDFLAGS
make -e libs

%install
export Z80_OZFILES=%{_datadir}/z88dk-%{version}/lib/
export ZCCCFG=%{_datadir}/z88dk-%{version}/lib/config/
make install install-libs DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man3z
cp -p netman/man3z/* %{buildroot}%{_mandir}/man3z

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
* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.10.1-alt1_1
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_5
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_4
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_4
- update to new release by fcimport

* Sun Jul 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3
- initial release by fcimport

