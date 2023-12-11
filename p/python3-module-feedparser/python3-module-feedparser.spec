%def_disable snapshot
%define pypi_name feedparser

%def_without doc
# no tests/tests in tarball
%def_disable check

Name: python3-module-%pypi_name
Version: 6.0.11
Release: alt1

Summary: Universal feed parser for Python
Group: Development/Python3
License: BSD-2-Clause
Url: https://github.com/kurtmckee/%pypi_name

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.8 python3(wheel) python3(setuptools)
%{?_with_doc:BuildRequires: python3-module-sphinx python3-module-requests}
%{?_enable_check:BuildRequires: python3(pytest) python3-module-requests}

%if_disabled snapshot
Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

%description
Universal feed parser is a Python module for downloading and parsing
syndicated feeds.  It can handle RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0, and CDF feeds.  It also parses several popular
extension modules, including Dublin Core and Apple's iTunes extensions.
It provides the same API to all formats, and sanitizes URIs and HTML.

%package doc
Summary: Documentation for the Universal feed parser for Python
Group: Development/Python
Requires: %name = %EVR

%description doc
This package contains documentation for the Universal feed parser.

%prep
%setup -n %pypi_name-%version

find -type f -print0 |
	xargs -r0 sed -i 's/\r//' --

%build
%pyproject_build
%{?_with_doc:py3_sphinx-build -b html docs html}

%install
%pyproject_install

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
install -pm644 LICENSE NEWS README.rst %buildroot%docdir/
%{?_with_doc:cp -a html %buildroot%docdir/}

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd tests
%__python3 runtests.py
popd

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%dir %docdir
%docdir/[LNR]*

%if_with doc
%files doc
%dir %docdir
%docdir/html
%endif

%changelog
* Mon Dec 11 2023 Yuri N. Sedunov <aris@altlinux.org> 6.0.11-alt1
- 6.0.11
- ported to %%pyproject* macros

* Sun May 22 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.10-alt1
- 6.0.10

* Thu May 19 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.9-alt1
- 6.0.9

* Fri Jun 25 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.8-alt1
- 6.0.8

* Thu Jun 17 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.6-alt1
- 6.0.6

* Tue Jun 15 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.5-alt1
- 6.0.5

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- 6.0.2

* Sat Sep 26 2020 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- 6.0.1

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- first build for Sisyphus

