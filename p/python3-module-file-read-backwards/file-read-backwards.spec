%define oname file-read-backwards

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Memory efficient way of reading files line-by-line from the end of file

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/file-read-backwards

# Source-url: https://pypi.io/packages/source/f/file_read_backwards/file_read_backwards-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-mock

%description
Memory efficient way of reading files line-by-line from the end of file.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Sisyphus
