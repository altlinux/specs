Name: python3-module-jsonrpc-base
Version: 1.0.3
Release: alt1

Summary: JSON-RPC client implementation interface python code
License: BSD
Group: Development/Python
Url: https://pypi.org/project/jsonrpc-base/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.* README.*
%python3_sitelibdir/jsonrpc_base
%python3_sitelibdir/jsonrpc_base-%version-*-info

%changelog
* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- initial
