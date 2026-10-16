Name: rpm-build-mediawiki
Version: 0.7
Release: alt1

Summary: RPM build environment for MediaWiki extensions
License: GPL
Group: Development/Other

URL: https://www.altlinux.org/MediaWiki_Policy
Source: %name-%version.tar

BuildArch: noarch

Requires: rpm-macros-mediawiki = %EVR

%description
RPM build environment for MediaWiki extensions packages:
pulls in rpm-macros-mediawiki with the mediawiki_ext_install
and setup_mediawiki_ext macros.

See %url for detailed mediawiki extension packaging policy.

%package -n rpm-macros-mediawiki
Summary: RPM macros for packaging MediaWiki extensions
Group: Development/Other

%description -n rpm-macros-mediawiki
RPM macros for MediaWiki extensions packages: mediawiki_ext_install,
setup_mediawiki_ext, set_required_mediawiki.
Use it in BuildRequires(pre) of an extension spec.

See %url for detailed mediawiki extension packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/mediawiki

%files
%doc EXAMPLE.ALT

%files -n rpm-macros-mediawiki
%_rpmmacrosdir/mediawiki

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- move the macros to rpm-macros-mediawiki subpackage (RPM Macros Packaging Policy),
  rpm-build-mediawiki requires it
- update EXAMPLE.ALT to the current extension spec template
- URL: use https

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- support mediawiki 1.24 or newer
- add setup_mediawiki_ext, mediawikiext_dir macros

* Wed Apr 01 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- remove ?> in the last config line

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- add set_required_mediawiki macro

* Fri May 21 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- fix Url, Source and Summary

* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- do not pack temp. *.files file

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- fix spec, fix generated path to extension

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
