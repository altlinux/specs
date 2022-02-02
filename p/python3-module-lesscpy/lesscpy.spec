%define _unpackaged_files_terminate_build 1
%define mname lesscpy

%def_with check

Name: python3-module-%mname
Version: 0.15.0
Release: alt1

Summary: Python LESS Compiler
License: MIT
Group: Development/Python3
# Source-git: https://github.com/lesscpy/lesscpy.git
Url: https://pypi.org/project/lesscpy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
# install_requires=
BuildRequires: python3(ply)
BuildRequires: python3(six)

BuildRequires: python3(nose)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
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

%build
%python3_build

%install
%python3_install
mv %buildroot/%_bindir/{lesscpy,py3-lesscpy}

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc LICENSE README.rst
%_bindir/py3-lesscpy
%python3_sitelibdir/%mname/
%python3_sitelibdir/%mname-%version-py%_python3_version.egg-info/

%changelog
* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1
- 0.13.0 -> 0.15.0.

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

