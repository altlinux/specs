%define  modulename bitarray

Name:    python-module-%modulename
Version: 1.0.1
Release: alt1

Summary: efficient arrays of booleans for Python
License: PSF
Group:   Development/Python
URL:     https://github.com/ilanschnell/bitarray

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

Source:  %modulename-%version.tar

%description
This module provides an object type which efficiently represents an array
of booleans.  Bitarrays are sequence types and behave very much like usual
lists.  Eight bits are represented by one byte in a contiguous block of
memory.  The user can select between two representations; little-endian
and big-endian.  All of the functionality is implemented in C.
Methods for accessing the machine representation are provided.
This can be useful when bit level access to binary files is required,
such as portable bitmap image files (.pbm).  Also, when dealing with
compressed data which uses variable bit length encoding, you may find
this module useful.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc AUTHORS README.rst

%changelog
* Thu Aug 08 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
