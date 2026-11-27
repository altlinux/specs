%define _unpackaged_files_terminate_build 1
%define soname 0

Summary: Thai language support routines
Name: libthai
Version: 0.1.30

Release: alt1
Group: System/Libraries
License: LGPL-2.1-or-later

Url: http://linux.thai.net
Vcs: https://github.com/tlwg/libthai

Source: %name-%version.tar.xz
#http://linux.thai.net/pub/thailinux/software/libthai/libthai-%version.tar.xz
Patch0: libthai-0.1.9-multilib.patch

BuildRequires: gcc
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: doxygen

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package devel
Group: Development/Other
Summary: Thai language support routines
Requires: pkgconfig
%description devel
The libthai-devel package includes the header files and developer docs
for the libthai package.
Install libthai-devel if you want to develop programs which will use
libthai.

%package common
Group: System/Configuration/Other
BuildArch: noarch
Obsoletes: libthai <= 0.1.29-alt1_6
Summary: Data files for %name
%description common
This package contains data files for %name.

%package -n %name%soname
Group: System/Libraries
Obsoletes: libthai <= 0.1.29-alt1_6
Summary: %name library
Requires: %name-common
%description -n %name%soname
%name library.

%prep
%setup
%patch0 -p1
sed -i 's/@VERSION@/%version/g' libthai.pc.in 

%build
%autoreconf
%configure --disable-static
make

%install
%makeinstall

# move installed doc files back to build directory to package them
# in the right place
mkdir installed-docs
mv $RPM_BUILD_ROOT%_docdir/libthai/* installed-docs
rmdir $RPM_BUILD_ROOT%_docdir/libthai

rm $RPM_BUILD_ROOT%_libdir/*.la

%files common
%doc README AUTHORS COPYING ChangeLog
%_datadir/libthai

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%files devel
%doc installed-docs/*
%_includedir/thai
%_libdir/%name.so
%_libdir/pkgconfig/*

%changelog
* Fri Nov 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.30-alt1
- 0.1.29 -> 0.1.30
- added Vcs
- builded in accordance with SharedLibsPolicy

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.1.29-alt1_6
- update to new release by fcimport

* Sun Jan 02 2022 Igor Vlasenko <viy@altlinux.org> 0.1.29-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.28-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.27-alt1_2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.25-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.25-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.25-alt1_1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.24-alt1_1
- update to new release by fcimport

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.21-alt1_1
- new version (closes: #30252)

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.19-alt1_2
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt3_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt3_6
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt3_5
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt1_4
- initial import by fcimport

