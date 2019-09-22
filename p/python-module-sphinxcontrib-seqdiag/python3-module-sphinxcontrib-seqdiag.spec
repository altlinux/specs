%define  modulename sphinxcontrib-seqdiag

Name:    python-module-%modulename
Version: 0.8.5
Release: alt1

Summary: A sphinx extension for embedding sequence diagram using seqdiag

License: BSD-2-Clause
Group:   Development/Python
URL:     https://github.com/blockdiag/sphinxcontrib-seqdiag

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/sphinxcontrib*
%doc *.rst

%changelog
* Sun Sep 22 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus.
