%define     oname openstackdocstheme
%def_with   python3

Name:       python-module-%oname
Version:    1.28.1
Release:    alt1

Summary:    Sphinx theme for RST-sourced documentation published to docs.openstack.org

License:    Apache-2.0
Group:      Development/Python
Url:        https://pypi.org/project/openstackdocstheme
#           https://github.com/openstack/openstackdocstheme

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %name-%version.tar

BuildArch:  noarch

BuildRequires: python-module-pbr
# for building docs
BuildRequires: python-module-dulwich

%if_with python3
BuildRequires: python3-module-pbr
%endif

%description
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to
docs.openstack.org. Intended for use by OpenStack projects.

%package -n python3-module-%oname
Summary:  Sphinx theme for RST-sourced documentation published to docs.openstack.org
Group: Development/Python3

%description -n python3-module-%oname
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to
docs.openstack.org. Intended for use by OpenStack projects.

%package -n python-module-%oname-docs
Summary:  Sphinx theme for RST-sourced documentation published to docs.openstack.org
Group: Development/Documentation

%description -n python-module-%oname-docs
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to

%prep
%setup

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

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

python setup.py build_sphinx

%install
%if_with python3
pushd ../python3
%python3_install
mkdir -p %buildroot%python3_sitelibdir_noarch/%oname/theme
cp -r %oname/theme/* \
%buildroot%python3_sitelibdir_noarch/%oname/theme
popd
%endif

mkdir -p %buildroot%python_sitelibdir_noarch/%oname/theme
cp -r %oname/theme/* \
%buildroot%python_sitelibdir_noarch/%oname/theme
%python_install

%files
%doc README.rst
%_bindir/*
%python_sitelibdir_noarch/%oname
%python_sitelibdir_noarch/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/*.egg-info
%endif

%files -n python-module-%oname-docs
%doc doc/build/html

%changelog
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
