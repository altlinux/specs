%define oname maya

Name: python-module-%oname
Version: 0.3.4
Release: alt1

Summary: Maya: Datetimes for Humans
License: MIT
Group: Development/Python
Url: https://github.com/kennethreitz/maya
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools

%add_python_req_skip ruamel pendulum

%description
Datetimes are very frustrating to work with in Python, especially when dealing
with different locales on different systems. This library exists to make the 
simple things much easier, while admitting that time is an illusion (timezones 
doubly so).

%package -n python3-module-%oname
Summary: Maya: Datetimes for Humans
Group: Development/Python3
%add_python3_req_skip ruamel.yaml pendulum

%description -n python3-module-%oname
Datetimes are very frustrating to work with in Python, especially when dealing
with different locales on different systems. This library exists to make the 
simple things much easier, while admitting that time is an illusion (timezones 
doubly so).

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
%doc LICENSE *.rst docs/* tests/
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.rst docs/* tests/
%python3_sitelibdir/*


%changelog
* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
