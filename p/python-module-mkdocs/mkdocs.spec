%define oname mkdocs

%def_with python3

Name: python-module-%oname
Version: 0.16.1
Release: alt1.1
Summary: Python tool to create HTML documentation from markdown sources
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mkdocs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
#https://github.com/mkdocs/mkdocs/pull/687
Source1:        mkdocs.1
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-jinja2 python-module-markdown
#BuildPreReq: python-module-yaml python-module-watchdog
#BuildPreReq: ghp-import python-module-argh python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-jinja2 python3-module-markdown
#BuildPreReq: python3-module-yaml python3-module-watchdog
#BuildPreReq: ghp-import.py3 python3-module-argh
%endif

%py_provides %oname
Requires: ghp-import

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2-tests python-module-markupsafe python-module-pathtools python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python3 python3-base python3-module-jinja2 python3-module-markupsafe python3-module-pathtools python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-jinja2 python-module-markdown python-module-setuptools python-module-watchdog python-modules-json python3-module-jinja2-tests python3-module-markdown python3-module-setuptools python3-module-watchdog rpm-build-python3

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Project documentation with Markdown
Group: Development/Python3
%py3_provides %oname
Requires: ghp-import.py3

%description -n python3-module-%oname
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

rm -rf mkdocs/themes/*/fonts/fontawesome-webfont.*

rm -rf mkdocs/themes/*/js/highlight.pack.js

sed -i 1d mkdocs/utils/ghp_import.py


%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

mkdir -p %buildroot/%_man1dir/
install -p -m 0644 %SOURCE1 %buildroot/%_man1dir/

%files
%_bindir/*
%_man1dir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.1-alt1.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

