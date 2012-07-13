Name: python-module-smmap
Version: 0.8.2
Release: alt1

Summary:  Sliding window memory map manager

License: BSD
Group: Development/Python
Url: git://github.com/Byron/smmap.git

Source: %name-%version.tar

%setup_python_module smmap

BuildRequires: python-devel python-module-setuptools
BuildArch: noarch


%description
A pure python implementation of a sliding window memory map manager

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir_noarch/%modulename/
%exclude %python_sitelibdir_noarch/%modulename/test
%python_sitelibdir_noarch/*.egg-info

%changelog
* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- initial
