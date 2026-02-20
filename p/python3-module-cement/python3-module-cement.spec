%define pypi_name cement

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.14
Release: alt3

Summary: Application Framework for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://builtoncement.com/
Vcs: https://github.com/datafolklabs/cement

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend

# remove todo-tutorial to avoid tinydb dependency
%add_findreq_skiplist %python3_sitelibdir/%pypi_name/cli/templates/generate/todo-tutorial/*

%if_with check
BuildRequires: python3-module-mock
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pypng
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-ruff
BuildRequires: python3-module-colorlog
BuildRequires: python3-module-watchdog
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-redis
BuildRequires: python3-module-pylibmc
BuildRequires: python3-module-pystache
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-requests
%endif

%description
Cement is an advanced and flexible Python framework designed
for building command-line applications. It provides essential
features such as argument parsing, configuration management,
logging, plugin architecture, and much more to streamline the
development of CLI tools.

%prep
%setup

# Breaks https://peps.python.org/pep-0621/
sed -i 's/, "README"//' pyproject.toml

if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
# - "tests/ext/test_ext_smtp.py" requires a running SMTP server (Mailpit).
# - "tests/ext/test_ext_memcached.py" requires a running Memcached server.
# - "tests/ext/test_ext_redis.py" requires a running Redis server.
%pyproject_run_pytest -vra \
	--deselect "tests/ext/test_ext_redis.py" \
	--deselect "tests/ext/test_ext_smtp.py" \
	--deselect "tests/ext/test_ext_memcached.py" \
	tests

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/CHANGELOG.md
%exclude %python3_sitelibdir/CONTRIBUTORS.md
%doc README.* LICENSE

%changelog
* Fri Feb 20 2026 Grigory Ustinov <grenka@altlinux.org> 3.0.14-alt3
- Fixed FTBFS.

* Sat Nov 01 2025 Grigory Ustinov <grenka@altlinux.org> 3.0.14-alt2
- Fixed FTBFS.

* Wed May 07 2025 Denis Sergeev <zeff@altlinux.org> 3.0.14-alt1
- 3.0.12 -> 3.0.14.

* Mon Jan 27 2025 Denis Sergeev <zeff@altlinux.org> 3.0.12-alt1
- Initial build for Sisyphus.
