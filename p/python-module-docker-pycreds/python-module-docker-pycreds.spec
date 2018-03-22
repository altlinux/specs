%define oname docker-pycreds
%define modname dockerpycreds
%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1

Summary: Python bindings for the docker credentials store API

License: %asl
Group: Development/Python
Url: https://github.com/shin-/dockerpy-creds

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
Python bindings for the docker credentials store API

%if_with python3
%package -n python3-module-%oname
Summary: Python bindings for the docker credentials store API (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the docker credentials store API
%endif


%prep
%setup -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.md
%python_sitelibdir/%modname
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 0.2.2-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus
