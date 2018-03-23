%define oname asterisk-ami
%define fname python3-module-%oname
%define descr A simple Python AMI client

Name: %fname
Version: 0.1.5
Release: alt1

Summary: %descr
Group: Development/Python3

License: BSD
Url: https://pypi.org/project/asterisk-ami/
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

BuildArch: noarch

%add_python3_req_skip tests.settings
%filter_from_provides /^python3(tests\.integration\..*)/d
%filter_from_provides /^python3(tests\.unit\.test_ami_client)/d

%description
%descr

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus (Closes: #33963).
