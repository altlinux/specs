%def_enable snapshot
%define _unpackaged_files_terminate_build 1
%define pypi_name Markdown
%define modname markdown

%def_enable check

Name: python3-module-%modname
Version: 3.4.3
Release: alt1

Summary: Python implementation of Markdown text-to-HTML convertor.
Group: Development/Python3
License: BSD-3-Clause
Url: http://pypi.python.org/pypi/Markdown/

%if_disabled snapshot
Source: https://pypi.io/packages/source/M/%pypi_name/%pypi_name-%version.tar.gz
%else
Vcs: git://github.com/waylan/Python-Markdown.git
Source: Markdown-%version.tar
%endif

BuildArch: noarch

%define metadata_ver 4.4

Requires: python3-module-Pygments
#markdown/util.py:    import importlib_metadata as metadata
Requires: python3-module-importlib-metadata >= %metadata_ver

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3(wheel)
BuildRequires: python3-module-yaml
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-importlib-metadata >= %metadata_ver
%{?_enable_check:BuildRequires: python3(tox)}

%description
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains Python implementation of markdown-to-HTML convertor.

%package docs
Summary: Documentation for Markdown
Group: Development/Documentation
BuildArch: noarch

%description docs
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains documentation for Markdown.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/%{modname}_py \
	%buildroot%_bindir/%{modname}_py3

%check
%tox_check
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/%{modname}_py3 README.md >README.html

%files
%_bindir/%{modname}_py3
%python3_sitelibdir/%modname/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Thu Mar 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3
- ported to %%pyproject* macros

* Sat Jul 16 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Jul 15 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4-alt1
- 3.4

* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.7-alt1
- 3.3.7

* Thu Nov 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3.6-alt1
- 3.3.6

* Thu Nov 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1.1
- updated dependencies

* Wed Nov 17 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5

* Fri Feb 26 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3.4-alt1
- 3.3.4

* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.3.3-alt1
- updated to 3.3.3-4-g8e7528f

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Thu Feb 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Feb 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.2-alt1
- 3.2 (python3 only)
- enabled check
- fixed License tag

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Fri Apr 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.2-alt2.git20150620.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.2-alt2.git20150620
- Disabled Doc, tests and unnecessary dependents

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.git20150620
- Version 2.6.2

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150219
- Version 2.6.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.git20141119
- Version 2.5.2

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141028
- Version 2.5.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.alpha
- Version 2.4.0.alpha

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.1-alt1
- Version 2.2.1

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2
- Added explicit conflict with discount

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3 (ALT #23510)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6b-alt1.1
- Rebuilt with python 2.6

* Sun Feb 17 2008 Mikhail Gusarov <dottedmag@altlinux.org> 1.6b-alt1
- Initial build
