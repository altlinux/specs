%define _unpackaged_files_terminate_build 1
%define oname fissix
%def_with check

Name: python3-module-%oname
Version: 21.11.13
Release: alt1

Summary: Backport of latest lib2to3, with enhancements
License: Python
Group: Development/Python3
BuildArch: noarch

Url: https://github.com/jreese/fissix
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(flit)
BuildRequires: python3(appdirs)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3-test
%endif

%description
Backport of latest lib2to3, with enhancements.

%prep
%setup

%build
# generate setup.py for legacy builder (flit build backend)
%__python3 - <<-'EOF'
from pathlib import Path
from flit.sdist import SdistBuilder


with open("setup.py", "wb") as f:
    sd_builder = SdistBuilder.from_ini_path(Path("pyproject.toml"))
    f.write(sd_builder.make_setup_py())
EOF
%python3_build

%install
%python3_install
cp -p %oname/*.txt %buildroot%python3_sitelibdir/%oname/

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    python3 -m pytest --verbose tests %oname/tests
EOF
export PIP_NO_BUILD_ISOLATION=no
export TOXENV=py3
tox.py3 --sitepackages -vv

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Feb 01 2022 Ivan Alekseev <qwetwe@altlinux.org> 21.11.13-alt1
- 21.11.13
