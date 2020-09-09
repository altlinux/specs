%define _unpackaged_files_terminate_build 1
%define mname lesscpy

%def_with check

Name: python3-module-%mname
Version: 0.13.0
Release: alt2

Summary: Python LESS Compiler
License: MIT
Group: Development/Python3
# Source-git: https://github.com/lesscpy/lesscpy.git
Url: https://pypi.org/project/lesscpy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
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

%prep
%setup
# fix tests https://github.com/lesscpy/lesscpy/pull/99/files
sed -i 's@lessf = less.split(\x27.\x27)\[0\].split(\x27/\x27)\[-1\]@lessf = less.rpartition(\x27.\x27)\[0\].split(\x27/\x27)\[-1\]@' \
       test/core.py

%build
%python3_build

%install
%python3_install
mv %buildroot/%_bindir/{lesscpy,py3-lesscpy}

%check
export PIP_INDEX_URL=http://host.invalid./
# copy necessary exec deps
tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/nosetests3 .tox/py%{python_version_nodots python3}/bin/nosetests
tox.py3 --sitepackages -e py%{python_version_nodots python3}

%files
%doc LICENSE README.rst
%_bindir/py3-lesscpy
%python3_sitelibdir/%mname
%python3_sitelibdir/%{mname}*.egg-info

%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 0.13.0-alt2
- Stopped Python2 package build.

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

