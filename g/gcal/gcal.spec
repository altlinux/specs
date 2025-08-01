Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/less /usr/bin/zdump texinfo
# END SourceDeps(oneline)
%define fedora 38
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 33

%global gcalmantag 4

Name:		gcal
Version:	4.1
Release:	alt3_%autorelease
Summary:	GNU Gregorian calendar program

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/gcal/
Source0:	https://ftp.gnu.org/gnu/gcal/%{name}-%{version}.tar.xz
# The man pages are not shipped in tarball but reside in the git repository
# at https://git.savannah.gnu.org/git/gcal.git
# To fetch the man pages from a clone of that repository, do:
# $ gcalmantag=4  # n.b. there is no 4.1 tag
# $ git archive --format=tar v${gcalmantag} -- doc/en/man | \
#     xz > gcal-man-v${gcalmantag}.tar.xz
Source1:	gcal-man-v%{gcalmantag}.tar.xz
Patch0:		gcal-glibc-no-libio.patch
Patch1:		gcal-configure-c99.patch
Patch2:		gcal-4.1-oob-write.patch
Patch3:		gcal-configure-tget.patch
BuildRequires:	gcc
BuildRequires:	gettext-tools libasprintf-devel
BuildRequires:	libncurses++-devel libncurses++w-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:	libunistring-devel
BuildRequires:	autoconf automake

# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)
Source44: import.info

%description
Gcal is a program for calculating and printing calendars.  Gcal
displays hybrid and proleptic Julian and Gregorian calendar sheets.
It also displays holiday lists for many countries around the globe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

tar xf %{SOURCE1}


%build
autoreconf -ifv
export LIBS=-lunistring
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
# Initialization of 'void (*)(void)' from incompatible pointer type
export CFLAGS="$CFLAGS -std=gnu17"
%endif
%configure --enable-unicode
%make_build


%check
make check


%install
%makeinstall_std
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 doc/en/man/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_datadir}/%{name}/Makefile.in
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc --no-dereference COPYING
%doc AUTHORS BUGS LIMITATIONS NEWS README THANKS
%{_bindir}/gcal
%{_bindir}/gcal2txt
%{_bindir}/tcal
%{_bindir}/txt2gcal
%{_datadir}/gcal/
%{_infodir}/*.info*
%{_mandir}/man1/*.1*

%changelog
* Fri Aug 01 2025 Igor Vlasenko <viy@altlinux.org> 4.1-alt3_33
- update to new release by fcimport

* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 4.1-alt3_28
- update to new release by fcimport

* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 4.1-alt3_24
- update to new release by fcimport

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 4.1-alt3_19
- fixed build

* Wed Oct 13 2021 Igor Vlasenko <viy@altlinux.org> 4.1-alt2_19
- fc update

* Wed Apr 22 2020 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.1-alt2_5
- Reverted previous change.

* Sun Apr 19 2020 Igor Vlasenko <viy@altlinux.ru> 4.1-alt2_4
- dropped perl(arybase.pm) autodependency

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 4-alt1_4
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 4-alt1_3
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2.1
- NMU: added BR: texinfo

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_4
- update to new release by fcimport

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_2
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt2_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_4
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_3
- new version

