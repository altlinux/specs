%define _unpackaged_files_terminate_build 1
%define pypi_name Hypercorn
%define pypi_nname hypercorn
%define mod_name %pypi_nname

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%{expand:%%pyproject_runtimedeps_metadata -- --extra %1} \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

%def_with check

Name: python3-module-%pypi_nname
Version: 0.17.3
Release: alt1
Summary: A ASGI Server based on Hyper libraries
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hypercorn
Vcs: https://github.com/pgjones/hypercorn/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Hypercorn is an ASGI and WSGI web server based on the sans-io hyper, h11, h2,
and wsproto libraries and inspired by Gunicorn. Hypercorn supports HTTP/1,
HTTP/2, WebSockets (over HTTP/1 and HTTP/2), ASGI, and WSGI specifications.
Hypercorn can utilise asyncio, uvloop, or trio worker types.

Hypercorn can optionally serve the current draft of the HTTP/3 specification
using the aioquic library.

%add_python_extra h3
%add_python_extra trio
%add_python_extra uvloop

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc README.*
%_bindir/hypercorn
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 0.17.3-alt1
- 0.17.2 -> 0.17.3.

* Tue May 28 2024 Stanislav Levin <slev@altlinux.org> 0.17.2-alt1
- 0.16.0 -> 0.17.2.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.16.0-alt2
- Fixed FTBFS (trio 0.25.0).

* Mon Feb 05 2024 Stanislav Levin <slev@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus.
