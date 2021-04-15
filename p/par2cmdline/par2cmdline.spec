Group: Archiving/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: par2cmdline
Version: 0.8.1
Release: alt1_4
Summary: PAR 2.0 compatible file verification and repair tool

License: GPLv2+
URL: https://github.com/Parchive/par2cmdline/
Source0: https://github.com/Parchive/par2cmdline/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2
Source1: https://github.com/Parchive/par2cmdline/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2.sig
# GitHub releases are signed by GitHub user https://github.com/BlackIkeEagle
# which has verified his GitHub handle via his Keybase.io profile
# https://keybase.io/blackikeeagle.
Source2: https://keybase.io/blackikeeagle/pgp_keys.asc?fingerprint=db2277bcd500aa3825610bdddb323392796ca067#/gpg-db2277bcd500aa3825610bdddb323392796ca067.asc
# Fix tests to account for endianness correctly.
# Backport of https://github.com/Parchive/par2cmdline/commit/4f3576a314d7169912842ec9dc1e595e61e52653.
Patch0: 0001-Fix-for-Github-issue-143.-Test-did-not-account-for-e.patch

BuildRequires: gcc-c++
# Needed for source file verification.
BuildRequires: gnupg gnupg2
Source44: import.info
Conflicts: par2 < 0.5
Obsoletes: par2 < 0.5
Provides: par2 = %version


%description
par2cmdline is a program for creating and using PAR2 files to detect damage
in data files and repair them if necessary. PAR2 files are usually
published in binary newsgroups on Usenet; they apply the data-recovery
capability concepts of RAID-like systems to the posting and recovery of
multi-part archives.


%prep
%setup -q
%patch0 -p1


# Remove executable permission from text files
chmod -x ChangeLog configure.ac INSTALL Makefile.am NEWS stamp-h.in


%build
%configure
%make_build


%install
%makeinstall_std


%check
make check-TESTS


%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*


%changelog
* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt1_4
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_2
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_1
- update to new release by fcimport

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.4-alt1_1
- new version

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt2_6
- update to new release by fcimport

* Wed Sep 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt2_2
- to Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt1_2
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.14-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.tbb.20100203-alt1_17
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.tbb.20100203-alt1_11
- initial fc import

