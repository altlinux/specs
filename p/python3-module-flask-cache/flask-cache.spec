%define oname flask-cache

Name: python3-module-%oname
Version: 0.11
Release: alt2

Summary: Adds easy cache support to Flask.
License: MIT
Group: Development/Python3
Url: https://github.com/thadeusb/flask-cache
BuildArch: noarch

Source: %oname-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-werkzeug
BuildRequires: python3-module-flask python-tools-2to3


%description
Adds easy cache support to Flask.

%package docs
Summary: Adds easy cache support to Flask.
Group: Development/Documentation

%description docs
Adds easy cache support to Flask.

This package contains documentation for python-module-%oname

%prep
%setup -n %oname-%version
%patch0 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

export PYTHONPATH=$PWD
%make -C docs man

%install
%python3_install

%files
%doc LICENSE README CHANGES
%python3_sitelibdir/*

%files docs
%doc docs/*/man/*


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt2
- porting on python3

* Thu Mar 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt1
- Initial build for Sisyphus
