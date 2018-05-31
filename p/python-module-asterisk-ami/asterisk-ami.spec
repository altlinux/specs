%define oname asterisk-ami
%define fname python-module-%oname
%define descr A simple Python AMI client

Name: %fname
Version: 0.1.5
Release: alt1

Summary: %descr
Group: Development/Python

License: BSD
Url: https://pypi.org/project/asterisk-ami/
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools

BuildArch: noarch

%add_python_req_skip tests.settings
%filter_from_provides /^python(tests\.integration\..*)/d
%filter_from_provides /^python(tests\.unit\.test_ami_client)/d

%description
%descr

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus (Closes: #33963).
