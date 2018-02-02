%define oname docopt

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt2.1

Summary: Pythonic argument parser, that will make you smile

License: MIT
Group: File tools
Url: https://github.com/docopt/docopt

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/docopt/docopt.git
Source: %name-%version.tar

BuildArch: noarch

# buildreq add all packages :)
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-pytest
BuildRequires:  python-module-nose python-modules-json

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-nose
BuildRequires:  python3-module-pytest
%endif

%description
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%package -n python3-module-%oname
Summary: Pythonic argument parser, that will make you smile
Group: Development/Python3

%description -n python3-module-%oname
Isn't it awesome how optparse and argparse generate help messages
based on your code?!

Hell no! You know what's awesome? It's when the option parser is
generated based on the beautiful help message that you write yourself!
This way you don't need to write thisstupid repeatable parser-code,
and instead can write only the help message--*the way you want it*.

%prep
%setup

# remove upstream egg-info
rm -rf *.egg-info

%if_with python3
cp -fR . ../python3-module-%oname
%endif

%build
%python_build

%if_with python3
pushd ../python3-module-%oname
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3-module-%oname
python3 setup.py test -v
popd
%endif

%files
%python_sitelibdir/%oname.py*
%python_sitelibdir/%oname-*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt2
- Version 0.6.2 release

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt1.git20150601.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt1.git20150601.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150601
- Snapshot from git

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1
- Version 0.6.2
- Added module for Python 3

* Sat Feb 23 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Sat Feb 16 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 14 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.5.0-1
- Inital release
