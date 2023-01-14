%define oname attrdict

Name:           python3-module-%oname
Version:        2.0.2
Release:        alt1

Summary:        A dict with attribute-style access

Group:          Development/Python3
License:        MIT
URL:            https://pypi.org/project/attrdict3

Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3

%description
AttrDict is a library that provides mapping objects that allow their elements
to be accessed both as keys and as attributes.

%prep
%setup

# Remove bundled egg-info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%{oname}3-%version-py%_python3_version.egg-info

%changelog
* Sat Jan 14 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus.
