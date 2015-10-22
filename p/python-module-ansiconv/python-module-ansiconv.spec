Name: python-module-ansiconv
Version: 1.0.0
Release: alt1
Summary: A Python module for converting ANSI coded text and converts it to either plain text or HTML

Group: Text tools
License: MIT
Url: https://bitbucket.org/dhrrgn/ansiconv
Source0: %name-%version.tar

BuildRequires: python-module-setuptools-tests
BuildArch: noarch

%description
A Python module for converting ANSI coded text and converts it to either plain text or HTML.

Documentation: http://pythonhosted.org/ansiconv/

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/ansiconv*
%doc README.md

%changelog
* Wed Oct 21 2015 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- v1.0.0-3-g8a7d68e
