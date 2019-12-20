%define oname multi_key_dict

Name: python3-module-%oname
Version: 2.0.3
Release: alt1

Summary: multiple key dictionary for Python (module) 
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/multi_key_dict/
BuildArch: noarch

# https://github.com/formiaczek/multi_key_dict
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus

