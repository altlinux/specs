Name:     vmtouch
Version:  1.3.1
Release:  alt1

Summary:  Portable file system cache diagnostics and control.
License:  %bsdstyle
Group:    Development/Other
Url:      https://hoytech.com/vmtouch/

Packager: Nikita Ermakov <arei@altlinux.org>

Source:   %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires: perl-podlators

%description
vmtouch is a tool for learning about and controlling the file system cache of unix and unix-like systems. It is BSD licensed so you can basically do whatever you want with it.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX="%{_prefix}"

%files
%_bindir/*
%_man8dir/*
%doc *.md

%changelog
* Mon Jan 21 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus.
