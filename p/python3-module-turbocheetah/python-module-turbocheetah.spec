%define modulename turbocheetah

Name: python3-module-%modulename
Version: 1.0
Release: alt2

Summary: TurboGears support package which provides a template engine plug-in for the Cheetah templating engine
License: MIT
Group: Development/Python3
Url: http://docs.turbogears.org/TurboCheetah
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
TurboCheetah is a TurboGears support package which provides a template engine
plug-in for the Cheetah templating engine, allowing you to use Cheetah templates
with TurboGears, Buffet or other systems that support the
python.templating.engines entry point.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt1.2.2
- (NMU) rebuild with python3.6

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

