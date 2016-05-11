%define _unpackaged_files_terminate_build 1

Name: custodia
Version: 0.1.0
Release: alt1
Summary:  A service to manage, retrieve and store secrets for other processes

Group: System/Configuration/Other
License: %gpl3plus
Url: https://github.com/latchset/custodia

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Patch from upstream.
# Must be dropped when new version will be relesead.
Patch1: 0001-Allow-tox-to-use-locally-installed-packages.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools

Requires: python-module-%name = %version-%release

%setup_python_module %name

%description
%summary

%package -n python-module-%name
Summary: Subpackage with python custodia modules
Group: Development/Python

%description -n python-module-%name
%summary

%prep
%setup
#patch -p1
%patch1 -p1

%build
%python_build

%install
%python_install

%files
%_defaultdocdir/%name/
%_bindir/*
%_man7dir/*

%files -n python-module-%name
%python_sitelibdir/*

%exclude %python_sitelibdir/tests/

%changelog
* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Allow tox to use locally installed packages (patch from upstream).
- Initial build.

