%define oname texttemplate

Name: python3-module-%oname
Version: 0.2.0
Release: alt4

Summary: Text templating module
License: LGPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/texttemplate/
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3


%description
texttemplate converts text templates into simple Python-based object
models easily manipulated from ordinary Python code. Fast, powerful and
easy to use.

%prep
%setup
%patch0 -p2

%build
%python3_build

%install
%python3_install

%files
%doc *.txt Documentation ./Examples
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt4
- python2 disabled
- porting on python3

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt3
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.2.0-alt2.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

