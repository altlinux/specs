%define _unpackaged_files_terminate_build 1

Name: alterator-control++
Version: 0.0.5
Release: alt1

Summary: Control++ module.
Group: System/Configuration/Other
License: MIT
ExcludeArch: aarch64
Source: %name-%version.tar
Requires: control++ >= 0.19.0-alt1
Requires: alterator-fbi >= 5.42

BuildRequires(Pre): rpm-macros-alterator
BuildRequires: alterator

%description
Control++ alterator module.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

# Configuration
mkdir -p %buildroot%_sysconfdir/%name
cp -r etc/* %buildroot%_sysconfdir/%name

# Generated files
mkdir -p %buildroot%_localstatedir/%name/lists
touch %buildroot/%_localstatedir/%name/lists/empty

# Documentation
mkdir -p %buildroot%_defaultdocdir/%name
cp LICENSE %buildroot%_defaultdocdir/%name/

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/controlpp.conf
%config(noreplace) %_sysconfdir/%name/warnlist
%dir %_localstatedir/%name
%dir %_localstatedir/%name/lists
%_localstatedir/%name/*
%dir %_defaultdocdir/%name/
%doc %_defaultdocdir/%name/*

%changelog
* Thu Nov 28 2019 Leonid Krashenko <krash@altlinux.org> 0.0.5-alt1
- Dangerous lists and user warnings
- Renamed to alterator-control++

* Mon Nov 18 2019 Leonid Krashenko <krash@altlinux.org> 0.0.4-alt1
- Unit-tests, bug fixes

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
