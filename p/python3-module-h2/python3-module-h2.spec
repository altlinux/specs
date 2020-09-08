%def_with python3

%define oname h2

Name: python3-module-h2
Version: 3.0.1
Release: alt4

Summary: HTTP/2 State-Machine based protocol implementation

Group: Development/Python3
License: MIT
Url: https://github.com/python-hyper/hyper-h2

# Source-url: https://github.com/python-hyper/hyper-h2/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-hyperframe >= 5.0
BuildRequires: python3-module-hpack >= 2.3

# for test
BuildRequires: python3-module-hypothesis

%description
This repository contains a pure-Python implementation of a HTTP/2 protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can speak HTTP/2 regardless of your
programming paradigm.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
PYTHONPATH=$(pwd) py.test3

%files
%python3_sitelibdir/h2/
%python3_sitelibdir/h2*.egg-info/

%changelog
* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt4
- standalone build python3 module

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 3.0.1-alt3
- Fixed testing against Pytest 5.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.1-alt2
- Enabled python-3 build.
- Enabled tests.

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for ALT Sisyphus

