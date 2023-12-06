%define srcname pytest-xprocess
%define modulename xprocess

#%%def_disable check

Name:    python3-module-%srcname
Version: 0.23.0
Release: alt1

Summary: Pytest plugin to manage external processes across test runs
License: MIT
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-xprocess
# URL:   https://pypi.org/project/pytest-xprocess

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_disabled check
%else
BuildRequires: /proc
BuildRequires: pytest3
BuildRequires: python3-module-psutil
%endif

BuildArch: noarch

# Source-url: %__pypi_url %srcname
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
rm -r *.egg-info

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/pytest_%modulename-%version.dist-info
%doc *.md

%changelog
* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.23.0-alt1
- new version (0.23.0) with rpmgs script

* Tue Jun 13 2023 Anton Midyukov <antohami@altlinux.org> 0.22.2-alt1
- new version (0.22.2) with rpmgs script

* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.17.1-alt1
- Initial build for Sisyphus
