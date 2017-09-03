Name: asciinema
Version: 1.4.0
Release: alt1
Summary: Terminal session recorder
License: GPLv3
Group: Terminals
Url: https://asciinema.org
BuildArch: noarch
Source: %name-%version.tar
BuildRequires: python3-module-setuptools

%description
asciinema [as-kee-nuh-muh] is a free and open source solution for
recording terminal sessions and sharing them on the web.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -pDm644 man/%name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%python3_sitelibdir/%{name}*
%_man1dir/%{name}.1.*
%doc CONTRIBUTING.md CHANGELOG.md README.md 

%changelog
* Sun Sep  3 2017 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- Initial build for ALT Linux Sisyphus
