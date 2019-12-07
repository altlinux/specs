%define py3bdir ../%name-%version-python3-build
%define realversion 0.9.8

Name: httpie
Version: 0.9.9
Release: alt2

Summary: A Curl-like tool for humans
Group: Networking/WWW
License: BSD
Url: http://httpie.org
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-system-urllib3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-Pygments python3-module-requests
BuildRequires: help2man

Requires: python3-module-requests >= 2.11.0
Requires: python3-module-Pygments >= 2.1.3


%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep
%setup
%patch0 -p0

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%__python3 setup.py build

%install
%__python3 setup.py install --skip-build --root %buildroot
mv %buildroot%_bindir/http %buildroot%_bindir/http.python3

mkdir -p %buildroot/%_man1dir

export PYTHONPATH=%buildroot%python3_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http.python3 > %buildroot/%_man1dir/http.python3.1

%files
%_bindir/http.python3
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%{realversion}*
%_man1dir/http.python3.1.*
%doc LICENSE README.rst


%changelog
* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.9-alt2
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Terechkov Evgenii <evg@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt3
- Fixed FTBFS (Add BR python3-module-setuptools).

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt2
- Update requires
- Added patch - fixed import 'urllib3'

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt1
- Build new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Sep  6 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux Sisyphus
