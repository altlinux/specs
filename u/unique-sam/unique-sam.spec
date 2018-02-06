%define _unpackaged_files_terminate_build 1
Name: unique-sam
Version: 0.2.4
Release: alt1.1
Summary: Analyse sam file and keep the unique aligment record
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unique-sam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dlmeduLi/unique-sam.git
Source0: https://pypi.python.org/packages/03/16/51c6c02140d2ce6ab9d71615341bdb0383d0a137e790868445161f93cb9b/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-libsam

%py_provides unique_sam
%py_requires libsam

%description
Unique-Sam is a simple command line tool to remove the duplicated
alignments in the SAM file. If the MAPQ field of the alignment is
available, unique-sam will keep one and only one alignment with the
highest score. Otherwise, unique-sam will calculate a score according to
the alignment's MD or CIGAR field and use the calculated value to remove
the duplicated alignments.

%prep
%setup -q 

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst PKG-INFO
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated PyPI update

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20150206
- Version 0.1.5

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150205
- Version 0.1.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150204
- Initial build for Sisyphus

