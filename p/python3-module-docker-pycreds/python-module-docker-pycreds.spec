%define oname docker-pycreds
%define modname dockerpycreds

Name: python3-module-%oname
Version: 0.4.0
Release: alt3

Summary: Python bindings for the docker credentials store API
License: %asl
Group: Development/Python3
Url: https://github.com/shin-/dockerpy-creds
BuildArch: noarch

Source: %oname-%version.tar

# Remove dependency on distutils
Patch: 27cbd31e74a38ad91a70365939299bcee96c3c09.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-distribute


%description
Python bindings for the docker credentials store API

%prep
%setup -n %oname-%version
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-*


%changelog
* Thu Oct 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt3
- Dropped dependency on distutils.

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- python2 disabled

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.ru> 0.4.0-alt1
- New version

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 0.3.0-alt1
- New version

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.ru> 0.2.3-alt1
- New version

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 0.2.2-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus
