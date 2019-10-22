%define _unpackaged_files_terminate_build 1

Name: alterator-controlpp
Version: 0.0.3
Release: alt1

Summary: Control++ module.
Group: System/Configuration/Other
License: MIT
ExcludeArch: aarch64
Source: %name-%version.tar
Requires: alterator-l10n >= 2.7-alt4
Requires: control++ >= 0.19.0-alt1
Requires: alterator-fbi >= 5.41-alt1

BuildPreReq: alterator >= 4.6-alt3
BuildRequires(Pre): rpm-macros-alterator

%description
Control++ alterator module.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_localstatedir/%name/lists
mkdir -p %buildroot%_defaultdocdir/%name
touch %buildroot/%_localstatedir/%name/lists/empty
# Documentation
cp LICENSE %buildroot%_defaultdocdir/%name/

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%dir %_sysconfdir/%name
%dir %_localstatedir/%name
%dir %_localstatedir/%name/lists
%_localstatedir/%name/*
%dir %_defaultdocdir/%name/
%_defaultdocdir/%name/*

%changelog
* Thu Oct 10 2019 Leonid Krashenko <krash@altlinux.org> 0.0.3-alt1
- Bug fixes, paths validation.
- Added README file.
- Initiailization check.

* Fri Sep 27 2019 Leonid Krashenko <krash@altlinux.org> 0.0.2-alt1
- Excluded "aarch64" architecture.
- Updated l10n and parameter validation.
- Module setup page.

* Fri Sep 20 2019 Leonid Krashenko <krash@altlinux.org> 0.0.1-alt1
- Initial build.
