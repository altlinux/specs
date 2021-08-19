%define oname whitenoise

Name: python3-module-%oname
Version: 5.3.0
Release: alt1

Summary: Radically simplified static file serving for Python web apps
License: MIT
Group: Development/Python3
Url: https://github.com/evansd/whitenoise
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme

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
%python3_build

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs man

%install
%python3_install

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%files docs
%doc docs/*

%changelog
* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt2
- Drop python2 support.

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus
