%define pypi_name vbml

Name: python3-module-vbml
Version: 1.1.post1
Release: alt1

Summary: Way to check, match & resist. Sofisticated object oriented regex-based text parser

License: MIT
Group: Development/Python3
URL: https://github.com/tesseradecade/vbml
# Source-url: https://files.pythonhosted.org/packages/ba/76/8b25f75c1ee4d41118676e5f3bb97397eac7eecd68d98054ec27e07974e3/vbml-1.1.post1.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Way to check, match & resist. Sofisticated object oriented regex-based text parser.

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
%python3_sitelibdir/vbml/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.post1-alt1
- initial build for Sisyphus.

