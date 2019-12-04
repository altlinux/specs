%define oname hachibee_sphinx_theme

Name: python3-module-%oname
Version: 0.2.5
Release: alt3

Summary: A simple sphinx theme
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/hachibee-sphinx-theme/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python-tools-2to3

%py3_provides %oname


%description
Sphinx hachibee theme.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt3
- python2 disabled

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

