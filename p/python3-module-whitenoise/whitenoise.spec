%define oname whitenoise

%def_with check

Name: python3-module-%oname
Version: 6.3.0
Release: alt1

Summary: Radically simplified static file serving for Python web apps

License: MIT
Group: Development/Python3
Url: https://github.com/evansd/whitenoise

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-django
BuildRequires: python3-module-brotlipy
%endif

%description
With a couple of lines of config WhiteNoise allows your web app to serve
its own static files, making it a self-contained unit that can be deployed
anywhere without relying on nginx, Amazon S3 or any other external service.
(Especially useful on Heroku, OpenShift and other PaaS providers.)

%package docs
Summary: Documentation for %name
Group: Development/Documentation

%description docs
With a couple of lines of config WhiteNoise allows your web app to serve
its own static files, making it a self-contained unit that can be deployed
anywhere without relying on nginx, Amazon S3 or any other external service.
(Especially useful on Heroku, OpenShift and other PaaS providers.)

This package contains documentation for %name

%prep
%setup

%build
%pyproject_build

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs man

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Sat Jan 07 2023 Grigory Ustinov <grenka@altlinux.org> 6.3.0-alt1
- Automatically updated to 6.3.0.
- Build with check.

* Mon Jun 06 2022 Grigory Ustinov <grenka@altlinux.org> 6.2.0-alt1
- Automatically updated to 6.2.0.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt1
- 6.1.0

* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt2
- Drop python2 support.

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus
