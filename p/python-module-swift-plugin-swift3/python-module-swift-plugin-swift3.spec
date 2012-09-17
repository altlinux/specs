Name:		python-module-swift-plugin-swift3
Version:	1.0.0
Release:	alt1.git5c74ba04
Summary:	The swift3 plugin for Openstack Swift

Group:		Development/Python
License:	ASL 2.0
URL:		https://github.com/fujita/swift3
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-distribute
Requires:	python-module-swift

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%setup -q

%build
%{__python} setup.py build
sed -i 's/\r//' LICENSE

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelibdir}/swift3-%{version}-*.egg-info/
%{python_sitelibdir}/swift3/
%doc AUTHORS LICENSE README.md

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.0-alt1.git5c74ba04
- Initial release for Sisyphus (based on Fedora)
