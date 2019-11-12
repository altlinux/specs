Name: json2yaml
Version: 1.1.1
Release: alt3

Summary: Convert JSON to YAML or vice versa, while preserving the order of associative arrays
License: ASLv2.0
Group: File tools
Url: https://pypi.python.org/pypi/json2yaml/
# https://github.com/drbild/json2yaml.git
BuildArch: noarch

Source: %{name}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docopt
BuildRequires: python3-module-yaml python3-module-pyaml

%py3_requires yaml pyaml docopt json


%description
Convert JSON to YAML or vice versa, while preserving the order of
associative arrays.

%prep
%setup -q

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name '%name' -o -name 'yaml2json' \))

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
#doc NOTICE *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt3
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Rebuilt to fix file permissions (closes: #34045)

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150127
- Initial build for Sisyphus

