%define  modulename simplecrypt

Name:    python-module-%modulename
Version: 4.1.7
Release: alt2

Summary: Simple, secure encryption and decryption for Python
License: Public Domain
Group:   Development/Python
URL:     https://pypi.python.org/pypi/simple-crypt


BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-pycrypto

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Simple Crypt encrypts and decrypts data. It has two functions, encrypt and decrypt.

%prep
%setup -n %modulename-%version

%build
cd simple-crypt
%python_build

%install
cd simple-crypt
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc simple-crypt/README.*


%changelog
* Mon Mar 27 2017 Denis Medvedev <nbr@altlinux.org> 4.1.7-alt2
- README packed

* Mon Mar 27 2017 Denis Medvedev <nbr@altlinux.org> 4.1.7-alt1
Initial release
