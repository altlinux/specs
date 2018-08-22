%python_req_hier
%define  modulename bitstring

Name:    python-module-%modulename
Version: 3.1.5
Release: alt1

Summary: A Python module to help you manage your bits
License: MIT
Group:   Development/Python
URL:     https://github.com/scott-griffiths/bitstring

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
bitstring is a pure Python module designed to help make the creation
and analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian),
hex, octal, binary, strings or files. They can be sliced, joined,
reversed, inserted into, overwritten, etc. with simple functions or
slice notation. They can also be read from, searched and replaced,
and navigated in, similar to a file or stream.

%package -n python3-module-%modulename
Summary:  A Python module to help you manage your bits
Group: Development/Python3

%description -n python3-module-%modulename
bitstring is a pure Python module designed to help make the creation
and analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian),
hex, octal, binary, strings or files. They can be sliced, joined,
reversed, inserted into, overwritten, etc. with simple functions or
slice notation. They can also be read from, searched and replaced,
and navigated in, similar to a file or stream.

Python 3 version.

%prep
%setup -n %modulename-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename.py*
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info

%changelog
* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus
