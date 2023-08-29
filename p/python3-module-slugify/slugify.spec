%define _unpackaged_files_terminate_build 1
%define  modulename slugify

%def_with check

Name:    python3-module-%modulename
Version: 6.1.1
Release: alt2

Summary: Returns unicode slugs
License: MIT
Group:   Development/Python3
URL:     https://github.com/un33k/python-slugify

Provides: python3-module-python-%modulename = %EVR

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(text_unidecode)

BuildRequires: python3(tox)
%endif

BuildArch: noarch

Source: %name-%version.tar

# try-except import
%py3_requires text_unidecode

%description
A Python slugify application that handles unicode.

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
    python test.py
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false --develop

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/python_slugify-%version-py%_python3_version.egg-info/

%changelog
* Sun Aug 27 2023 Alexandr Shashkin <dutyrok@altlinux.org> 6.1.1-alt2
- added provide to normalized project name for compability with Python
  ecosystem

* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 4.0.1 -> 6.1.1.

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.1-alt1
- 4.0.1 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- 4.0.0 released

* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.4-alt1
- Separate build for Sisyphus
