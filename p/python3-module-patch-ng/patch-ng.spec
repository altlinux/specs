%define oname patch-ng

Name: python3-module-%oname
Summary: Library to parse and apply unified diffs
Version: 1.17.1
Release: alt1

Group: Development/Python3
License: MIT
Url: https://github.com/conan-io/python-patch-ng
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Library to parse and apply unified diffs.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md doc/ example/
%python3_sitelibdir/patch_ng*
%python3_sitelibdir/__pycache__/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.17.1-alt1
- Initial build

