%define modulename wget

Name: python3-module-%modulename
Version: 3.2
Release: alt2

Summary: pure python download utility
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/wget
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
%summary

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install 

%files
%python3_sitelibdir/%modulename.*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%modulename-*.egg-info


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt2
- python2 disabled

* Tue Oct 11 2016 Konstantin Artyushkin <akv@altlinux.org> 3.2-alt1
- new version

