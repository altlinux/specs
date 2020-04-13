%global oname jsonpath-rw

Name: python3-module-%oname
Version: 1.4.0
Release: alt3

Summary: Extended implementation of JSONPath for Python
License: ASL 2.0
Group: Development/Python
Url: https://github.com/kennknowles/python-jsonpath-rw

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-ply
BuildRequires: python3-module-decorator
BuildRequires: python3-module-six

Conflicts: python-module-%oname

%description
This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming. It is tested with
Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%package doc
Summary: Documentation for %name
Group:  Development/Documentation

%description doc
Documentation for %name.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python3_sitelibdir/*
%_bindir/jsonpath.py

%changelog
* Mon Apr 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt3
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2.qa1
- NMU: applied repocop patch

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt2
- Updated dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0
- cleanup spec
- delete tests from package

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.3-alt1
- First build for ALT (based on Fedora 1.2.3-4.fc21.src)

