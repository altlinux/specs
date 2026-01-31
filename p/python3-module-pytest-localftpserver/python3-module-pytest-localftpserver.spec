%define modname pytest-localftpserver
%define pypi_name pytest_localftpserver

# docutils<0.22,>=0.20
%def_disable check

Name: python3-module-%modname
Version: 1.5.0
Release: alt1

Summary: PyTest FTP Server
License: Apache-2.0 and MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%modname

Vcs: https://github.com/oz123/pytest-localftpserver.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools) python3(setuptools_scm)
%{?_enable_check:
BuildRequires: python3(tox) python3(pytest) python3(pyftpdlib)
BuildRequires: python3(PyOpenSSL) python3(cryptography)
BuildRequires: python3(flake8) python3(coverage)}

%description
A PyTest plugin which provides an FTP fixture for your tests.

%prep
%setup -n %pypi_name-%version
sed -i '/bump2version/d
        /sphinx-copybutton/d
        s/tox==/tox>=/' requirements_dev.txt
%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* LICENSE HISTORY*

%changelog
* Sat Jan 31 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- first build for Sisyphus


