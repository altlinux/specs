%define oname ua_parser
%def_disable check

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt2
Summary: Python port of Browserscope's user agent parser
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/ua-parser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tobie/ua-parser.git
Source: %name-%version.tar
BuildArch: noarch
%if_with python3
BuildRequires(pre): rpm-build-python3
%endif
BuildRequires: python-module-pytest python-module-yaml python-modules-json

#BuildPreReq: python-module-setuptools-tests python-module-yaml
#BuildPreReq: python-modules-json

%py_provides %oname

%description
The crux of the original parser--the data collected by Steve Souders
over the years--has been extracted into a separate YAML file so as to be
reusable as is by implementations in other programming languages.

ua-parser is just a small wrapper around this data.

%if_with python3
%package -n python3-module-%oname
Summary:        %summary
Group:          Development/Python
BuildRequires: python3-module-pytest python3-module-yaml

%description -n python3-module-%oname
The crux of the original parser--the data collected by Steve Souders
over the years--has been extracted into a separate YAML file so as to be
reusable as is by implementations in other programming languages.

ua-parser is just a small wrapper around this data.
%endif

%prep
%setup

cp -v regexes.* uap-core/
cp -v regexes.* py/ua_parser/

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug
#python setup.py sdist

%if_with python3
pushd ../python3
%python3_build_debug
#python3 setup.py sdist
popd
%endif

%install
%python_install

install -m644 py/%oname/regexes.* %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
install -m644 py/%oname/regexes.* %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
python setup.py test
rm -fR build
export PYTHONPATH=%buildroot%python_sitelibdir
py.test


%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test
popd
%endif

%files
%doc *.md *.txt *.markdown
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt2
- NMU: Updated build dependencies.

* Tue May 30 2017 Lenar Shakirov <snejok@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 0.3.4-alt3.git20141025
- Enable python3

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.4-alt2.git20141025
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20141025
- Initial build for Sisyphus

