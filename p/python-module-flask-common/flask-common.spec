%define oname flask-common

Name: python-module-%oname
Version: 0.2.0
Release: alt1

Summary: A Flask extension with lots of common time-savers (file-serving, favicons, etc).
License: Apache-2.0
Group: Development/Python
Url: https://github.com/kennethreitz/flask-common
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools

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
* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
