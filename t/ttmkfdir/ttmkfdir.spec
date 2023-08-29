Group: System/Base
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Utility to create fonts.scale files for truetype fonts
Name: ttmkfdir
Version: 3.0.9
Release: alt3_69
# Only licensing attribution is in README, no version.
License: LGPL-2.0-or-later
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
Patch10:ttmkfdir-3.0.9-freetype-header-fix2.patch
Patch11:ttmkfdir-3.0.9-fedora-ldflags.patch
Patch12:ttmkfdir-3.0.9-tag.patch
Source10: ttmkfdir.1

BuildRequires: libfreetype-devel >= 2.0
BuildRequires: flex libtool
BuildRequires: bzlib-devel
BuildRequires: zlib-devel
BuildRequires: gcc-c++
Source44: import.info
Url: http://freecode.com/projects/ttmkfdir

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1


%build
%{make_build} OPTFLAGS="$RPM_OPT_FLAGS" RPM_LD_FLAGS="$RPM_LD_FLAGS -pie"

%install
%{makeinstall_std} PREFIX="%{_prefix}"
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE10} %{buildroot}%{_mandir}/man1/

%files
%doc README
%{_bindir}/ttmkfdir
%{_mandir}/man1/ttmkfdir.1*

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 3.0.9-alt3_69
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 3.0.9-alt3_64
- fc update

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt3_59
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt3_58
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt3_54
- update to new release by fcimport

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt3_53
- NMU: added URL

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt2_53
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt2_51
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt2_48
- update to new release by fcimport

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

