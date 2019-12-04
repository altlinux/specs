%define _unpackaged_files_terminate_build 1
%define oname js.tinymce

Name: python3-module-%oname
Version: 4.2.7
Release: alt2

Summary: Fanstatic packaging of TinyMCE
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.tinymce/

Source0: https://pypi.python.org/packages/8b/8c/a6c5f15e903dcdb6e2aeb33fffd85a8b4ba0722f3a11b19227b7d747678e/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js


%description
This library packages TinyMCE for fanstatic.

%prep
%setup -q -n %{oname}-%{version}

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
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.7-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.7-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.28-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.28-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.28-alt1
- Initial build for Sisyphus

