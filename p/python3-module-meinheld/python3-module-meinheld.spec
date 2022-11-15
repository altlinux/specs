%define  oname meinheld

%def_with check

Name:    python3-module-%oname
Version: 0.6.1
Release: alt3.1

Summary: meinheld is a high performance asynchronous WSGI Web Server (based on picoev)
License: BSD
Group:   Development/Python3
URL:     https://github.com/mopemope/meinheld

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-distribute

%if_with check
BuildRequires: python3-module-gunicorn
%endif

Source:  %oname-%version.tar


%description
%summary

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/

%description tests
%summary

This package contains tests for %oname

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

mv tests/ %buildroot%python3_sitelibdir/%oname/

%if_with check
%check
%__python3 setup.py test
%endif

%files
%doc LICENSE *.rst example/
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%exclude %python3_sitelibdir/%oname/tests/

%files tests
%python3_sitelibdir/%oname/tests/


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.6.1-alt3.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Oct 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- fix build

* Fri Feb 22 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.1-alt2
- Fix license

* Thu Dec 13 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
