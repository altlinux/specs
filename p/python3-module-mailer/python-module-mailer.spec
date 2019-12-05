%define modname mailer

Name: python3-module-%modname
Version: 0.8.1
Release: alt2

Summary: A module to send email simply in Python
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/%modname/
BuildArch: noarch

# hg clone https://bitbucket.org/ginstrom/mailer
Source: mailer-%version.tgz
Patch0: fix-import-according-with-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
A module that simplifies sending email.

%prep
%setup -n mailer-%version
%patch0 -p2

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html
mkdir man
cp -fR docs/build/html/* man/

%files
%doc README.md LICENSE.txt man/
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt2
- porting on python3

* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.hg20140606.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.hg20140606.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.hg20140606
- Version 0.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Thu Jul 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- initial build
