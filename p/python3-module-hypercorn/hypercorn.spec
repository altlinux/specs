%define _unpackaged_files_terminate_build 1
%define pypi_name Hypercorn
%define pypi_nname hypercorn
%define mod_name %pypi_nname

%def_with check

Name: python3-module-%pypi_nname
Version: 0.18.0
Release: alt2
Summary: A ASGI Server based on Hyper libraries
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hypercorn
Vcs: https://github.com/pgjones/hypercorn/
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
Hypercorn is an ASGI and WSGI web server based on the sans-io hyper, h11, h2,
and wsproto libraries and inspired by Gunicorn. Hypercorn supports HTTP/1,
HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI, and WSGI specifications.
Hypercorn can utilise asyncio, uvloop, or trio worker types.

Hypercorn can optionally serve the current draft of the HTTP/3 specification
using the aioquic library.

%pyproject_configure_pypi_subpackage h3
%pyproject_configure_pypi_subpackage trio
%pyproject_configure_pypi_subpackage uvloop

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%_bindir/hypercorn
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 09 2026 Stanislav Levin <slev@altlinux.org> 0.18.0-alt2
- Fixed FTBFS (h2 4.3.0).

* Tue Dec 09 2025 Stanislav Levin <slev@altlinux.org> 0.18.0-alt1
- 0.17.3 -> 0.18.0.

* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 0.17.3-alt1
- 0.17.2 -> 0.17.3.

* Tue May 28 2024 Stanislav Levin <slev@altlinux.org> 0.17.2-alt1
- 0.16.0 -> 0.17.2.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.16.0-alt2
- Fixed FTBFS (trio 0.25.0).

* Mon Feb 05 2024 Stanislav Levin <slev@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus.
