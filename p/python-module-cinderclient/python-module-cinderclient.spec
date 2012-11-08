Name:		python-module-cinderclient
Version:	0.2.26
Release:	alt1
Summary:	Python API and CLI for OpenStack cinder

Group:		Development/Python
License:	ASL 2.0
URL:		http://github.com/openstack/python-cinderclient
Source0:	%{name}-%{version}.tar.gz

Patch0001:	%{name}-fix-version-in-setup.patch

#
# patches_base=0.2
#

BuildArch:	noarch
BuildRequires:	python-module-distribute

Requires:	python-module-httplib2
Requires:	python-module-prettytable
Requires:	python-module-distribute

%description
This is a client for the OpenStack cinder API. There's a Python API (the
cinderclient module), and a command-line script (cinder). Each
implements 100% of the OpenStack cinder API.

%prep
%setup -q
%patch0001 -p2

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/cinder
%{python_sitelibdir}/cinderclient
%{python_sitelibdir}/*.egg-info

%changelog
* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2.26-alt1
- Initial release for Sisyphus (based on Fedora)
