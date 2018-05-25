%define  modulename python-markdown-math

Name:    python3-module-markdown-math
Version: 0.5
Release: alt1

Summary: Math extension for Python-Markdown
License: BSD
Group:   Development/Python3
URL:     https://github.com/mitya57/python-markdown-math

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This extension adds math formulas support to Python-Markdown.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/__pycache__/*.pyc
%python3_sitelibdir/*.py
%python3_sitelibdir/*.egg-info

%changelog
* Sun May 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- Initial build for Sisyphus
