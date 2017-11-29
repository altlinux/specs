%define _unpackaged_files_terminate_build 1
%define oname nose_warnings_filters

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1
Summary: Allow to inject warning filters during ``nosetest``.
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/nose_warnings_filters

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose
%endif

%description
Allow to inject warning filters during ``nosetest``.

%if_with python3
%package -n python3-module-%oname
Summary: Allow to inject warning filters during ``nosetest``.
Group: Development/Python3

%description -n python3-module-%oname
Allow to inject warning filters during ``nosetest``.
%endif

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt1
- Initial build for ALT.
