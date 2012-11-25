Name: python3-doc
Version: 3.3.0
Release: alt1

Summary: Documentation for the Python 3 programming language
Summary(ru_RU.UTF-8): Документация по языку программирования Python.

Packager: Python Development Team <python@packages.altlinux.org>

License: PSF
Group: Development/Python
Url: http://docs.python.org/3/

BuildArch: noarch
AutoReqProv: no

Source: python-%version-docs-html.tar.bz2

%description
Documentation for the Python 3 programming language, interpreter,
and bundled module library in the HTML format.

%description -l ru_RU.UTF-8
Документация по языку программирования Python 3, его интерпретатору
и распространяемой с ним библиотеке модулей, в формате HTML.

%prep
%setup -n python-%version-docs-html

%files
%doc *

%changelog
* Mon Nov 26 2012 Fr. Br. George <george@altlinux.ru> 3.3.0-alt1
- Autobuild version bump to 3.3.0

