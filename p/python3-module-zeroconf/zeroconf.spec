Name: python3-module-zeroconf
Version: 0.39.4
Release: alt1

Summary: Pure Python Multicast DNS Service Discovery Library
License: LGPLv2
Group: Development/Python
Url: https://pypi.org/project/zeroconf/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/zeroconf
%python3_sitelibdir/zeroconf-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.39.4-alt1
- 0.39.4 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.39.1-alt1
- 0.39.1 released

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.7-alt1
- 0.38.7 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.6-alt1
- 0.38.6 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.4-alt1
- 0.38.4 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.3-alt1
- 0.38.3 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.36.8-alt1
- 0.36.8 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.36.7-alt1
- 0.36.7 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.33.3-alt1
- 0.33.3

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.31.0-alt1
- 0.31.0 released

* Fri Apr 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.29.0-alt2
- exclude tests

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.29.0-alt1
- 0.29.0 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.28.8-alt1
- 0.28.8 released

* Tue Nov 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.28.6-alt1
- 0.28.6 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.28.5-alt1
- 0.28.5 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.28.0-alt1
- 0.28.0 released

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.27.1-alt1
- 0.27.1 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24.4-alt1
- 0.24.4 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.0-alt1
- 0.23.0 released

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2
- Rebuilt to regenerate dependencies.

* Fri Oct 20 2017 Anton Midyukov <antohami@altlinux.org> 0.19.1-alt1
- new version 0.19.1

* Mon Sep 19 2016 Anton Midyukov <antohami@altlinux.org> 0.17.6-alt1
- Initial build for Alt Linux Sisiphus.
