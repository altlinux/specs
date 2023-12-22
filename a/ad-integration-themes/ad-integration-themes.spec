Name: ad-integration-themes
Version: 1.0
Release: alt1

Summary: Icon themes for AD integration BaseAlt projects
License: GPLv3+
Group:   Other
Url:     https://gitlab.basealt.space/knyazevsr/ad-integration-themes

Source: %name-%version.tar
BuildArch: noarch

%description
Themes pack for BaseAlt Active Directory integration projects
like ADMC, GPUI and other.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
cp -R themes/*/ %buildroot%_datadir/%name

%files
%doc LICENSE README.md
%_datadir/%name

%changelog
* Tue Dec 12 2023 Semyon Knyazev <samael@altlinux.org> 1.0-alt1
- Append AD-integration color, AD-integration duotone, AD-integration line
  and Kora AD-integration themes. These were tested only in ADMC context and
  can be expanded for other projects (like GPUI).
