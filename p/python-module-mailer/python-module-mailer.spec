%define modname mailer

Name: python-module-%modname
Version: 0.8.1
Release: alt1

Summary: A module to send email simply in Python
License: MIT
Group: Development/Python

Url: http://pypi.python.org/pypi/%modname/
# hg clone https://bitbucket.org/ginstrom/mailer
Packager: Mikhail A Pokidko <pma@altlinux.ru>
BuildArch: noarch

Source: mailer-%version.tgz

BuildRequires: python-module-setuptools
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
BuildRequires: time

BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base


%description
A module that simplifies sending email.

%package -n python3-module-%modname
Summary: A module to send email simply in Python
Group: Development/Python3
%add_python3_req_skip Queue

%description -n python3-module-%modname
A module that simplifies sending email.

%prep
%setup -n mailer-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html
mkdir man
cp -fR docs/build/html/* man/

%files
%doc README.md LICENSE.txt man/
%python_sitelibdir/*

%files -n python3-module-%modname
%doc README.md LICENSE.txt man/
%python3_sitelibdir/*


%changelog
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
