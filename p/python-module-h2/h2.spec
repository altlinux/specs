%def_with python3

%define oname h2
Name: python-module-%oname
Version: 3.0.1
Release: alt2

Summary: HTTP/2 State-Machine based protocol implementation

Url: http://hyper.rtfd.org
License: MIT
Group: Development/Python

# https://github.com/python-hyper/hyper-h2.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-hypothesis python-module-hyperframe python-module-hpack
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-hypothesis python3-module-hyperframe python3-module-hpack
%endif

%description
This repository contains a pure-Python implementation of a HTTP/2 protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can speak HTTP/2 regardless of your
programming paradigm.

%package -n python3-module-h2
Summary: HTTP/2 State-Machine based protocol implementation
Group: Development/Python3

%description -n python3-module-h2
This repository contains a pure-Python implementation of a HTTP/2 protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can speak HTTP/2 regardless of your
programming paradigm.
%prep
%setup

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

%check
PYTHONPATH=$(pwd) py.test

%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-h2
%python3_sitelibdir/*
%endif


%changelog
* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.1-alt2
- Enabled python-3 build.
- Enabled tests.

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for ALT Sisyphus

