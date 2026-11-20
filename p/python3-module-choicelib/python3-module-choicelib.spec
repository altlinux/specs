%define pypi_name choicelib

Name: python3-module-choicelib
Version: 0.1.5
Release: alt1

Summary: Choice a best similar-interface library from given list

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/choicelib/
# Source-url: https://files.pythonhosted.org/packages/20/e0/3b0dd0c2dc1817c6a2c45da0928df54f8880a67cfb58aafd1f63c7a63bcc/choicelib-0.1.5.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Choice a best similar-interface library from given list.

%prep
%setup
# Use the maintained Poetry core backend.
sed -i -e 's/poetry>=0.12/poetry-core/' \
    -e 's/poetry.masonry.api/poetry.core.masonry.api/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/choicelib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- initial build for Sisyphus.

