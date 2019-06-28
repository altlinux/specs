%define  modulename bitarray

Name:    python3-module-%modulename
Version: 0.9.3
Release: alt1

Summary: efficient arrays of booleans for Python
License: PSF
Group:   Development/Python3
URL:     https://github.com/ilanschnell/bitarray

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source:  %modulename-%version.tar

%description
======================================
bitarray: efficient arrays of booleans
======================================

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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc AUTHORS README.rst

%changelog
* Fri Jun 28 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
