%define oname argcomplete

%def_with python3

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20141109.1.1.1
Summary: Bash tab completion for argparse
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/argcomplete/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kislyuk/argcomplete.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-argparse
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-argparse
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%package -n python3-module-%oname
Summary: Bash tab completion for argparse
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

It makes two assumptions:

* You're using bash or zsh as your shell
* You're using argparse to manage your command line arguments/options

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
python setup.py test
python test/test.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 test/test.py
popd
%endif

%files
%doc *.rst docs/*.rst docs/examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.git20141109.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20141109.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20141109.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20141109
- Version 0.8.3

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20141103
- Version 0.8.2
- Enabled testing

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141005
- Initial build for Sisyphus

