%define _unpackaged_files_terminate_build 1
%def_with check

Name:       rexi
Version:    1.2.0
Release:    alt1
BuildArch:  noarch

License:    MIT
Group:      Text tools
Summary:    Terminal UI for Regex Testing.

Url:        https://github.com/royreznik/rexi
Source:     %name-%version.tar
Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typer
BuildRequires: python3-module-colorama
BuildRequires: python3-module-textual
%endif

Requires:   python3-module-%name = %EVR

%description
Rexi is a simple yet powerful CLI tool designed for developers,
data scientists, and anyone interested in working with regular
expressions directly from the terminal. Built with Python and
leveraging the textual library, rexi offers a user-friendly terminal
UI to interactively work with regular expressions.

%package -n python3-module-%name
Group:      Other
Summary:    Python module for rexi.
BuildArch:  noarch

%description -n python3-module-%name
Rexi is a simple yet powerful CLI tool designed for developers,
data scientists, and anyone interested in working with regular
expressions directly from the terminal. Built with Python and
leveraging the textual library, rexi offers a user-friendly terminal
UI to interactively work with regular expressions.

Package contains python module for %name.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Thu Feb 27 2025 Sergey Savelev <medovi@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
