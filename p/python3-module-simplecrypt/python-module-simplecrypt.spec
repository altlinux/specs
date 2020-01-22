%define  oname simplecrypt

Name:    python3-module-%oname
Version: 4.1.7
Release: alt3

Summary: Simple, secure encryption and decryption for Python
License: Public Domain
Group:   Development/Python3
URL:     https://pypi.python.org/pypi/simple-crypt

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pycrypto

Source:  %oname-%version.tar


%description
Simple Crypt encrypts and decrypts data. It has two functions, encrypt and decrypt.

%prep
%setup -n %oname-%version

%build
cd simple-crypt
%python3_build

%install
cd simple-crypt
%python3_install

%files
%doc simple-crypt/README.*
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.1.7-alt3
- Porting on Python3.

* Mon Mar 27 2017 Denis Medvedev <nbr@altlinux.org> 4.1.7-alt2
- README packed

* Mon Mar 27 2017 Denis Medvedev <nbr@altlinux.org> 4.1.7-alt1
Initial release
