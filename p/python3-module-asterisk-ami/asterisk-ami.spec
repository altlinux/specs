%define oname asterisk-ami
%define descr A simple Python AMI client

Name: python3-module-%oname
Version: 0.1.5
Release: alt3

Summary: %descr
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/asterisk-ami/
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

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

# don't install tests in such directory please
rm -rf %buildroot%python3_sitelibdir/tests

# seriously? why did they do this?
rm -f %buildroot/%_prefix/requirements.txt

%files
%doc README.rst
%python3_sitelibdir/asterisk
%python3_sitelibdir/*.egg-info

%changelog
* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt3
- Fixed installation.

* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- Build for Python2 disabled.

* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus (Closes: #33963).
