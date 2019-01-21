%python_req_hier
%define  modulename treq

Name:    python-module-%modulename
Version: 18.6.0
Release: alt2

Summary: Python requests like API built on top of Twisted's HTTP client.
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/treq

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-incremental

%add_python_req_skip twisted.test twisted.test.proto_helpers twisted.trial twisted.trial.unittest

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-incremental

BuildArch: noarch

Source:  %modulename-%version.tar

%description
treq is an HTTP library inspired by requests but written on top of Twisted's
Agents.

It provides a simple, higher level API for making HTTP requests when using
Twisted.

%package -n python3-module-%modulename
Summary: Python requests like API built on top of Twisted's HTTP client.
Group: Development/Python3

%description -n python3-module-%modulename
treq is an HTTP library inspired by requests but written on top of Twisted's
Agents.

It provides a simple, higher level API for making HTTP requests when using
Twisted.

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
* Mon Jan 21 2019 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt2
- Added python_req_hier (Closes: 35940)

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt1
- Initial build for Sisyphus
