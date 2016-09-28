# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Summary:        PAR 2.0 compatible file verification and repair tool
Name:           par2cmdline
Version:        0.6.14
Release:        alt2_2
License:        GPLv2+
Group:          Archiving/Other
URL:            http://parchive.sourceforge.net/

Source:         https://github.com/Parchive/par2cmdline/archive/v%{version}.tar.gz

# Backport of OpenMP support from https://github.com/jkansanen/par2cmdline-mt
# Also see https://github.com/Parchive/par2cmdline/issues/27
Patch0:         par2cmdline-openmp-support.patch

# One of the testcases uses /dev/random
# The koji builders may not have enough entropy
# available so use the /dev/urandom device instead
Patch1:         par2cmdline-use-urandom-in-tests.patch

Obsoletes:      parchive <= 1.1.4
Provides:       parchive = 1.1.4.0.par2.%{version}

BuildRequires:  autoconf automake libtool
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
%setup -q -n par2cmdline-%{version}
%patch0 -p1
autoreconf -i --force

%patch1 -p1

# fix end-of-lines of several files
sed -i 's/\r//' AUTHORS PORTING README ROADMAP


%build
%configure
make %{_smp_mflags}
chmod 644 ChangeLog galois.h par1repairer.cpp par2repairer.cpp par2repairersourcefile.cpp par2repairersourcefile.h


%install
make install DESTDIR=$RPM_BUILD_ROOT


%check
make check-TESTS


%files
%doc AUTHORS COPYING ChangeLog README 
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*


%changelog
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

