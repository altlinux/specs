%define oname nvr

Name: neovim-remote
Version: 2.2.1
Release: alt1

Summary: Remote controle for Neovim

License: %mit
Group: Development/Tools
Url: https://github.com/mhinz/neovim-remote

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: nopython
%define __python %nil

BuildRequires(pre): rpm-build-python3 rpm-build-licenses
Requires: python3(msgpack)

%description
This package provides an executable called nvr which solves these cases:
 - Controlling nvim processes from the shell. E.g. opening files in another terminal window.
 - Opening files from within :terminal without starting a nested nvim process.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Thu Sep 19 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- new version

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.1.9-alt1
- new version

* Mon Apr 8 2019 Vladimir Didenko <cow@altlinux.org> 2.1.7-alt1
- new version

* Tue Mar 19 2019 Vladimir Didenko <cow@altlinux.org> 2.1.5-alt1
- new version

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 2.1.4-alt1
- new version

* Wed Sep 19 2018 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt1
- initial build for Sisyphus
