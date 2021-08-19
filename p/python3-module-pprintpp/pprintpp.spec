%define oname pprintpp

Name: python3-module-pprintpp
Version: 0.4.0
Release: alt1

Summary: A drop-in replacement for pprint that's actually pretty

License: BSD
Group: Development/Python3
Url: https://github.com/wolever/pprintpp

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

# ipython is a optional extension
%add_python3_req_skip IPython

%description
A drop-in replacement for pprint that's actually pretty.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.txt
%_bindir/pypprint
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Sisyphus
