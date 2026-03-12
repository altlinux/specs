%define oname py2pack

Name:       py2pack
Version:    0.9.1
Release:    alt1

Summary:    Generate distribution packages from Python packages on PyPI
License:    GPL-2.0+
Group:      Development/Python3
Url:        http://github.com/saschpe/py2pack
Packager:   Andrey Cherepanov <cas@altlinux.org>

BuildArch:  noarch

Source:     %name-%version.tar
Patch1:     py2pack-alt-spec-support.patch
Patch2:     py2pack-alt-spec-default.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

Requires: python3-module-py2pack = %version-%release

%add_python3_req_skip distutils.core

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%package -n python3-module-py2pack
Summary: General purpose template engine
Group: Development/Python3
%description -n python3-module-py2pack
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%prep
%setup -n %oname-%version
%patch1 -p1
%patch2 -p1

%build

%pyproject_build

%install

%pyproject_install

%files
%_bindir/%oname

%files -n python3-module-py2pack
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1
- updated ALT patches for new version
- switch to pyproject build (hatchling)

* Mon Oct 23 2023 Anton Vyatkin <toni@altlinux.org> 0.8.7-alt2
- NMU: skip distutils.core requires.

* Mon Jun 07 2021 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt1
- New version.

* Tue Nov 10 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.6-alt1
- New version.
- Fix scripts iteration in alt.spec.

* Tue Oct 27 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.5-alt1
- New version.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt2
- Require python3(pbr) for correct version show.
- Add ALT spec template (ALT #38761).
- Use alt.spec template by default.

* Fri Jul 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version (ALT #38757).
- Fix License tag according to SPDX.
- Build from upstream tag.
- Change maintainer.

* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.4-alt2
- Porting on Python3.

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script) from github sources

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt2
- initial build for ALT Linux Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_4
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_3
- initial fc import

