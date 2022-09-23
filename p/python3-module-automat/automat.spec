%define _unpackaged_files_terminate_build 1
%define pypi_name Automat
%define mod_name automat

%def_with check

Name: python3-module-%mod_name
Version: 20.2.0
Release: alt3

Summary: Self-service finite-state machines for the programmer on the go

Url: https://pypi.org/project/Automat/
License: MIT
Group: Development/Python3

# Source-url: https://github.com/glyph/automat
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools-scm)

%if_with check
# deps
BuildRequires: python3(six)
BuildRequires: python3(attrs)

# extra
BuildRequires: python3(graphviz)
BuildRequires: python3(twisted)
BuildRequires: /usr/bin/dot

BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%package visualize
Summary: %summary
Group: Development/Python3
Requires: %name
%py3_requires graphviz
%py3_requires twisted
Requires: /usr/bin/dot

%description visualize
Extra 'visualize' for %pypi_name.

%prep
%setup
%autopatch -p1

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
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%python3_sitelibdir/automat/_test/

%check
%tox_check_pyproject -- -vra

%files
%python3_sitelibdir/%mod_name/
%exclude %python3_sitelibdir/%mod_name/_visualize.py
%exclude %python3_sitelibdir/%mod_name/__pycache__/_visualize.*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%files visualize
%_bindir/automat-visualize
%python3_sitelibdir/%mod_name/_visualize.py
%python3_sitelibdir/%mod_name/__pycache__/_visualize.*

%changelog
* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 20.2.0-alt3
- Modernized packaging.
- Dropped dependency on unmaintained m2r.
- Packaged visualize tool.
- Enabled testing.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 20.2.0-alt2
- build python3 package separately

* Thu Mar 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 20.2.0-alt1
- new version (20.2.0) with rpmgs script

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1.qa1
- NMU: applied repocop patch

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Sisyphus

