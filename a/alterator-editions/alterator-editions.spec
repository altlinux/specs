%define _altdata_dir %_datadir/alterator

Name: alterator-editions
Version: 0.1
Release: alt1

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for change between product editions
License: GPL-2.0+
Group: System/Configuration/Other
Requires: alterator >= 3.1-alt4, alterator-sh-functions
Requires: alterator-l10n >= 2.9.163
Requires: alterator-backend-edition-utils

BuildPreReq: alterator >= 3.1
BuildRequires: alterator

%description
alterator module for change between product editions

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Sat Aug 02 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.1-alt1
- Initial build.
