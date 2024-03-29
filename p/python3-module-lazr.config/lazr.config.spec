%define _unpackaged_files_terminate_build 1
%define oname lazr.config

%def_with check

Name: python3-module-%oname
Version: 3.0
Release: alt2

Summary: Create configuration schemas, and process and validate configurations
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/lazr.config
Vcs: https://git.launchpad.net/lazr.config

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-lazr.delegates
BuildRequires: python3-module-zope.testrunner
%endif

%description
The LAZR config system is typically used to manage process configuration.
Process configuration is for saying how things change when we run systems
on different machines, or under different circumstances.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.rst *.txt
%python3_sitelibdir/lazr
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests


%changelog
* Tue Jan 23 2024 Anton Vyatkin <toni@altlinux.org> 3.0-alt2
- Fix FTBFS.

* Mon Apr 10 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Wed Mar 22 2023 Anton Vyatkin <toni@altlinux.org> 2.2.3-alt1
- New version 2.2.3.

* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus
