%define _unpackaged_files_terminate_build 1
%define modname cloudant

Name: python-module-%modname
Version: 2.9.0
Release: alt1

Summary: A Python library for Cloudant and CouchDB
License: Apache-2.0
Group: Development/Python
URL: https://github.com/cloudant/python-cloudant
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-devel

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools


%description
A Python library for Cloudant and CouchDB.

%package -n python3-module-%modname
Summary: A Python library for Cloudant and CouchDB
Group: Development/Python3

%description -n python3-module-%modname
A Python library for Cloudant and CouchDB.

%prep
%setup

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
%doc LICENSE README.md
%python_sitelibdir/%modname
%python_sitelibdir/%modname-%version-py*.egg-info

%files -n python3-module-%modname
%doc LICENSE README.md
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-py*.egg-info


%changelog
* Wed Dec 26 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build
