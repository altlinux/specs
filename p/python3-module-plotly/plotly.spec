%define oname plotly

%def_disable check

Name: python3-module-%oname
Version: 1.6.6
Release: alt4

Summary: Python plotting library for collaborative, interactive, publication-quality graphs
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/plotly/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-notebook

%py3_provides %oname


%description
Use this package to make collaborative, interactive, publication-quality
graphs from Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
for i in $(find %oname -name '*.py'); do
    py.test-%_python3_version $i -vv || exit 1
done

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.6.6-alt4
- python2 disabled

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.6.6-alt3
- rebuild for python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.6-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.6.6-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt1
- Version 1.6.6

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Version 1.6.4

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

