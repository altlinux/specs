%define modulename turbocheetah

%def_with python3

Name: python-module-%modulename
Version: 1.0
Release: alt1.2.1

Summary: TurboGears support package which provides a template engine plug-in for the Cheetah templating engine
License: MIT
Group: Development/Python

Url: http://docs.turbogears.org/TurboCheetah
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %modulename

%description
TurboCheetah is a TurboGears support package which provides a template engine
plug-in for the Cheetah templating engine, allowing you to use Cheetah templates
with TurboGears, Buffet or other systems that support the
python.templating.engines entry point.

%package -n python3-module-%modulename
Summary: TurboGears support package which provides a template engine plug-in for the Cheetah templating engine
Group: Development/Python3

%description -n python3-module-%modulename
TurboCheetah is a TurboGears support package which provides a template engine
plug-in for the Cheetah templating engine, allowing you to use Cheetah templates
with TurboGears, Buffet or other systems that support the
python.templating.engines entry point.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc *.txt
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with python 2.6

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

