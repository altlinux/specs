Name: xdg-terminal-exec
Version: 0.1
Release: alt1

Summary: Proposal for XDG terminal execution utility

License: GPLv3
Group: System/Base
Url: https://github.com/Vladimir-csp/xdg-terminal-exec

# Source-git: https://github.com/Vladimir-csp/xdg-terminal-exec.git
Source: %name-%version.tar

BuildArch: noarch

%description
Proposal for XDG terminal execution utility and default terminal specification.

The configuration spec is crafted in image of mime-apps-spec using different names in similar structure, governed by basedir-spec.

%prep
%setup

%build

%install
install -D %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Sat Apr 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
