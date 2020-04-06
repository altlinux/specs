%define oname js.query

Name: python3-module-%oname
Version: 1.9.2
Release: alt2

Summary: fanstatic jQuery
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jquery/

# hg clone https://bitbucket.org/fanstatic/js.jquery
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js

%description
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

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
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.2-alt2
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1.dev0.hg20130303.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.dev0.hg20130303.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.dev0.hg20130303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1.dev0.hg20130303
- Initial build for Sisyphus

