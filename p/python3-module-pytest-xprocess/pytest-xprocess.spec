%define  srcname pytest-xprocess

# needed /proc/1/stat
%def_disable check

Name:    python3-module-%srcname
Version: 0.17.1
Release: alt1

Summary: Pytest plugin to manage external processes across test runs
License: MIT
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-xprocess
# URL:   https://pypi.org/project/pytest-xprocess

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-psutil
%endif

BuildArch: noarch

Source: %srcname-%version.tar

%description
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...

%prep
%setup -n %srcname-%version
# Remove bundled egg-info
rm -rf *.egg-info
# Remove executable bit from README
chmod -x README.rst

%build
%python3_build

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.md

%changelog
* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.17.1-alt1
- Initial build for Sisyphus
