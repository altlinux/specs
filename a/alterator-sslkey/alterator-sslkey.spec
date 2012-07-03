%define _altdata_dir %_datadir/alterator

Name: alterator-sslkey
Version: 0.2.3
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for manipulations with ssl keys
Packager: Mikhail Efremov <sem@altlinux.org>
Source: %name-%version.tar

Requires: alterator >= 4.10-alt8 alterator-sh-functions >= 0.6-alt5 libshell >= 0.0.1-alt4
Requires: cert-sh-functions
Requires: tzdata
Requires: alterator-l10n >= 2.7-alt10

BuildPreReq: alterator >= 4.10-alt8
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for manipulations with ssl keys, sign requests
and certificates

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_altdata_dir/type/*

%changelog
* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- desktop file: add uk translation (by Roman Savochenko).

* Mon Oct 25 2010 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- show message when certificate uploaded.
- drop vhttpd-utils requires.
- Rewrite certificates validation.

* Thu Oct 15 2009 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- fix display long strings.
- use -enddate openssl option, not -text.

* Mon Sep 28 2009 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- display certificates expiration date.
- fix status of certificates translation.
- use wf 'none'.

* Tue Sep 15 2009 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- use button instead of reference (closes: #21457).
- fix requires.

* Mon Sep 07 2009 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- fix requires.
- move translations to alterator-l10n.
- Allow empty string in 'C' field (closes: #21456).

* Thu Aug 13 2009 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- fixed certificate deletion.
- hide 'Download sign request' if key not exist.
- index.scm: always update keys list when popup window closed.
- fixed error messages language.
- use 'e-mail' type.

* Fri Aug 07 2009 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- desktop file: 'SSL keys' -> 'SSL keys management'
- check certificate fields types.
- Russian translation.
- use timezone for default C and L.
- set popup window height.

* Mon Jul 20 2009 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- initial release


