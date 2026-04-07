%define _unpackaged_files_terminate_build 1

Name:    speakup-tools
Epoch: 1
Version: 0.0
Release: alt1

Summary: Speakup Tools
License: GPL-3.0
Group:   Accessibility
Url:     https://github.com/linux-speakup/speakup-tools
VCS:     https://github.com/linux-speakup/speakup-tools

BuildArch: noarch

Source: %name-%version.tar

%description
This directory contains extra tools which make speakup easier to use.
Below you will find a brief description of these tools and how to

%prep
%setup

%build
%make all

%install
%makeinstall_std prefix=%_prefix


%files
%doc README LICENSE
%_bindir/speakup_setlocale
%_bindir/speakupconf
%_sbindir/talkwith
%_modprobedir/speakupconf.conf
%dir %_datadir/%name
%_datadir/%name/locales
%_man1dir/*

%changelog
* Tue Apr 07 2026 Artem Semenov <savoptik@altlinux.org> 1:0.0-alt1
- Updated versioning
- Fixed licensing

* Fri Dec 26 2025 Artem Semenov <savoptik@altlinux.org> 20240322-alt1
- Initial build for Sisyphus
