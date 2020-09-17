Name:    tags4info
Version: 0.12.3
Release: alt1
Summary: Tags4info is Files, Web bookmarks and Applications organizer

Group:   Development/Java
License: $license
URL:     http://tags4.info/
Source0: %name-%version.tar
Packager: Pavel Vasenkov <pav@altlinux.org>

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel >= 1.8.0

BuildArch: noarch
Requires: java >= 1.8.0

%description
Description: Tags4info - file and web bookmarks organizer

Requires: jpackage-utils
Requires: %name = %EVR

%prep
%setup

%install
mkdir -p $RPM_BUILD_ROOT/etc/%name/resources/icons
cp -fR * %buildroot

%files
%{_sysconfdir}/%name/*
%{_target_libdir_noarch}/*
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/doc/*

%changelog
* Thu Sep 17 2020 Pavel Vasenkov <pav@altlinux.org> 0.12.3-alt1
- initial build for Alt Linux Sisyphus (Closes: #38928)