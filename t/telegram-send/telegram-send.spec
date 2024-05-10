Name: telegram-send
Version: 0.37
Release: alt1

Summary: Send messages and files over Telegram from the command-line
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://github.com/rahiel/telegram-send
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt-shebang-fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: python3-module-anyio

%description
Telegram-send is a command-line tool to send messages and files over Telegram to
your account, to a group or to a channel. It provides a simple interface that
can be easily called from other programs.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%_bindir/%name
%python3_sitelibdir/telegram_send
%python3_sitelibdir/%{pyproject_distinfo telegram_send}

%changelog
* Fri May 10 2024 Anton Kurachenko <srebrov@altlinux.org> 0.37-alt1
- Initial build for Sisyphus.
