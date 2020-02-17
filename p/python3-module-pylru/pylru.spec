%define _unpackaged_files_terminate_build 1
%define oname pylru

Name:       python3-module-%oname
Version:    1.0.9
Release:    alt2

Summary:    A least recently used (LRU) cache implementation
License:    GPL
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/pylru/

BuildArch:  noarch

# https://github.com/jlhutch/pylru.git
Source0: https://pypi.python.org/packages/c0/7d/0de1055632f3871dfeaabe5a3f0510317cd98b93e7b792b44e4c7de2b17b/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
Pylru implements a true LRU cache along with several support classes.
The cache is efficient and written in pure Python. It works with Python
2.6+ including the new 3.x series. Basic operations (lookup, insert,
delete) all run in a constant amount of time.


%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.9-alt2
- Build for python2 disabled.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt1.git20141014.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1.git20141014.1
- NMU: Use buildreq for BR.

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20141014
- Initial build for Sisyphus

