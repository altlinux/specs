Name:		python-module-glanceclient
Version:	0.4.1
Release:	alt1
Summary:	Python API and CLI for OpenStack Glance

Group:		Development/Python
License:	ASL 2.0
URL:		http://github.com/openstack/python-glanceclient
Source0:	%{name}-%{version}.tar.gz

#
# patches_base=0.4.1
#
Patch0001:	python-module-glanceclient-ensure-v1-lqp-works-correctly.patch
Patch0002:	python-module-glanceclient-enable-client-V1-to-download-images.patch
Patch0003:	python-module-glanceclient-update-pip-requires-with-warlock-2.patch
Patch0004:	python-module-glanceclient-update-command-descriptions.patch
Patch0005:	python-module-glanceclient-adjust-egg-info-for-Fedora.patch
Patch0006:	python-module-glanceclient-fix-keystoneclient-deps.patch

BuildArch:	noarch
BuildRequires:	python-module-distribute

Requires:	python-module-httplib2
Requires:	python-module-keystoneclient >= 0.1.2
Requires:	python-module-prettytable
Requires:	python-module-distribute
Requires:	python-module-warlock

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each
implements 100% of the OpenStack Glance API.

%prep
%setup -q
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
# Remove bundled egg-info
rm -rf python_glanceclient.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

%files
%doc README.rst
%doc LICENSE
%{_bindir}/glance
%{python_sitelibdir}/glanceclient
%{python_sitelibdir}/*.egg-info

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)
