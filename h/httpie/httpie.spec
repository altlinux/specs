%define py3bdir ../%name-%version-python3-build

%def_with python3

Name: httpie
Version: 0.8.0
Release: alt1.1
Summary: A Curl-like tool for humans

Group: Networking/WWW
License: BSD
Url: http://httpie.org
Source0: %name-%version.tar
BuildRequires: python-dev python-module-Pygments python-module-requests help2man python-module-setuptools rpm-build-python python-modules-json
BuildArch: noarch

%if_with python3
BuildRequires: python3-dev python3-module-Pygments python3-module-requests rpm-build-python3
%endif

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%if_with python3
%package -n httpie-python3
Summary: A Curl-like tool for humans
Group: Networking/WWW

%description -n httpie-python3
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.
%endif

%prep
%setup
sed -i '/#!\/usr\/bin\/env/d' %name/__main__.py

%if_with python3
rm -rf %py3bdir
cp -a . %py3bdir
%endif

%build
python setup.py build

%if_with python3
pushd %py3bdir
python3 setup.py build
popd
%endif

%install
%if_with python3
pushd %py3bdir
python3 setup.py install --skip-build --root %buildroot
mv %buildroot%_bindir/http %buildroot%_bindir/http.python3
popd
%endif

python setup.py install --root %buildroot

mkdir -p %buildroot/%_man1dir
export PYTHONPATH=%buildroot%python_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http > %buildroot/%_man1dir/http.1

%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http.python3 > %buildroot/%_man1dir/http.python3.1
%endif

%files
%_bindir/http
%python_sitelibdir/%name
%python_sitelibdir/%name-%{version}*
%_man1dir/http.1.*
%doc LICENSE README.rst

%if_with python3
%files -n httpie-python3
%_bindir/http.python3
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%{version}*
%_man1dir/http.python3.1.*
%doc LICENSE README.rst
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Sep  6 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux Sisyphus
