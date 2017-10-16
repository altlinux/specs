%define oname plaster

%def_with python3


Name: python-module-%oname
Version: 1.0
Release: alt1
BuildArch: noarch
License: MIT
Group: Development/Python
Summary: Application configuration settings abstraction layer
URL:     https://github.com/Pylons/%{oname}

# https://github.com/Pylons/plaster.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(pytest)
BuildRequires: python-module-sphinx python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(pytest)
%endif

%description
plaster is a loader interface around multiple
configuration file formats. It exists to define a common API for
applications to use when they wish to load configuration. The library
itself does not aim to handle anything except a basic API that
applications may use to find and load configuration settings. Any
specific constraints should be implemented in a loader which can be
registered via an entry point.

%package doc
Summary: Documentation for python-module-plaster
Group: Development/Python

%description doc
Contains the documentation for python-module-plaster.

%if_with python3
%package -n python3-module-%oname
Summary: Application configuration settings abstraction layer
Group: Development/Python3

%description -n python3-module-%oname
plaster is a loader interface around multiple
configuration file formats. It exists to define a common API for
applications to use when they wish to load configuration. The library
itself does not aim to handle anything except a basic API that
applications may use to find and load configuration settings. Any
specific constraints should be implemented in a loader which can be
registered via an entry point.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

# The plaster docs upstream only build if plaster is installed. Since we are building plaster docs
# from a source checkout, let's insert plaster into the path.
sed -i "s:import plaster:sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))\nimport plaster:" docs/conf.py

# Related to the above, upstream plaster gets the version for the docs by using pkg_resources which
# can only work if plaster is installed. Let's just substitute the version in since we know what it
# is.
sed -i "s/version = pkg_resources.*/version = '%{version}'/" docs/conf.py

# Upstream docs use pylons_sphinx_themes. Let's just convert it to use the standard sphinx theme for now.
sed -i "/import pylons_sphinx_themes/d" docs/conf.py
sed -i "/html_theme_path =.*/d" docs/conf.py
sed -i "/html_theme =.*/d" docs/conf.py
sed -i "/.*github_url.*/d" docs/conf.py

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%make_build -C docs html
rm -rf docs/_build/html/.buildinfo

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
PYTHONPATH="./src" py.test

%if_with python3
pushd ../python3
PYTHONPATH="./src" py.test3
popd
%endif

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/*

%files doc
%doc docs/_build/html
%doc CHANGES.rst LICENSE.txt README.rst

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5-1
- Initial release.
