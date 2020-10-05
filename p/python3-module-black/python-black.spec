%define _unpackaged_files_terminate_build 1
%define oname black

%def_with check

Name: python3-module-%oname
Version: 20.8b1
Release: alt1

Summary: The Uncompromising Code Formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/black/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3(aiohttp)
BuildRequires: python3(aiohttp.test_utils)
BuildRequires: python3(aiohttp_cors)
BuildRequires: python3(appdirs)
BuildRequires: python3(click)
BuildRequires: python3(click.testing)
BuildRequires: python3(mypy_extensions)
BuildRequires: python3(pathspec)
BuildRequires: python3(regex)
BuildRequires: python3(toml)
BuildRequires: python3(tox)
BuildRequires: python3(typing_extensions)
%endif

%py3_provides black_primer

%description
Black is the uncompromising Python code formatter. By using it, you agree to
cede control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting. You
will save time and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading.
Formatting becomes transparent after a while and you can focus on the content
instead.

Black makes code review faster by producing the smallest diffs possible.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envpython} -m unittest {posargs}
EOF

export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc README.md LICENSE
%_bindir/black
%_bindir/blackd
%_bindir/black-primer
%python3_sitelibdir/*

%changelog
* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 20.8b1-alt1
- Initial build for Sisyphus.
