%define oname plaster
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.1.2
Release: alt1

Summary: Application configuration settings abstraction layer

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/plaster/

# https://github.com/Pylons/plaster.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest)
%endif

%description
plaster is a loader interface around multiple
configuration file formats. It exists to define a common API for
applications to use when they wish to load configuration. The library
itself does not aim to handle anything except a basic API that
applications may use to find and load configuration settings. Any
specific constraints should be implemented in a loader which can be
registered via an entry point.

%if_with docs
%package doc
Summary: Documentation for python3-module-%oname
Group: Development/Documentation

%description doc
Contains the documentation for python3-module-%oname
%endif

%prep
%setup

%if_with docs
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
%endif

%build
%pyproject_build

%if_with docs
%make_build SPHINXBUILD="sphinx-build-3" -C docs html
rm -rf docs/_build/html/.buildinfo
%endif

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%if_with docs
%files doc
%doc docs/_build/html
%doc CHANGES.rst LICENSE.txt README.rst
%endif

%changelog
* Thu Dec 29 2022 Anton Vyatkin <toni@altlinux.org> 1.1.2-alt1
- new version 1.1.2

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
