# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
#global prever r821

Name:           grfcodec
Version:        6.0.0
Release:        alt2_1
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:          Development/Tools
License:        GPLv2+
URL:            http://dev.openttdcoop.org/projects/grfcodec
Source0:        http://binaries.openttd.org/extra/grfcodec/%{version}/grfcodec-%{version}-source.tar.gz
#Source0:        http://binaries.openttd.org/extra/grfcodec-nightly/%{prever}/grfcodec-nightly-%{prever}-source.tar.gz

BuildRequires:  boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel libpng-devel
Obsoletes:      nforenum < 4.0.0-2
Provides:       nforenum = 4.0.0-2
Source44: import.info


%description
A suite of programs to modify Transport Tycoon Deluxe's GRF files.


%prep
%setup -q


%build
cat << EOF >> Makefile.local
STRIP=true
V=1
CXXFLAGS=%{optflags}
prefix=%{_prefix}
DO_NOT_INSTALL_DOCS=1
DO_NOT_INSTALL_CHANGELOG=1
DO_NOT_INSTALL_LICENSE=1
EOF

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc changelog.txt COPYING
%doc docs/*.txt
%{_bindir}/grf*
%{_bindir}/nforenum
%{_mandir}/man1/grf*.1.*
%{_mandir}/man1/nforenum.1.*


%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt2_1
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_3
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_2
- update to new release by fcimport

* Wed Oct 26 2011 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_1
- update to new release by fcimport

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_1
- initial release by fcimport

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 0.9.10-alt1
- first build for Sisyphus, based on specfile from Fedora
