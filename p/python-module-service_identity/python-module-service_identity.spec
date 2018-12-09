%define  modulename service_identity

Name:    python-module-%modulename
Version: 18.1.0
Release: alt1

Summary: Service Identity Verification for Python
License: MIT
Group:   Development/Python
URL:     https://github.com/pyca/service_identity

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
service_identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Sun Dec 09 2018 Andrey Cherepanov <cas@altlinux.org> 18.1.0-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 17.0.0-alt1
- Initial build for Sisyphus
