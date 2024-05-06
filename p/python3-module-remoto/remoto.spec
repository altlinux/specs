%define oname remoto

Name: python3-module-%oname
Version: 1.2.1
Release: alt2
Summary: Execute remote commands or processes
Group: Development/Python3

License: MIT
Url: https://github.com/alfredodeza/remoto

# https://github.com/alfredodeza/remoto.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-execnet
BuildRequires: python3-module-setuptools
Requires: python3-module-execnet

%description
Execute remote commands or processes.

%prep
%setup
%patch -p1

%build
export REMOTO_NO_VENDOR=1
%python3_build

%install
export REMOTO_NO_VENDOR=1
%python3_install -O1

%check
export REMOTO_NO_VENDOR=1
export PYTHONPATH=$(pwd)
py.test3 -v remoto/tests

%files
%python3_sitelibdir/*
%doc LICENSE README.rst

%changelog
* Mon May 06 2024 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt2
- Fix tests

* Fri Sep 10 2021 Alexey Shabalin <shaba@altlinux.org> 1.2.1-alt1
- new version 1.2.1

* Tue Feb 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.4-alt1
- build python3 package

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.30-alt1
- Updated to upstream version 0.0.30.

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 0.0.28-alt1
- First build for Sisyphus (based on 0.0.28-1.fc25)

