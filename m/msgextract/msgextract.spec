Name: msgextract
Version: 0.2
Release: alt1

Summary: Easily extract the contents of MSG email files

License: GPLv2
Group: File tools
Url: https://github.com/AlexanderShad/msgextract
Vcs: https://github.com/AlexanderShad/msgextract

Source: %name-%version.tar

Requires: perl-Email-Outlook-Message-scripts mpack

BuildArch: noarch

%description
A simple script to automate the unpacking of an MSG email message file so that it can be done with one command.

%prep
%setup

%build
%install
install -Dm755 %name.sh %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Mon Dec 09 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
