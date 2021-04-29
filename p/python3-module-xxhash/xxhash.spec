%define _unpackaged_files_terminate_build 1
%define oname xxhash

%def_with check

Name: python3-module-%oname
Version: 2.0.2
Release: alt1
Summary: Binding for xxHash
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/xxhash/

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libxxhash-devel

%if_with check
BuildRequires: python3(tox)
%endif

%description
xxhash is a Python binding for the xxHash library.

%prep
%setup
%patch -p1

# remove bundled libs
rm -r deps

%build
# make use of system xxhash library
export XXHASH_LINK_SO=1
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[tox]
envlist = py%{python_version_nodots python},py%{python_version_nodots python3}

[testenv]
commands =
    python setup.py test -v
EOF
export PIP_NO_INDEX=YES
export XXHASH_LINK_SO=1
export TOX_TESTENV_PASSENV='XXHASH_LINK_SO'
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/xxhash/
%python3_sitelibdir/xxhash-%version-py%_python3_version.egg-info/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.4.3 -> 2.0.2.

* Fri Jan 17 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.3.0 -> 1.4.3 (Closes: #37849).

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- Initial build.
