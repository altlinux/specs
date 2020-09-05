Name: ansible-lint
Version: 4.3.4
Release: alt1

Summary: Best practices checker for Ansible

Group: System/Libraries
License: MIT
Url: https://github.com/willthames/ansible-lint

Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-tools
BuildRequires: python3-module-tox python3-module-pip python3-module-wheel
BuildRequires: python3-module-setuptools_scm >= 3.5.0
BuildRequires: python3-module-setuptools_scm_git_archive >= 1.0
BuildRequires: python3-module-yaml
BuildRequires: python3-module-rich
BuildRequires: python3-module-ruamel-yaml >= 0.15.37
BuildRequires: python3-module-typing_extensions
BuildRequires: ansible >= 2.8

# for python3 < 3.8
Requires: python3-module-typing_extensions

%description
ansible-lint checks playbooks for practices and behaviour that could potentially be improved

%prep
%setup
echo "ref-names: tag: v%version" > .git_archival.txt

%build
python3 -m pip wheel --wheel-dir pyproject_wheeldir --no-deps --use-pep517 --no-build-isolation --disable-pip-version-check --progress-bar off --verbose .
#%%python3_build

%install
python3 -m pip install --root %buildroot --no-deps --disable-pip-version-check --progress-bar off --verbose --ignore-installed --no-warn-script-location pyproject_wheeldir/*.whl
if [ -d %buildroot%_bindir ]; then
  pathfix.py -pni "%__python3" %buildroot%_bindir/*
  rm -rfv %buildroot%_bindir/__pycache__
fi
if [ -d %buildroot%python3_sitelibdir ]; then
  sed -i 's/pip/rpm/' %buildroot%python3_sitelibdir/*.dist-info/INSTALLER
fi
if [ -d %buildroot%python3_sitelibdir_noarch ]; then
  sed -i 's/pip/rpm/' %buildroot%python3_sitelibdir_noarch/*.dist-info/INSTALLER
fi
#%%python3_install

%files
%doc README.rst examples
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.4-alt1
- 4.3.4

* Thu Mar 12 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- 4.2.0

* Thu Sep 12 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Build new version with python3.

* Mon May 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
