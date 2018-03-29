%define oname whitenoise

Name: python-module-%oname
Version: 3.3.1
Release: alt1

Summary: Radically simplified static file serving for Python web apps
License: MIT
Group: Development/Python
Url: https://github.com/evansd/whitenoise
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx python-module-sphinx_rtd_theme

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-sphinx python3-module-sphinx_rtd_theme


%description
With a couple of lines of config WhiteNoise allows your web app to serve 
its own static files, making it a self-contained unit that can be deployed 
anywhere without relying on nginx, Amazon S3 or any other external service. 
(Especially useful on Heroku, OpenShift and other PaaS providers.)

%package -n python3-module-%oname
Summary: Radically simplified static file serving for Python web apps
Group: Development/Python3

%description -n python3-module-%oname
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
%setup -n %oname-%version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

export PYTHONPATH=$PWD
%make -C docs man

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc LICENSE *.rst tests/
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.rst tests/
%python3_sitelibdir/*

%files docs
%doc docs/*


%changelog
* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus
