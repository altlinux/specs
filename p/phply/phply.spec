Name: phply
Version: 1.2.6
Release: alt1

Summary: Lexer and parser for PHP source implemented using PLY

License: BSD
Group: Development/Python
Url: https://github.com/viraptor/phply

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-ply

Requires: python3-module-%name = %version-%release

%description
phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.

%package -n python3-module-%name
Summary: Lexer and parser for PHP source implemented using PLY
Group: Development/Python3
%py3_provides phply.phpast
%py3_provides phply.phplex
%py3_provides phply.phpparse

%description -n python3-module-%name
Python 3 module for phply. phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.


%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/phplex
%_bindir/phpparse

%files -n python3-module-%name
%exclude %python3_sitelibdir/tests
%python3_sitelibdir/*-nspkg.pth
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version.dist-info

%changelog
* Fri Jan 13 2023 Vladimir Didenko <cow@altlinux.ru> 1.2.6-alt1
- new version

* Fri May 7 2021 Vladimir Didenko <cow@altlinux.ru> 1.2.5-alt3
- don't build python2 module

* Mon Sep 23 2019 Anton Farygin <rider@altlinux.ru> 1.2.5-alt2
- added missing python3 provides for modules

* Tue Mar 19 2019 Vladimir Didenko <cow@altlinux.ru> 1.2.5-alt1
- new version

* Tue Jul 17 2018 Vladimir Didenko <cow@altlinux.ru> 1.2.4-alt1
- initial build for Sisyphus
