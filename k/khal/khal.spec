%def_with check

Name: khal
Version: 0.14.0
Release: alt1

Summary: CLI calendar application

License: MIT
Group: Other
URL: https://pypi.org/project/khal
VCS: https://github.com/pimutils/khal

BuildArch: noarch

Source: %name-%version.tar

Requires: python3-module-vdirsyncer

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3-module-pytz python3-module-dateutil
BuildRequires: python3-module-icalendar python3-module-urwid
BuildRequires: python3-module-freezegun python3(xdg)
BuildRequires: python3-module-configobj python3-module-click-log
BuildRequires: python3-module-tzlocal python3-module-vdirsyncer
%endif

%description
Khal is a standards based CLI and terminal calendar program, able to synchronize 
with CalDAV servers through vdirsyncer.

%package -n python3-module-%name
Group:   Development/Python3
Summary: CLI calendar application
%description -n python3-module-%name
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%version"
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests -k 'not test_configure_command and not test_configure_command_create_vdir'

%files
%doc *.rst AUTHORS.txt COPYING
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Wed Mar 25 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt1
- 0.13.0 -> 0.14.0

* Mon Sep 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt2
- add requires vdirsyncer

* Sat Sep 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- Initial build for ALT Linux.
