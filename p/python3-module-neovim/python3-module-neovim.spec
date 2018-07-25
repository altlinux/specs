%define oname neovim

Name: python3-module-%oname
Version: 0.2.6
Release: alt1

Summary: Python 3 client to Neovim

License: %asl
Group: Development/Python
Url: https://github.com/neovim/python-client

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3 rpm-build-licenses

%description
Pynvim implements support for python plugins in Nvim. It also works as a library
for connecting to and scripting Nvim processes through its msgpack-rpc API.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Wed Jul 25 2018 Vladimir Didenko <cow@altlinux.org> 0.2.6-alt1
- initial build for Sisyphus