%define oname pydotplus

Name: python3-module-%oname
Version: 2.0.2
Release: alt2

Summary: Python interface to Graphviz Dot language
License: MIT
Group: Development/Python3
Url: https://github.com/carlos-jenkins/pydotplus
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyparsing

Requires: %_bindir/dot


%description
PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz Dot language.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.2-alt2
- python2 disabled

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- Initial build
