%define oname js.jqueryui

Name: python3-module-%oname
Version: 1.10.3
Release: alt3

Summary: fanstatic jQuery UI
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jqueryui/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3

%py3_provides %oname
%py3_requires js js.jquery

%description
This library packages jQuery UI for fanstatic. It is aware of different
modes (normal, minified).

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.3-alt3
- Build for python2 diisabled.

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.3-alt2.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.3-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.3-alt2
- Applied python-module-js.jqueryui-1.10.3-alt1.diff

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.3-alt1
- Initial build for Sisyphus

