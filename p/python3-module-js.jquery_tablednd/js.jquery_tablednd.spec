%define oname js.jquery_tablednd

Name: python3-module-%oname
Version: 0.4
Release: alt2

Summary: Fanstatic packaging of jQuery TableDND
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jquery_tablednd/

# https://github.com/disko/js.jquery_tablednd.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js js.jquery


%description
This library packages jQuery TableDND for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR js/jquery_tablednd/resources \
    %buildroot%python3_sitelibdir/js/jquery_tablednd/

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4-alt1.git20130222.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20130222.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20130222.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130222
- Initial build for Sisyphus

