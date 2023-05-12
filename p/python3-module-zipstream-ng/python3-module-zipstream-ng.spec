%define _unpackaged_files_terminate_build 1
%define  modulename zipstream

%def_enable check

Name:    python3-module-zipstream-ng
Version: 1.5.0
Release: alt1

Summary: A modern and easy to use streamable zip file generator.
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/pR0Ps/zipstream-ng.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

Conflicts: python3-module-zipstream

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary
It can package and stream many files and folders on the fly without 
needing temporary files or excessive memory.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs}
EOF

%tox_check_pyproject -- -vra

%files
%_bindir/zipserver
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{modulename}_ng-%version.dist-info/


%changelog
* Fri May 12 2023 Danil Shein <dshein@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 1.3.4-alt1
- initial build for Sisyphus

