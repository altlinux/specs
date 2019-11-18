%define module_name amqplib

Name: python3-module-%module_name
Version: 1.0.2
Release: alt3

Group: Development/Python3
License: GPLv2
Summary: Python AMQP (Advanced Message Queuing Protocol) Client library
URL: http://code.google.com/p/py-amqplib/

Source: %module_name-%version.tgz

BuildRequires(pre): rpm-build-python3


%description
Python AMQP (Advanced Message Queuing Protocol) Client library.

%prep
%setup -n %module_name-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc CHANGES LICENSE README TODO
%python3_sitelibdir/amqplib*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt2.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- build for ALT
