%define _unpackaged_files_terminate_build 1

%define oname js.jquery_timepicker_addon

Name: python3-module-%oname
Version: 1.5.3
Release: alt2

Summary: Fanstatic packaging of jQuery-Timepicker-Addon
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.jquery_timepicker_addon/

Source0: https://pypi.python.org/packages/34/e5/d9b910b937a521710cb629759171466813052b989e45d2d3eba69d202800/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js js.jqueryui


%description
This library packages jQuery-Timepicker-Addon for fanstatic.

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
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.3-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

