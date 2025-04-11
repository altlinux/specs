%define  modulename python-markdown-math

Name:    python3-module-markdown-math
Version: 0.9
Release: alt1

Summary: Math extension for Python-Markdown
License: BSD
Group:   Development/Python3
URL:     https://github.com/mitya57/python-markdown-math

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This extension adds math formulas support to Python-Markdown.

%prep
%setup -n %modulename-%version
subst 's/^license.*/license={text="BSD-3-Clause"}/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/__pycache__/*.pyc
%python3_sitelibdir/*.py
%python3_sitelibdir/python_markdown_math-%version.dist-info

%changelog
* Fri Apr 11 2025 Andrey Cherepanov <cas@altlinux.org> 0.9-alt1
- New version.
- Use %%pyproject_build.

* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.8-alt1
- New version.

* Wed Jun 10 2020 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- New version.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- New version.

* Sun May 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- Initial build for Sisyphus
