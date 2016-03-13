%define sname anyjson

%def_with python3

Summary: Get the best JSON encoder/decoder available on this system
Name: python-module-%sname
Version: 0.3.3
Release: alt1.hg20120622.1
# hg clone https://bitbucket.org/runeh/anyjson
Source0: %name-%version.tar
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/anyjson/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
Convenience module to import the best available json serialize/deserializer installed.

%package -n python3-module-%sname
Summary: Get the best JSON encoder/decoder available on this system
Group: Development/Python3

%description -n python3-module-%sname
Convenience module to import the best available json serialize/deserializer installed.

%prep
%setup

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

%files
%doc README LICENSE CHANGELOG
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%sname
%doc README LICENSE CHANGELOG
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt1.hg20120622.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.hg20120622
- Version 0.3.3

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.1
- Added module for Python 3

* Thu May 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3.1-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.4-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.2.4-alt1
- initial build
