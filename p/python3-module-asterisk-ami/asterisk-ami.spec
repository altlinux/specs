%define oname asterisk-ami
%define descr A simple Python AMI client

Name: python3-module-%oname
Version: 0.1.7
Release: alt1

Summary: %descr
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/asterisk-ami
VCS: https://github.com/ettoreleandrotognoli/python-ami
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%add_python3_req_skip tests.settings
%filter_from_provides /^python3(tests\.integration\..*)/d
%filter_from_provides /^python3(tests\.unit\.test_ami_client)/d

%description
%descr

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/asterisk
%python3_sitelibdir/asterisk_ami-%version.dist-info

%changelog
* Thu May 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.1.7-alt1
- Build new version.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt3
- Fixed installation.

* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- Build for Python2 disabled.

* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus (Closes: #33963).
