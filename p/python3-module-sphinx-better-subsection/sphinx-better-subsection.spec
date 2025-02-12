Name: python3-module-sphinx-better-subsection

Version: 0.2
Release: alt1

Summary: Better your Sphinx section IDs 
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/sphinx-better-subsection/
Vcs: https://github.com/GeeTransit/sphinx-better-subsection

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

subst 's|[tool.hatch.version]||' pyproject.toml
subst 's|source = "vcs"||' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%exclude %python3_sitelibdir/sphinx_better_subsection-0.0.0.dist-info
%python3_sitelibdir/*


%changelog
* Wed Feb 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- Initial build for ALT Linux (git.a47a2e77)
