%define oname plaster

Name: python3-module-%oname
Version: 1.0
Release: alt2
BuildArch: noarch
License: MIT
Group: Development/Python3
Summary: Application configuration settings abstraction layer
URL:     https://github.com/Pylons/%{oname}

# https://github.com/Pylons/plaster.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3(pytest)

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

%prep
%setup

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
%python3_build

%make_build SPHINXBUILD="sphinx-build-3" -C docs html
rm -rf docs/_build/html/.buildinfo

%install
%python3_install

%check
PYTHONPATH="./src" py.test3

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/*

%files doc
%doc docs/_build/html
%doc CHANGES.rst LICENSE.txt README.rst

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.0-alt2
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU: applied repocop patch

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5-1
- Initial release.
