%define  modulename vulture

%def_with check

Name:    python3-module-%modulename
Version: 2.4
Release: alt1.1

Summary: Find dead Python code
License: MIT
Group:   Development/Python3
URL:     https://github.com/jendrikseipp/vulture

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-toml
%endif

BuildArch: noarch

Source:  %name-%version.tar

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%modulename/whitelists/whitelist_utils.py


%description
Vulture finds unused classes, functions and variables in your code.
This helps you cleanup and find errors in your programs. If you run it
on both your library and test suite you can find untested code.
Due to Python's dynamic nature, static code analyzers like vulture
are likely to miss some dead code. Also, code that is only called
implicitly may be reported as unused. Nonetheless, vulture can be a
very helpful tool for higher code quality.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -v tests

%files
%_bindir/*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.4-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue May 24 2022 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Initial build for Sisyphus
