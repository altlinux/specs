%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-systemd
Epoch: 1
Version: 234
Release: alt3
Summary: Python module wrapping systemd functionality
Group: Development/Python3

License: LGPLv2+
Url: https://github.com/systemd/python-systemd
Source: %name-%version.tar
Patch1: %name-snapshot.patch

BuildPreReq: rpm-build-python3
BuildRequires: python3-devel python3-module-lxml
BuildRequires: libsystemd-devel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Python module for native access to the systemd facilities.
Functionality includes sending of structured messages to the journal
and reading journal files, querying machine and boot identifiers and a
lists of message identifiers provided by systemd. Other functionality
provided by libsystemd is also wrapped.

%prep
%setup -q
%patch1 -p1

%build
%python3_build

%install
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/systemd/test/

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest {posargs:-vra systemd/test}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/systemd/
%python3_sitelibdir/systemd_python-%version-py%_python3_version.egg-info/

%changelog
* Mon Jan 24 2022 Stanislav Levin <slev@altlinux.org> 1:234-alt3
- Applied upstream patches (fixed build against Python3.10).

* Mon Oct 05 2020 Stanislav Levin <slev@altlinux.org> 1:234-alt2
- Stopped Python2 package build.
- Enabled testing.
- Dropped dependency on Pytest at runtime.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:234-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Aug 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1:234-alt1
- 234

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:230-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:230-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1:230-alt1
- Initial packaging

