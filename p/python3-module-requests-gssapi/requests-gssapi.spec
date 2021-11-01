%define _unpackaged_files_terminate_build 1
%define mname requests-gssapi

%def_with check

Name: python3-module-%mname
Version: 1.2.3
Release: alt1

Summary: A GSSAPI/SPNEGO authentication handler for python-requests
License: ISC
Group: Development/Python3
# Source-git: https://github.com/pythongssapi/requests-gssapi.git
Url: https://pypi.org/project/requests-gssapi

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(gssapi)
BuildRequires: python3(requests)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

# PyPI name
%py3_provides requests-gssapi
Provides: python3-module-requests_gssapi = %EVR

%description
Requests is an HTTP library, written in Python, for human beings.
This library adds optional GSSAPI authentication support and
supports mutual authentication.

It provides a fully backward-compatible shim for the old
python-requests-kerberos library. A more powerful interface is
provided by the HTTPSPNEGOAuth component, but this is of course not
guaranteed to be compatible.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands = {envpython} -m pytest {posargs:.}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc AUTHORS LICENSE *.rst
%python3_sitelibdir/requests_gssapi/
%python3_sitelibdir/requests_gssapi-%version-py%_python3_version.egg-info/

%changelog
* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- 1.2.1 -> 1.2.3.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- removed python-2.7 support

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1.

* Mon Jul 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fix regex string escaping

* Fri May 04 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build
