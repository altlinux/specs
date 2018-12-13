%define oname flask-common

Name: python-module-%oname
Version: 0.3.0
Release: alt1

Summary: A Flask extension with lots of common time-savers (file-serving, favicons, etc).
License: Apache-2.0
Group: Development/Python
Url: https://github.com/kennethreitz/flask-common
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-flask
BuildRequires: python-module-gunicorn
BuildRequires: python-module-whitenoise
BuildRequires: python-module-crayons
BuildRequires: python-module-maya
BuildRequires: python-module-flask-caching

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-flask
BuildRequires: python3-module-gunicorn
BuildRequires: python3-module-whitenoise
BuildRequires: python3-module-crayons
BuildRequires: python3-module-maya
BuildRequires: python3-module-flask-caching

%description
A Flask extension with lots of common time-savers (file-serving, favicons, etc).

%package -n python3-module-%oname
Summary: A Flask extension with lots of common time-savers (file-serving, favicons, etc).
Group: Development/Python3
%description -n python3-module-%oname
A Flask extension with lots of common time-savers (file-serving, favicons, etc).

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc LICENSE *.md
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.md
%python3_sitelibdir/*


%changelog
* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.0-alt1
- 0.3.0

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
