%define  modulename bitstring

Name:    python3-module-%modulename
Version: 3.1.5
Release: alt2

Summary: A Python module to help you manage your bits
License: MIT
Group:   Development/Python3
URL:     https://github.com/scott-griffiths/bitstring

Packager: Anton Midyukov <antohami@altlinux.org>

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

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info

%changelog
* Mon May 24 2021 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt2
- rename srpm to python3-module-aiofiles
- drop python2 subpackage

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus
