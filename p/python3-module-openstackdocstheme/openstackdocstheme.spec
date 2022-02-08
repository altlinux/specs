%define     oname openstackdocstheme

%def_with docs
# problems with hacking < 3.1.0
%def_without check

Name:       python3-module-%oname
Version:    2.3.1
Release:    alt1

Summary:    Sphinx theme for RST-sourced documentation published to docs.openstack.org

License:    Apache-2.0
Group:      Development/Python3
Url:        https://pypi.org/project/openstackdocstheme
#           https://github.com/openstack/openstackdocstheme

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %name-%version.tar

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-dulwich
%endif

%if_with check
BuildRequires: python3-module-pip
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-hacking
%endif

%description
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to
docs.openstack.org. Intended for use by OpenStack projects.

%package doc
Summary:    %oname documentation
Group:      Development/Documentation
%description doc
Documentation for %oname

%prep
%setup

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

%if_with docs
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir_noarch/%oname/theme
cp -r %oname/theme/* \
%buildroot%python3_sitelibdir_noarch/%oname/theme

%check
python3 setup.py test

%files
%doc README.rst
%_bindir/docstheme-build-pdf
%_bindir/docstheme-build-translated.sh
%_bindir/docstheme-lang-display-name.py
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/*.egg-info

%if_with docs
%files doc
%doc doc/build/html
%endif

%changelog
* Tue Feb 08 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Build new version.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Build new version.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.7-alt1
- Build new version.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.6-alt1
- Build new version.

* Thu Jul 30 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.5-alt1
- Build new version.

* Mon Jun 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.2-alt1
- Build new version.
- Build with docs.

* Wed May 20 2020 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Build new version.

* Tue Feb 11 2020 Grigory Ustinov <grenka@altlinux.org> 1.31.2-alt1
- Build new version.
- Drop python2 support.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.31.1-alt1
- Build new version.
- Remove docs.

* Thu Jun 06 2019 Grigory Ustinov <grenka@altlinux.org> 1.30.0-alt1
- Build new version.

* Mon Apr 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.29.2-alt1
- Build new version.

* Thu Feb 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.29.1-alt1
- Build new version.

* Thu Jan 10 2019 Grigory Ustinov <grenka@altlinux.org> 1.28.1-alt1
- Build new version.

* Tue Nov 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.27.1-alt1
- Build new version.

* Tue Oct 09 2018 Grigory Ustinov <grenka@altlinux.org> 1.25.1-alt2
- Build with docs.

* Fri Oct 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.25.1-alt1
- Build new version.
- Change build scheme.

* Thu Aug 09 2018 Grigory Ustinov <grenka@altlinux.org> 1.21.1-alt2
- Fix copying missing theme files.

* Wed Aug 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.21.1-alt1
- Initial build for Sisyphus (without docs).
