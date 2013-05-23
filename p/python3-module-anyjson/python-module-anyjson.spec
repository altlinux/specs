BuildRequires(pre): rpm-build-python3
%define oldname python-module-anyjson
%define sname anyjson
Summary: Get the best JSON encoder/decoder available on this system
Name: python3-module-%sname
Version: 0.3.1
Release: alt1
Source0: %oldname-%version.tar
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/anyjson/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Convenience module to import the best available json serialize/deserializer installed.

%prep
%setup -n %{oldname}-%{version} -q

%build
%python3_build

%install
%python3_install

%files
%doc README LICENSE CHANGELOG
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info

%changelog
* Thu May 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- python3 copycat test run

