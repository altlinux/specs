Name:     acr
Version:  1.9.3
Release:  alt1

Summary:  Auto Conf Replacement
License:  %gpl2plus
Group:    Development/Other
Url:      https://github.com/radare/acr
BuildArch: noarch

Packager: Nikita Ermakov <arei@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
ACR tries to replace autoconf functionality generating a full-compatible
'configure' script (runtime flags). But using shell-script instead of m4.
This means that ACR is faster, smaller and easy to use.

%prep
%setup

%build
%configure

%install
%makeinstall_std

%check
%make_build test

%files
%_bindir/*
%_man1dir/*
%_man5dir/*
%_datadir/vim
%_datadir/%name
%_datadir/doc/%name-%version

%changelog
* Fri Jul 24 2020 Nikita Ermakov <arei@altlinux.org> 1.9.3-alt1
- Update to 1.9.3

* Mon Apr 08 2019 Nikita Ermakov <arei@altlinux.org> 1.7.2-alt1
- Initial build for ALT Sisyphus
