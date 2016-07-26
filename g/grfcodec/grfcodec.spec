# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
#global prever r821

Name:           grfcodec
Version:        6.0.6
Release:        alt1_1
Summary:        A suite of programs to modify Transport Tycoon Deluxe's GRF files
Group:          Development/Tools
License:        GPLv2+
URL:            http://dev.openttdcoop.org/projects/grfcodec
Source0:        http://binaries.openttd.org/extra/grfcodec/%{version}/grfcodec-%{version}-source.tar.xz
#Source0:        http://binaries.openttd.org/extra/grfcodec-nightly/%{prever}/grfcodec-nightly-%{prever}-source.tar.xz

BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel libpng-devel
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
%{_mandir}/man1/grf*.1*
%{_mandir}/man1/nforenum.1*


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.6-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 6.0.5-alt1_5
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 6.0.4-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 6.0.4-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 6.0.4-alt1_3
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 6.0.4-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 6.0.4-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 6.0.3-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_2
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_2
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt1_1
- update to new release by fcimport

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt2_2.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt2_2
- update to new release by fcimport

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
