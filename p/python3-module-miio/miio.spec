Name: python3-module-miio
Version: 0.5.12
Release: alt3

Provides: python3-module-python-miio = %EVR

Summary: Python miIO library
License: BSD
Group: Development/Python
Url: https://pypi.org/project/python-miio/

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%package -n miio-tools
Summary: miIO tools
Group: Development/Python
Requires: python3-module-miio = %version-%release

%description
This library (and its accompanying cli tool) can be used to interface
with devices using Xiaomi's miIO and miOT protocols.

%description -n miio-tools
This library (and its accompanying cli tool) can be used to interface
with devices using Xiaomi's miIO and miOT protocols.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
find %buildroot%python3_sitelibdir -type f -name \*.py |\
	xargs grep -l 'miio.tests.dummies' |\
	sed 's,%buildroot,%exclude ,' > tests.files
find %buildroot%python3_sitelibdir -type d -name tests |\
	sed 's,%buildroot,%exclude ,' >> tests.files

%files -f tests.files
%python3_sitelibdir/miio
%python3_sitelibdir/python_miio-%version.dist-info

%files -n miio-tools
%_bindir/*

%changelog
* Thu Oct 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.12-alt3
- provide python-miio

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.12-alt2
- avoid appdirs dependency

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.12-alt1
- 0.5.12 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.11-alt1
- 0.5.11 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.10-alt1
- 0.5.10 released

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.9.2-alt1
- 0.5.9.2 released

* Thu Oct 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.8-alt1
- 0.5.8 released

* Tue Jun 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.6-alt1
- 0.5.6 released

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.5-alt1
- 0.5.5 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt1
- 0.5.4 released

* Fri Nov 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt2
- exclude tests from package due to excessive reqs

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- 0.5.3 released

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2.1-alt1
- initial
