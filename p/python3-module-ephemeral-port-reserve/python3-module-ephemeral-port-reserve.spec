%define _unpackaged_files_terminate_build 1
%define pypi_name ephemeral-port-reserve
%define mod_name ephemeral_port_reserve

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.4
Release: alt1

Summary: Find an unused port, reliably
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ephemeral-port-reserve/
Vcs: https://github.com/Yelp/ephemeral-port-reserve

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Sometimes you need a networked program to bind to a port that can't be
hard-coded. Generally this is when you want to run several of them
in parallel; if they all bind to port 8080, only one of them can succeed.

The usual solution is the "port 0 trick". If you bind to port 0, your
kernel will find some arbitrary high-numbered port that's unused and
bind to that. Afterward you can query the actual port that was bound
to if you need to use the port number elsewhere. However, there are
cases where the port 0 trick won't work. For example, mysqld takes
port 0 to mean "the port configured in my.cnf". Docker can bind your
containers to port 0, but uses its own implementation to find a free
port which races and fails in the face of parallelism.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.4-alt1
- Built for ALT Sisyphus.

