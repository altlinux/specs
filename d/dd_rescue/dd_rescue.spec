%define _unpackaged_files_terminate_build 1

%define rhelp_version 0.3.0

Name:           dd_rescue
Version:        1.99.13
Release:        alt1
Summary:        Fault tolerant "dd" utility for rescuing data from bad media
Group:          File tools
License:        GPL+
URL:            http://www.garloff.de/kurt/linux/ddrescue/

Source:         %name-%version.tar
# http://www.kalysto.org/pkg/dd_rhelp-%{rhelp_version}.tar.gz
Source1:        dd_rhelp-%{rhelp_version}.tar

Patch1: dd_rescue-%version-alt.patch

BuildRequires: autoconf
BuildRequires: libacl-devel libattr-devel

%description
ddrescue is a utility similar to the system utility "dd" which copies
data from a file or block device to another. ddrescue does however
not abort on errors in the input file. This makes it suitable for
rescuing data from media with errors, e.g. a disk with bad sectors.

This package includes dd_rhelp, a wrapper script facilitating data 
recovery.

%prep
%setup
%setup -a 1 -D -T
%patch1 -p1
%ifarch %e2k
# The combination of the laziness of the author of the makefile and
# the desire of the compiler for Elbrus to throw errors for any reason
# leads to an error, since the makefile tries to build dependencies
# for every source file, including those that don't have the required
# includes and will not compile.
sed -i 's/$(CC) $(CFLAGS) -DGEN_DEP/echo >.dep #/' Makefile
%endif

%build
%make RPM_OPT_FLAGS="%{optflags}" %{?_smp_mflags} LIB=%_lib LIBDIR=%{_libdir}
cp -p README.dd_rescue README
cp -p dd_rhelp-%{rhelp_version}/README README.dd_rhelp
cp -p dd_rhelp-%{rhelp_version}/FAQ FAQ.dd_rhelp

%install
%makeinstall_std INSTALLDIR=%{buildroot}/%{_bindir} INSTASROOT="" INSTALLFLAGS="" LIB=%_lib LIBDIR=%{_libdir}
install -D -m 755 dd_rhelp-%{rhelp_version}/dd_rhelp %{buildroot}%{_bindir}/dd_rhelp

%files
%doc COPYING README README.dd_rhelp FAQ.dd_rhelp
%_bindir/dd_rescue
%_bindir/dd_rhelp
%_libdir/libddr_MD5.so
%_libdir/libddr_crypt.so
%_libdir/libddr_hash.so
%_libdir/libddr_null.so
%_man1dir/%{name}.*
%_man1dir/ddr_crypt.1*
%_man1dir/ddr_lzo.1*

%changelog
* Wed Jul 10 2024 Anton Farygin <rider@altlinux.ru> 1.99.13-alt1
- 1.99.10 -> 1.99.13

* Sat Jan 08 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.99.10-alt1.1
- Fixed build for Elbrus.

* Thu Mar 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.99.10-alt1
- Updated to upstream version 1.99.10.

* Mon May 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.99.8-alt2
- Fixed build for aarch64.

* Fri May 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.99.8-alt1
- Updated to upstream version 1.99.8.

* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.42.1-alt2_3
- moved to sisyphus for rescue iso

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.42.1-alt1_3
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_2
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1_1
- update to new release by fcimport

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1_1
- update to new release by fcimport

* Fri Dec 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_2
- converted for ALT Linux by srpmconvert tools

