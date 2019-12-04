%define _unpackaged_files_terminate_build 1
%define oname js.html5shiv

%def_with python3

Name: python3-module-%oname
Version: 3.7.3
Release: alt2

Summary: Fanstatic packaging of html5shiv
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.html5shiv/

# hg clone https://bitbucket.org/fanstatic/js.html5shiv
Source0: https://pypi.python.org/packages/de/dc/b051382290657f45a311681753b649e4d1670627596bc33a0e5d278cb31f/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires js


%description
This library packages html5shiv for fanstatic.

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
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.7.3-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.3-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2.2-alt1.dev0.hg20130504.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.2.2-alt1.dev0.hg20130504.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2.2-alt1.dev0.hg20130504
- Initial build for Sisyphus

