%define oname cloudpickle
%def_with python3

Name:           python-module-%oname
Version:        0.4.0
Release:        alt1
Summary:        Extended pickling support for Python objects
Group:          Development/Python
License:        BSD
URL:            https://github.com/cloudpipe/cloudpickle
BuildArch:      noarch

# https://github.com/cloudpipe/cloudpickle.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(mock) python2.7(pytest) python2.7(tornado) python2.7(curses)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(mock) python3(pytest) python3(tornado) python3(curses)
%endif

%description
cloudpickle makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library. cloudpickle is especially useful for cluster computing where
Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data. Among other things, cloudpickle
supports pickling for lambda expressions, functions and classes defined
interactively in the __main__ module.

%if_with python3
%package -n python3-module-%oname
Summary: Extended pickling support for Python objects
Group: Development/Python3

%description -n python3-module-%oname
cloudpickle makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library. cloudpickle is especially useful for cluster computing where
Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data. Among other things, cloudpickle
supports pickling for lambda expressions, functions and classes defined
interactively in the __main__ module.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
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

%check
python setup.py test

# There is one test not working with Python 3
# GH issue: https://github.com/cloudpipe/cloudpickle/issues/114
%if_with python3
pushd ../python3
python3 setup.py test ||:
popd
%endif

%files
%doc LICENSE README.md
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py?.?.egg-info

%files -n python3-module-%oname
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py?.?.egg-info

%changelog
* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt1
- Initial build for ALT.

* Wed Aug 09 2017 Lumir Balhar <lbalhar@redhat.com> - 0.3.1-1
- Initial package.
