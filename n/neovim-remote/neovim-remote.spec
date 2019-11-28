%define oname nvr

Name: neovim-remote
Version: 2.3.4
Release: alt2

Summary: Remote controle for Neovim

License: %mit
Group: Development/Tools
Url: https://github.com/mhinz/neovim-remote

Source: %name-%version.tar
BuildArch: noarch

Patch: %name-%version-%release.patch

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
%patch -p1

%build
%python3_build

%install
%python3_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 2.3.4-alt2
- fix neovim module requirement

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 2.3.4-alt1
- new version

* Thu Oct 17 2019 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- new version

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
