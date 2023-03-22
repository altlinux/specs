%define _unpackaged_files_terminate_build 1
%define oname lazr.config

Name: python3-module-%oname
Version: 2.2.3
Release: alt1

Summary: Create configuration schemas, and process and validate configurations
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/lazr.config
Vcs: https://git.launchpad.net/lazr.config

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
The LAZR config system is typically used to manage process configuration.
Process configuration is for saying how things change when we run systems
on different machines, or under different circumstances.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst *.txt
%python3_sitelibdir/lazr
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests


%changelog
* Wed Mar 22 2023 Anton Vyatkin <toni@altlinux.org> 2.2.3-alt1
- New version 2.2.3.

* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus
