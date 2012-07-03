Name: docs-cppreference
Version: 2009.2.17
Release: alt2
Summary: A complete reference for C++ language.

License: GPLv2+
Group: Documentation
Source0: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.png

Url: http://cppreference.com

Requires: kchmviewer

%description
The cppreference is a complete offline manual for standart library of C++
language. It includes full description of syntax and using clases of standart library

%prep
%setup 

%files
%doc cppreference.chm


%changelog
* Wed Mar 11 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 2009.2.17-alt2
- fix mistakes in spec

* Wed Feb 25 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 2009.2.17-alt1
- New version; 
- html pages have been removed from package

