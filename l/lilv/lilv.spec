Name: lilv
Version: 0.24.24
Release: alt2

Summary: An LV2 Resource Description Framework Library
License: 0BSD
Group: Sound
Url: https://github.com/lv2/lilv

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ meson rpm-build-python3
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sord-0)
BuildRequires: pkgconfig(sratom-0)
BuildRequires: pkgconfig(zix-0)

%package -n liblilv
Summary: lilv shared libraries
Group: System/Libraries

%package -n liblilv-devel
Summary: Development libraries and headers for lilv
Group: Development/C
Provides: lilv-devel = %EVR
Obsoletes: lilv-devel

%package -n python3-module-lilv
Summary: Python bindings for lilv
Group: Development/Python3
Requires: liblilv == %EVR
BuildArch: noarch

%description
lilv is a library to make the use of LV2 plugins as simple as possible
for applications. Lilv is the successor to SLV2, rewritten to be significantly
faster and have minimal dependencies.

%description -n liblilv
lilv is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.
This package contains the libraries for lilv.

%description -n liblilv-devel
lilv is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.
This package contains the headers and development libraries for lilv.

%description -n python3-module-lilv
lilv is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.
This package contains the python bindings for lilv.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/lv2*
%_datadir/bash-completion/completions/lilv
%_man1dir/lv2*.1*

%files -n liblilv
%doc AUTHORS NEWS README.md
%_libdir/liblilv-0.so.*

%files -n liblilv-devel
%_libdir/liblilv-0.so
%_pkgconfigdir/lilv-0.pc
%_includedir/lilv-0

%files -n python3-module-lilv
%python3_sitelibdir_noarch/lilv.*
%python3_sitelibdir_noarch/*/lilv.*

%changelog
* Tue Feb 27 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24.24-alt2
- fix devel subpackage naming (closes: 49521)

* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24.24-alt1
- 0.24.24 released

* Thu Feb 24 2022 Igor Vlasenko <viy@altlinux.org> 0.24.12-alt1_3
- new version

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.24.10-alt1_3.1
- NMU: fix libnumpy-devel BR

* Wed Jun 30 2021 Igor Vlasenko <viy@altlinux.org> 0.24.10-alt1_3
- FTBFS quick fix (closes: #40334)

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.24.10-alt1_1
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.24.6-alt1_2
- update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_7
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_5
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.24.4-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.2-alt2_7
- update to new release by fcimport

* Tue Jan 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.2-alt2_4
- Updated build dependencies.

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.24.2-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_7
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_6
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20.0-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_3
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt1_2
- converted for ALT Linux by srpmconvert tools

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.14.4-alt1_2
- fc import

