%define _unpackaged_files_terminate_build 1
%define pypi_name tinycss2

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: A tiny CSS parser
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/tinycss2/
VCS: https://github.com/Kozea/tinycss2.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

# submodule
# tests/css-parsing-tests from https://github.com/SimonSapin/css-parsing-tests
Source1: css-parsing-tests.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%if_with check
# deps
BuildRequires: python3(webencodings)

BuildRequires: python3(pytest)
%endif

%description
%pypi_name is a low-level CSS parser and generator written in Python: it can
parse strings, return objects representing tokens and blocks, and generate CSS
strings corresponding to these objects.

Based on the CSS Syntax Level 3 specification, %pypi_name knows the grammar of
CSS but doesn't know specific rules, properties or values supported in various
CSS modules.

%prep
%setup -a1
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst docs/changelog.rst
%python3_sitelibdir/tinycss2/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 03 2022 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.2 -> 1.1.1.
- Enabled testing.

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt1
- Version updated to 1.0.2.

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Updated to upstream version 0.6.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20140819.1
- NMU: Use buildreq for BR.

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140819
- Initial build for Sisyphus

