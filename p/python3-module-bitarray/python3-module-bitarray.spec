%define  modulename bitarray

Name:    python3-module-%modulename
Version: 2.7.3
Release: alt1

Summary: Efficient arrays of booleans for Python
License: Python
Group:   Development/Python3
Url:     https://github.com/ilanschnell/bitarray
Vcs:     https://github.com/ilanschnell/bitarray.git

Packager: Andrew A. Vasilyev <andy@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
%pyproject_build

%install
%pyproject_install

%check
make test PYTHON=%__python3

%files
%python3_sitelibdir/*
%doc LICENSE *.rst doc/*.rst

%changelog
* Wed Feb 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.7.3-alt1
- 2.7.3

* Mon Feb 13 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.7.2-alt1
- 2.7.2
- migrate to pyproject

* Sat Feb 11 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.7.1-alt1
- 2.7.1

* Wed Feb 08 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.7.0-alt1
- 2.7.0

* Mon Jan 09 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.6.2-alt1
- 2.6.2

* Thu Dec 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Jul 19 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.6.0-alt1
- 2.6.0

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.5.1-alt1
- 2.5.1

* Thu Mar 31 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.4.1-alt1
- 2.4.1

* Thu Mar 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Feb 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.3.7-alt1
- 2.3.7

* Thu Feb 10 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.3.6-alt1
- 2.3.6

* Tue Jan 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 2.3.5-alt1
- 2.3.5

* Mon Sep 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.3.4-alt1
- 2.3.4

* Mon Sep 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.3.3-alt1
- 2.3.3

* Tue Aug 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.3.2-alt1
- 2.3.2

* Sun Aug 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.2.5-alt1
- 2.2.5

* Sun Aug 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.2.4-alt1
- 2.2.4

* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon Jul 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Jun 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.1.2-alt1
- 2.1.2

* Sun Jun 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.1.1-alt1
- 2.1.1

* Fri May 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Apr 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sat Apr 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.2-alt1
- 1.9.2

* Fri Apr 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.1-alt1
- 1.9.1

* Sun Apr 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.0-alt1
- 1.9.0

* Fri Mar 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Feb 06 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Nov 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Sep 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Aug 09 2019 Andrew A. Vasilyev <andy@altlinux.org> 1.0.1-alt1
- 1.0.1-alt1

* Fri Jun 28 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus
