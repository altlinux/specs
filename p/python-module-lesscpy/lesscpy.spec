%define _unpackaged_files_terminate_build 1
%define mname lesscpy

%def_with check

Name: python-module-%mname
Version: 0.13.0
Release: alt1

Summary: Python LESS Compiler
License: MIT
Group: Development/Python
# Source-git: https://github.com/lesscpy/lesscpy.git
Url: https://pypi.org/project/lesscpy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-tox
BuildRequires: python-module-ply
BuildRequires: python-module-coverage
BuildRequires: python-module-flake8
BuildRequires: python-module-nose
BuildRequires: python3-module-tox
BuildRequires: python3-module-ply
BuildRequires: python3-module-coverage
BuildRequires: python3-module-flake8
BuildRequires: python3-module-nose
%endif

BuildArch: noarch

%description
A compiler written in Python for the LESS language. For those of us not willing
or able to have node.js installed in our environment. Not all features of LESS
are supported (yet). Some features wil probably never be supported (JavaScript
evaluation). This program uses PLY (Python Lex-Yacc) to tokenize / parse the
input and is considerably slower than the NodeJS compiler. The plan is to
utilize this to build in proper syntax checking and perhaps YUI compressing.

%package -n python3-module-%mname
Summary: Python3 LESS Compiler
Group: Development/Python3

%description -n python3-module-%mname
A compiler written in Python for the LESS language. For those of us not willing
or able to have node.js installed in our environment. Not all features of LESS
are supported (yet). Some features wil probably never be supported (JavaScript
evaluation). This program uses PLY (Python Lex-Yacc) to tokenize / parse the
input and is considerably slower than the NodeJS compiler. The plan is to
utilize this to build in proper syntax checking and perhaps YUI compressing.

%prep
%setup
# fix tests https://github.com/lesscpy/lesscpy/pull/99/files
sed -i 's@lessf = less.split(\x27.\x27)\[0\].split(\x27/\x27)\[-1\]@lessf = less.rpartition(\x27.\x27)\[0\].split(\x27/\x27)\[-1\]@' \
       test/core.py
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install

pushd ../python3
%python3_install
mv %buildroot/%_bindir/{lesscpy,py3-lesscpy}
popd

%python_install

%check
export PIP_INDEX_URL=http://host.invalid./
# copy necessary exec deps
tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/nosetests .tox/py%{python_version_nodots python}/bin/
tox --sitepackages -e py%{python_version_nodots python} -v

pushd ../python3
# copy necessary exec deps
tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/nosetests3 .tox/py%{python_version_nodots python3}/bin/nosetests
tox.py3 --sitepackages -e py%{python_version_nodots python3}
popd

%files
%doc LICENSE README.rst
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-py?.?.egg-info
%_bindir/lesscpy

%files -n python3-module-%mname
%doc LICENSE README.rst
%_bindir/py3-lesscpy
%python3_sitelibdir/%mname
%python3_sitelibdir/%{mname}*.egg-info

%changelog
* Fri Jun 15 2018 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1
- 0.10.1 -> 0.13.0

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.10.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.10.1-alt1
- First build for ALT (based on Fedora 0.10.1-3.fc21.src)

