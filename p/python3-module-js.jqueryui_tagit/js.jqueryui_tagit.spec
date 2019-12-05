%define oname js.jqueryui_tagit

Name: python3-module-%oname
Version: 2.0.24.2
Release: alt2

Summary: Fanstatic packaging of Tag-it!
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jqueryui_tagit/

# https://github.com/Kotti/js.jqueryui_tagit.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js js.jqueryui


%description
This library packages Tag-it! for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.24.2-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.24.2-alt1.git20130509.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.24.2-alt1.git20130509.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.24.2-alt1.git20130509.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.24.2-alt1.git20130509
- Initial build for Sisyphus

