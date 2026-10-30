Name: python3-module-probatio
Version: 0.13.0
Release: alt2

Summary: Data validation library
License: MIT
Group: Development/Python
URL: https://pypi.org/project/probatio
VCS: https://github.com/frenck/probatio

Source0: %name-%version.tar
Source1: pyproject_deps.json

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Probatio is a modern, maintained data validation library for Python. The model
is simple: a schema is data, and data describes data. You compose schemas from
plain Python types, dicts, lists, and a handful of small helpers, then call the
schema with a value to validate it.
It is a drop-in for voluptuous: the same public API, so you can swap the import
and keep your existing schemas.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup test
sed -ri '/^version\s*=/ s,"[^"]+","%version",' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_fuzz_engine.py::test_matches_voluptuous: upstream test-suite bug —
# the fuzz strategy never avoids ADR-017's deliberate float/int deviation
# from voluptuous; fails with hypothesis != 6.168.3. Deselect until fixed upstream.
%pyproject_run_pytest -o addopts= --deselect tests/test_fuzz_engine.py::test_matches_voluptuous

%files
%python3_sitelibdir/probatio
%python3_sitelibdir/probatio-%version.dist-info

%changelog
* Fri Oct 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.13.0-alt2
- ftbfs fixed by deselecting questionable test

* Tue Oct 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.13.0-alt1
- 0.13.0 released

