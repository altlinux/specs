# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define  modulename bitstring

Name:    python3-module-%modulename
Version: 3.1.9
Release: alt1

Summary: A Python module to help you manage your bits
License: MIT
Group:   Development/Python3
URL:     https://github.com/scott-griffiths/bitstring

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Fri Jun 16 2023 Anton Midyukov <antohami@altlinux.org> 3.1.9-alt1
- new version
- Migration to PEP517

* Mon May 24 2021 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt3
- fix changelog

* Mon May 24 2021 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt2
- rename srpm to python3-module-bitstring
- drop python2 subpackage

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus
