%global modname oauthlib
%def_with python3

Name:               python-module-oauthlib
Version:            0.7.2
Release:            alt1
Summary:            An implementation of the OAuth request-signing logic

Group:              Development/Python
License:            BSD
URL:                http://pypi.python.org/pypi/oauthlib
Source0:            %{name}-%{version}.tar
# python-unittest2 is now provided by "python" package and python-unittest is retired
#  adapt setup.py to reflect this fact downstream
Patch0:             python-oauthlib-dont-require-unittest2.patch

BuildArch:          noarch

BuildRequires:      python-devel python-module-pytest
BuildRequires:      python-module-setuptools

BuildRequires:      python-module-nose
BuildRequires:      python-module-unittest2
BuildRequires:      python-module-mock

BuildRequires:      python-module-Crypto >= 2.6
Requires:           python-module-Crypto >= 2.6

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%if_with python3
%package -n python3-module-%{modname}
Summary:        An implementation of the OAuth request-signing logic
Group:		Development/Python3
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-pytest
BuildRequires:  python3-module-setuptools

BuildRequires:  python3-module-nose
BuildRequires:  python3-module-unittest2
BuildRequires:  python3-module-mock

BuildRequires:  python3-module-Crypto >= 2.6
Requires:       python3-module-Crypto >= 2.6

%description -n python3-module-%{modname}
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft
OAuth client support onto your favorite HTTP library, or provider support
onto your favourite web framework. If you're a maintainer of such a
library, write a thin veneer on top of OAuthLib and get OAuth support for
very little effort.

%endif

%prep
%setup

%patch0 -p2

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Make sure that setuptools knows to pick up the correct version of
# python-crypto on epel/rhel...
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"pycrypto>=2.6\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

%if_with python3
cp -fR . ../python3
%endif

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
# %check
# %__python setup.py test

%files
%doc README.rst LICENSE
%{python_sitelibdir}/%{modname}/
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-%modname
%doc README.rst LICENSE
%{python3_sitelibdir}/%{modname}/
%{python3_sitelibdir}/%{modname}-%{version}*
%endif

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.3-alt1
- Version 0.6.3

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1
- Added module for Python 3

* Fri Jul 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.6.0-alt1
- First build for ALT (based on Fedora 0.6.0-6.fc21.src)

