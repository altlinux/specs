%define oname flask-appconfig
%define modname flask_appconfig

Name: python3-module-%oname
Version: 0.11.1
Release: alt1

Summary: Configures Flask applications in a canonical way.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/flask-appconfig/
BuildArch: noarch

# https://github.com/mbr/flask-appconfig/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-click

%py3_requires flask
%py3_provides %modname


%description
Configures Flask applications in a canonical way. Also auto-configures Heroku.
Aims to standardize configuration.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Configures Flask applications in a canonical way. Also auto-configures Heroku.
Aims to standardize configuration.

This package contains pickles for %oname.

%package tests
Summary: Documentation for %oname
Group: Development/Python3
BuildArch: noarch

%description tests
Configures Flask applications in a canonical way. Also auto-configures Heroku.
Aims to standardize configuration.

This package contains tests for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%modname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%modname/

mv tests/ %buildroot%python3_sitelibdir/%modname/

%check
%__python3 setup.py test

%files
%doc README.rst LICENSE
%python3_sitelibdir/flask_appconfig
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.11.1-alt1
- Initial build.

