%define oname openstackdocstheme
# checking theme is quite strange
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 3.0.1
Release: alt1

Summary: OpenStack Docs Theme

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/openstackdocstheme

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-dulwich >= 0.15.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%description
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to
docs.openstack.org. Intended for use by OpenStack projects.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

# Move theme files to proper location
# somehow they aren't installed automatically
mv %oname/theme %buildroot%python3_sitelibdir/%oname/theme

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/docstheme-build-pdf
%_bindir/docstheme-build-translated.sh
%_bindir/docstheme-lang-display-name.py
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%oname-%version-py%_python3_version.egg-info

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

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
