%define oname llist

Name: python3-module-%oname
Version: 0.4
Release: alt2

Summary: Linked list data structures for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/llist/

# https://github.com/ajakubek/python-llist.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python-tools-2to3

%py3_provides %oname


%description
llist is an extension module for CPython providing basic linked list
data structures. Collections implemented in the llist module perform
well in problems which rely on fast insertions and/or deletions of
elements in the middle of a sequence. For this kind of workload, they
can be significantly faster than collections.deque or standard Python
lists.

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%add_optflags -fno-strict-aliasing

%python3_build_debug

%install
%python3_install

%check
%if 0
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
%endif

%files
%doc CHANGES README docs/*.rst examples
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt1.git20130101.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20130101.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20130101.1
- NMU: Use buildreq for BR.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130101
- Initial build for Sisyphus

