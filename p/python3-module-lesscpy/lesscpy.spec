%define _unpackaged_files_terminate_build 1
%define pypi_name lesscpy
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.15.1
Release: alt1
Summary: Python LESS Compiler
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lesscpy
Vcs: https://github.com/lesscpy/lesscpy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
# upstream still uses deprecated nose
BuildRequires: python3-module-pytest
%endif

%description
A compiler written in Python for the LESS language. For those of us not willing
or able to have node.js installed in our environment. Not all features of LESS
are supported (yet). Some features wil probably never be supported (JavaScript
evaluation). This program uses PLY (Python Lex-Yacc) to tokenize / parse the
input and is considerably slower than the NodeJS compiler. The plan is to
utilize this to build in proper syntax checking and perhaps YUI compressing.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot/%_bindir/{lesscpy,py3-lesscpy}

%check
%pyproject_run_pytest -ra

%files
%doc LICENSE README.rst
%_bindir/py3-lesscpy
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 12 2024 Stanislav Levin <slev@altlinux.org> 0.15.1-alt1
- 0.15.0 -> 0.15.1.

* Thu Apr 06 2023 Anton Vyatkin <toni@altlinux.org> 0.15.0-alt2
- Fix BuildRequires

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

