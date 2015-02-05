%define oname bespin

%def_with python3

Name: python-module-%oname
Version: 0.4.8.1
Release: alt1.git20150205
Summary: Opinionated wrapper around boto that reads yaml
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bespin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/realestate-com-au/bespin.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-delfick_error python-module-option_merge
BuildPreReq: python-module-input_algorithms python-module-argparse
BuildPreReq: python-module-six python-module-humanize
BuildPreReq: python-module-boto python-module-yaml
BuildPreReq: python-module-rainbow_logging_handler
BuildPreReq: python-module-filechunkio python-module-noseOfYeti
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-requests python-modules-json
BuildPreReq: python-module-pytz python-module-radssh
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-delfick_error python3-module-option_merge
BuildPreReq: python3-module-input_algorithms python3-module-argparse
BuildPreReq: python3-module-six python3-module-humanize
BuildPreReq: python3-module-boto python3-module-yaml
BuildPreReq: python3-module-rainbow_logging_handler
BuildPreReq: python3-module-filechunkio python3-module-noseOfYeti
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-pytz python3-module-radssh
%endif

%py_provides %oname
%py_requires delfick_error option_merge input_algorithms argparse json
%py_requires six humanize boto yaml rainbow_logging_handler filechunkio
%py_requires requests pytz radssh

%description
An opinionated wrapper around the boto API that knows how to read yaml
files and make things happen.

%package -n python3-module-%oname
Summary: Opinionated wrapper around boto that reads yaml
Group: Development/Python3
%py3_provides %oname
%py3_requires delfick_error option_merge input_algorithms argparse
%py3_requires six humanize boto yaml rainbow_logging_handler filechunkio
%py3_requires requests pytz radssh

%description -n python3-module-%oname
An opinionated wrapper around the boto API that knows how to read yaml
files and make things happen.

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
python setup.py test
./test.sh -v
%if_with python3
pushd ../python3
python3 setup.py test
#sed -i 's|nosetests|nosetests3|' test.sh
#./test.sh -v
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8.1-alt1.git20150205
- Version 0.4.8.1

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6.8-alt1.git20150203
- Version 0.4.6.8

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150119
- Version 0.4.3

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150119
- Version 0.4.1

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150116
- Initial build for Sisyphus

