%define _unpackaged_files_terminate_build 1
%define oname xxhash

%def_with check

Name: python-module-%oname
Version: 1.4.3
Release: alt1
Summary: Binding for xxHash
License: BSD-2-Clause
Group: Development/Python
Url: https://pypi.org/project/xxhash/

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libxxhash-devel

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(tox)
%endif

%description
xxhash is a Python binding for the xxHash library.

%package -n python3-module-%oname
Summary: Binding for xxHash
Group: Development/Python3

%description -n python3-module-%oname
xxhash is a Python3 binding for the xxHash library.

%prep
%setup
%patch -p1

# remove bundled libs
rm -r deps

rm -rf ../python3
cp -a . ../python3

%build
# make use of system xxhash library
export XXHASH_LINK_SO=1
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

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
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/xxhash/
%python_sitelibdir/xxhash-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/xxhash/
%python3_sitelibdir/xxhash-%version-py%_python3_version.egg-info/

%changelog
* Fri Jan 17 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.3.0 -> 1.4.3 (Closes: #37849).

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- Initial build.
