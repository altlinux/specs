%define modulename mailer

%def_with python3

Name: python-module-mailer
Version: 0.7
Release: alt1.hg20140606

Summary: A module to send email simply in Python

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modulename/

Packager: Mikhail A Pokidko <pma@altlinux.ru>

BuildArch: noarch

# hg clone https://bitbucket.org/ginstrom/mailer
Source: %name-%version.tar

#setup_python_module %modulename

# Automatically added by buildreq on Thu Mar 11 2010
BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
A module that simplifies sending email.

%package -n python3-module-%modulename
Summary: A module to send email simply in Python
Group: Development/Python3

%description -n python3-module-%modulename
A module that simplifies sending email.

%prep
%setup
rm -fR build

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc docs/build/html/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc docs/build/html/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.hg20140606
- Version 0.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Thu Jul 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- initial build

