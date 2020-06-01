%define oname mkdocs

Name: python3-module-%oname
Version: 1.0.4
Release: alt3

Summary: Python tool to create HTML documentation from markdown sources
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/mkdocs/

BuildArch: noarch

Source: mkdocs-%version.tar.gz
#https://github.com/mkdocs/mkdocs/pull/687
Source1: mkdocs.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2-tests
BuildRequires: python3-module-markdown
BuildRequires: python3-module-watchdog

Requires: ghp-import.py3
Requires: python3-module-livereload

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single YAML
configuration file.

This package contains tests for %oname.

%prep
%setup -n mkdocs-%version

rm -rf mkdocs/themes/*/fonts/fontawesome-webfont.*

rm -rf mkdocs/themes/*/js/highlight.pack.js

sed -i 1d mkdocs/utils/ghp_import.py

%build
%python3_build_debug

%install
%python3_install

mkdir -p %buildroot/%_man1dir/
install -p -m 0644 %SOURCE1 %buildroot/%_man1dir/

%files
%_bindir/*
%_man1dir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/*/test*

%changelog
* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt3
- Requires fixed.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt2
- Build for python2 disabled.

* Wed Apr 24 2019 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

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

