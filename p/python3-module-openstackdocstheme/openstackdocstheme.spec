%define oname openstackdocstheme
%define fname python3-module-%oname
%define descr OpenStack Sphinx Theme \
\
Theme and extension support for Sphinx documentation that is published to \
docs.openstack.org. Intended for use by OpenStack projects.

%define exportPBRversion \
%if "3"=="" \
export PBR_VERSION=$(pbr -v 2>&1) \
%else \
export PBR_VERSION=$(pbr.py3 -v) \
%endif

Name:    %fname
Version: 1.21.1
Release: alt1

%if ""==""
Summary:  Sphinx theme for RST-sourced documentation published to docs.openstack.org
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License:  Apache-2.0
Url:      https://github.com/openstack/openstackdocstheme

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
BuildArch: noarch
BuildRequires: python3-module-pbr

%description
OpenStack Sphinx Theme

Theme and extension support for Sphinx documentation that is published to
docs.openstack.org. Intended for use by OpenStack projects.

%prep
%setup

%build
%if ""==""
%exportPBRversion
%python3_build
%endif

%install
%if ""==""
%exportPBRversion
%python3_install
%endif

%if ""==""

%files
%doc README.rst
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/*.egg-info

%endif

%changelog
* Wed Aug 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.21.1-alt1
- Initial build for Sisyphus (without docs).
