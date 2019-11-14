%define oname sphinxcontrib-ansi

%def_with bootstrap

Name: python3-module-%oname
Version: 0.6
Release: alt2

Summary: Sphinx extension ansi
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxcontrib-ansi/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-mock

%if_with bootstrap
%py3_provides sphinxcontrib.ansi
%py3_requires sphinxcontrib sphinx
%endif


%description
A Sphinx extension, which turns ANSI color sequences in Sphinx documents
into colored HTML output.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
# py3.test -vv

%files
%doc README *.rst doc/*.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- python2 -> python3

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.3
- (NMU) rebuild with all requires

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1.2
- (NMU) rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

