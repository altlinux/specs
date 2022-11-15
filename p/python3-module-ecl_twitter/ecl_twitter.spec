%define oname ecl_twitter

%def_without docs

Name: python3-module-%oname
Version: 1.2.2
Release: alt2.1

Summary: Easy Twitter integration for Django
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ecl_twitter/
BuildArch: noarch

# https://github.com/elmcitylabs/ECL-Twitter.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname

%description
ECL Twitter is an awesome Twitter library for Python 2.7+. It makes the
Twitter API a joy to use, and Django integration is baked in. To find
out more, read on!

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
ECL Twitter is an awesome Twitter library for Python 2.7+. It makes the
Twitter API a joy to use, and Django integration is baked in. To find
out more, read on!

This package contains pickles for %oname.
%endif

%prep
%setup
%patch0 -p1

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

%build
export DJANGO_SETTINGS_MODULE="project_name.settings"
%python3_build_debug

%install
export DJANGO_SETTINGS_MODULE="project_name.settings"
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%if_with doc
%doc docs/_build/html
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle
%endif


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.2.2-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- Porting on Python3.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20120607
- Initial build for Sisyphus

