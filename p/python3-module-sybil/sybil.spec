%define _unpackaged_files_terminate_build 1

%define  oname sybil
%def_with check

Name:    python3-module-%oname
Version: 3.0.1
Release: alt1

Summary:  Automated testing for the examples in your documentation.
License: MIT
Group:   Development/Python3
URL:     https://github.com/cjw296/sybil

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

# https://github.com/cjw296/sybil.git
Source: %name-%version.tar

%description
Automated testing for the examples in your documentation.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false --develop

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 1.4.0 -> 3.0.1.

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.0.7 -> 1.4.0.
- Stopped Python2 package build.

* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt2
- Fixed documentation build.

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.
