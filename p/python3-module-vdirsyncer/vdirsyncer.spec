%define nameS vdirsyncer

Name: python3-module-vdirsyncer
Version: 0.20.0
Release: alt1

Summary: Synchronize calendars and contacts

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/vdirsyncer
VCS: https://github.com/pimutils/vdirsyncer

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%description
Vdirsyncer is a command-line tool for synchronizing calendars and addressbooks 
between a variety of servers and the local filesystem. The most popular usecase 
is to synchronize a server with a local folder and use a set of other programs to 
change the local events and contacts. Vdirsyncer can then synchronize those 
changes back to the server.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%nameS
%python3_sitelibdir/%nameS/
%python3_sitelibdir/%{pyproject_distinfo %nameS}/
%doc *.rst LICENSE

%changelog
* Sat Sep 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.20.0-alt1
- Initial build for ALT Linux.

