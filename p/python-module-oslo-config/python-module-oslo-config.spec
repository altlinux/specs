%global sname oslo.config

Name:       python-module-oslo-config
Version:    1.2.1
Release:    alt1
Summary:    OpenStack common configuration library

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %{name}-%{version}.tar
#
# patches_base=1.2.1
#
Patch0001: 0001-add-usr-share-project-dist.conf-to-the-default-confi.patch
Patch0002: 0002-Revert-Use-oslo.sphinx-and-remove-local-copy-of-doc-.patch
Patch0003: 0003-oslo-config-namespace_packages-remove.patch

BuildArch:  noarch
Requires:   python-module-setuptools
Requires:   python-module-argparse
Requires:   python-module-six

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package doc
Summary:    Documentation for OpenStack common configuration library
Group:      Documentation

BuildRequires: python-module-sphinx

%description doc
Documentation for the oslo-config library.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

# Remove bundled egg-info
rm -rf %{sname}.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%python_build

%install
%python_install

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%check

%files
%doc README.rst
%{python_sitelibdir}/oslo
%{python_sitelibdir}/*.egg-info
#%%{python_sitelibdir}/*-nspkg.pth

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.1-alt1
- First build for ALT

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Alan Pevec <apevec@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Tue Aug 20 2013 apevec@redhat.com 1.2.0-0.5.a3
- Look also for $prog-dist.conf for glance-manage

* Thu Aug 8 2013 pbrady@redhat.com - 1:1.2.0-0.4.a3
- Look for /usr/share/$project/$project-dist.conf by default

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.3.a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 pbrady@redhat.com - 1:1.2.0-0.2.a3
- Update to 1.2.0a3 milestone

* Mon Jun 24 2013 apevec@redhat.com - 1:1.2.0-0.1.a2
- Update to 1.2.0a2 milestone

* Tue Mar 12 2013 Mark McLoughlin <markmc@redhat.com> - 1:1.1.0-1
- Update to 1.1.0 final.

* Wed Mar  6 2013 Mark McLoughlin <markmc@redhat.com> - 1.1.0-0.1.b1
- Update to 1.1.0b1, bump epoch

* Tue Mar  5 2013 Mark McLoughlin <markmc@redhat.com> - 2013.1-0.1.b5
- Update to 2013.1b5
- Require python-argparse (#917937)

* Fri Feb 22 2013 Mark McLoughlin <markmc@redhat.com> - 2013.1-0.1.b4
- Update to 2013.1b4

* Sun Feb 17 2013 Mark McLoughlin <markmc@redhat.com> - 2013.1-0.1.b3
- Initial package (#912023).
