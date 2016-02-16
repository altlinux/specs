# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Summary: Utility to create fonts.scale files for truetype fonts
Name: ttmkfdir
Version: 3.0.9
Release: alt2_46
# Only licensing attribution is in README, no version.
License: LGPLv2+
Group: File tools
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: %{name}-%{version}.tar.bz2
Patch: ttmkfdir-3.0.9-cpp.patch
Patch1: ttmkfdir-3.0.9-zlib.patch
Patch2: ttmkfdir-3.0.9-fix-freetype217.patch
Patch3: ttmkfdir-3.0.9-namespace.patch
Patch4: ttmkfdir-3.0.9-fix-crash.patch
Patch5: ttmkfdir-3.0.9-warnings.patch
Patch6: ttmkfdir-3.0.9-segfaults.patch
Patch7: ttmkfdir-3.0.9-encoding-dir.patch
Patch8: ttmkfdir-3.0.9-font-scale.patch
Patch9: ttmkfdir-3.0.9-bug434301.patch
Patch10:ttmkfdir-3.0.9-freetype-header-fix.patch
Source10: ttmkfdir.1

BuildRequires: libfreetype-devel >= 2.0
BuildRequires: flex libtool
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
Source44: import.info
Patch33: ttmkfdir-3.0.9-alt-Makefile-tag-cxx.patch

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#patch10 -p1
%patch33 -p0


%build
make %{?_smp_mflags} OPTFLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE10} %{buildroot}%{_mandir}/man1/

%files
%doc README
%{_bindir}/ttmkfdir
%{_mandir}/man1/ttmkfdir.1*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt2_46
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_46
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_44
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_42
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_41
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_40
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_39
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_38
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_37
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_36
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_35
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_34
- update to new release by fcimport

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_33
- release by fcimport; long live mkfontscale, but let a thousand flowers bloom

