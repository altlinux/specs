%define oname crayons

Name: python-module-%oname
Version: 0.1.2
Release: alt1

Summary: This module is really simple, it gives you colored strings for terminal usage.
License: MIT
Group: Development/Python
Url: https://github.com/kennethreitz/crayons
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools

%description
Crayons is nice because it automatically wraps a given string in both the 
foreground color, as well as returning to the original state after the 
string is complete. Most terminal color libraries make you manage this 
yourself.

%package -n python3-module-%oname
Summary: This module is really simple, it gives you colored strings for terminal usage. etc).
Group: Development/Python3
%description -n python3-module-%oname
Crayons is nice because it automatically wraps a given string in both the 
foreground color, as well as returning to the original state after the 
string is complete. Most terminal color libraries make you manage this 
yourself.

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
%doc LICENSE *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*


%changelog
* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
