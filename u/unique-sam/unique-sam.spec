Name: unique-sam
Version: 0.1.3
Release: alt1.git20150205
Summary: Analyse sam file and keep the unique aligment record
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/unique-sam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dlmeduLi/unique-sam.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-libsam

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
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150205
- Version 0.1.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150204
- Initial build for Sisyphus

