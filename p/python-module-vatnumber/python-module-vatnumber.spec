%define realname vatnumber

Name:           python-module-%realname
Version:        1.0
Release:        alt1
Summary:        Python module to validate VAT numbers

Group:          Development/Python
License:        GPLv3+
URL:            http://code.google.com/p/vatnumber/
Source0:        http://vatnumber.googlecode.com/files/%realname-%version.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute

%description
Python module to validate VAT numbers.

%prep
%setup -q -n %realname-%version

%build
%python_build

%install
%python_install

%files
%doc CHANGELOG COPYRIGHT README
%python_sitelibdir/%realname
%python_sitelibdir/%{realname}*.egg-info


%changelog
* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

