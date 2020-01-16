%define oname kid

Name: python3-module-%oname
Version: 0.9.6
Release: alt2

Summary: Template language for XML
License: MIT/X11
Group: Development/Python3
Url: http://www.kid-templating.org/
BuildArch: noarch

Source: %oname-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Kid is a simple template language for XML based vocabularies written
in Python. It was spawned as a result of a kinky love triangle between
XSLT, TAL, and PHP. We believe many of the best features of these
languages live on in Kid with much of the limitations and complexity
stamped out (see WhatsBorrowed and WhatsDifferent). For more info on
current and planned features and licensing information, see AboutKid.

%prep
%setup -n %oname-%version
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc README COPYING
%_bindir/kid
%_bindir/kidc
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-*.egg-info


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.6-alt2
- porting on python3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Denis Klimov <zver@altlinux.org> 0.9.6-alt1
- Initial build for ALT Linux

