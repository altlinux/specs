%define  oname OSlash

Name:    python3-module-%oname
Version: 0.6.3
Release: alt1

Summary: Functors, Applicatives, And Monads in Python
License: MIT
Group:   Development/Python3
URL:     https://github.com/dbrattli/OSlash

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/oslash
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Fri Apr 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus.
