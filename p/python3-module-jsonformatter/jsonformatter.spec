%def_without bootstrap

%def_with check

%define oname jsonformatter

Name: python3-module-jsonformatter
Version: 0.3.4
Release: alt1

Summary: Easily customize LogRecord attributes

License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/jsonformatter/
VCS: https://github.com/MyColorfulDays/jsonformatter

Source: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: rpm-build-python3
BuildRequires: python3-module-build
BuildRequires: python3-module-installer
BuildRequires: python3-module-pyproject-installer

BuildArch: noarch

%description
jsonformatter is a Python library that allows you to easily customize 
and replace LogRecord attributes.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%pyproject_build

%install
%pyproject_install

# Диагностика для определения точного пути
echo "=== Поиск установленных файлов ==="
find %buildroot -name "jsonformatter*" -type d 2>/dev/null | sort
echo "=== Содержимое site-packages ==="
find %buildroot -path "*/site-packages/*" -type d 2>/dev/null | sort

%check
export LC_ALL=en_US.UTF-8

%files
# Явно указываем пути, которые показала диагностика
# Скорее всего это будет один из этих вариантов:
%python3_sitelibdir/jsonformatter/
%python3_sitelibdir/jsonformatter-0.3.4.dist-info/

%changelog
* Tue Feb 17 2026 Pavel Vasenkov <pav@altlinux.org> 0.3.4-alt1
- New build for sisyphus
