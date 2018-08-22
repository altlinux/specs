%define  modulename cbor

%python_req_hier

Name:    python-module-%modulename
Version: 1.0.0
Release: alt1

Summary: CBOR rfc7049 for Python
License: ASL-2.0
Group:   Development/Python
URL:     https://github.com/brianolson/cbor

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

Source:  %modulename-%version.tar

%description
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

%package -n python3-module-%modulename
Summary: CBOR rfc7049 for Python 
Group: Development/Python3

%description -n python3-module-%modulename
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

Python 3 version.

%prep
%setup -n %modulename-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
