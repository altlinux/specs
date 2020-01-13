Name: python3-module-zeroconf
Version: 0.24.4
Release: alt1

Summary: Pure Python Multicast DNS Service Discovery Library
License: LGPLv2
Group: Development/Python
Url: https://pypi.org/project/zeroconf/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
This is fork of pyzeroconf, Multicast DNS Service Discovery for Python,
originally by Paul Scott-Murphy (https://github.com/paulsm/pyzeroconf),
modified by William McBrine (https://github.com/wmcbrine/pyzeroconf).

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/zeroconf
%python3_sitelibdir/zeroconf-%version-*-info

%changelog
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
