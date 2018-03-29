%define oname flask-cache

Name: python-module-%oname
Version: 0.11
Release: alt1

Summary: Adds easy cache support to Flask.
License: MIT
Group: Development/Python
Url: https://github.com/thadeusb/flask-cache
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-werkzeug
BuildRequires: python-module-flask

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-werkzeug
BuildPreReq: python3-module-flask

%description
Adds easy cache support to Flask.

%package -n python3-module-%oname
Summary: Adds easy cache support to Flask.
Group: Development/Python3
%add_python3_req_skip exceptions

%description -n python3-module-%oname
Adds easy cache support to Flask.

%package docs
Summary: Adds easy cache support to Flask.
Group: Development/Documentation

%description docs
Adds easy cache support to Flask.

This package contains documentation for python-module-%oname

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +

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
%doc LICENSE README CHANGES
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE README CHANGES
%python3_sitelibdir/*

%files docs
%doc docs/*/man/*


%changelog
* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt1
- Initial build for Sisyphus
