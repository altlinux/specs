%define _unpackaged_files_terminate_build 1
%define oname testlink

Name: python3-module-%oname
Version: 0.6.4
Release: alt1
Summary: A Python client to use the TestLink API
License: Apache 2.0
Group: Development/Python3
Url: https://github.com/orenault/TestLink-API-Python-client
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
TestLink-API-Python-client is a Python XML-RPC client for TestLink.

%prep
%setup

%build
%python3_build

%install
%python3_install
cp -r example test %buildroot%python3_sitelibdir/%oname

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/TestLink_API_Python_client-%version-py%_python3_version.egg-info
%doc LICENSE-2.0.txt doc/{install.rst,usage.rst}

%changelog
* Thu Oct 17 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.4-alt1
- Initial build for ALT
