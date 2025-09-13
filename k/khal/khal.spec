Name: khal
Version: 0.13.0
Release: alt1

Summary: CLI calendar application

License: MIT
Group: Other
URL: https://pypi.org/project/khal
VCS: https://github.com/pimutils/khal

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-setuptools_scm

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
install -Dm 0644 misc/%name.desktop %buildroot%_datadir/applications/%name.desktop

%files
%doc *.rst AUTHORS.txt COPYING
%_bindir/*
%_datadir/applications/%name.desktop

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Sat Sep 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- Initial build for ALT Linux.
