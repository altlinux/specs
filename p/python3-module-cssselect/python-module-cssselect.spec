%define _unpackaged_files_terminate_build 1

%def_with check

Name: python3-module-cssselect
Version: 0.9.1
Release: alt3

Summary: Parses CSS3 Selectors and translates them to XPath 1.0
Group: Development/Python3
License: BSD-style
Url: http://packages.python.org/cssselect/
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-lxml

%if_with check
BuildRequires: python3(tox)
%endif

# http://pypi.python.org/packages/source/c/cssselect/cssselect-%version.tar.gz
Source: cssselect-%version.tar

%description
Cssselect parses CSS3 Selectors and translates them to XPath 1.0
expressions.  Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document.

%prep
%setup -n cssselect-%version

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%python3_sitelibdir/*
%doc AUTHORS docs README.rst CHANGES LICENSE PKG-INFO

%changelog
* Mon Apr 26 2021 Stanislav Levin <slev@altlinux.org> 0.9.1-alt3
- Built Python3 package from its ows src.

* Wed Feb 19 2020 Stanislav Levin <slev@altlinux.org> 0.9.1-alt2
- Fixed FTBS.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1 (ALT #30204)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.1
- Added module for Python 3

* Tue May 21 2013 Dmitry V. Levin <ldv@altlinux.org> 0.8-alt1
- Initial revision.
