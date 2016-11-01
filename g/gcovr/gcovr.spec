Name: gcovr
Version: 3.3
Release: alt1

Summary: Manages the compilation of coverage information from gcov
License: BSD
Group: Development/Tools

Url: https://pypi.python.org/pypi/gcovr

Source: https://pypi.python.org/packages/source/g/%name/%name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-modules python-module-distribute

%description
The gcovr command provides a utility for running the gcov command and
summarizing code coverage results. This command is inspired by the
Python coverage.py package, which provides a similar utility in
Python. Further, gcovr can be viewed as a command-line alternative of
the lcov utility, which runs gcov and generates an HTML output.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README.txt
%_bindir/gcovr
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info/

%changelog
* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Fri Dec 13 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- 3.1

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 3.0-alt1
- 2.4 -> 3.0

* Mon Sep 02 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt2
- Update Url

* Wed Aug 28 2013 Igor Zubkov <icesik@altlinux.org> 2.4-alt1
- build for Sisyphus

