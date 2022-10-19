%define _unpackaged_files_terminate_build 1
%define pypi_name xxhash

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt1
Summary: Binding for xxHash
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/xxhash/
VCS: https://github.com/ifduyue/python-xxhash.git

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libxxhash-devel

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%description
xxhash is a Python binding for the xxHash library.

%prep
%setup
%patch -p1

# remove bundled libs
rm -r deps

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
# make use of system xxhash library
export XXHASH_LINK_SO=1
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
allowlist_externals =
    bash
commands =
    bash -c 'cd tests && python -m unittest -v'
EOF
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/xxhash/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.0.2 -> 3.1.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.4.3 -> 2.0.2.

* Fri Jan 17 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.3.0 -> 1.4.3 (Closes: #37849).

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- Initial build.
