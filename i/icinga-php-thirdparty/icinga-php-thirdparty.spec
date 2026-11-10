# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 BaseALT Ltd
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define _unpackaged_files_terminate_build 1
%global basedir %_datadir/icinga-php/vendor

Name:           icinga-php-thirdparty
Version:        1.1.0
Release:        alt1
Summary:        Icinga PHP Thirdparty for Icinga Web 2
License:        MIT
Group:          Monitoring
URL:            https://icinga.com
Vcs:            https://github.com/Icinga/icinga-php-thirdparty.git
Source0:        https://github.com/Icinga/%name/archive/v%version/%name-%version.tar
Patch0:         Simferopol_TZ.patch

BuildRequires(pre): rpm-build-php-version

BuildRequires:  php%php_defver-devel
BuildRequires:  fdupes
BuildArch:      noarch

%description
This package bundles all 3rd party PHP libraries
used by Icinga Web products into one piece,
which can be integrated as library into Icinga Web 2.

%prep
%setup
%patch0 -p2
find vendor/predis -type f -name "*.sh" -exec chmod +x {} \;
chmod -x vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer/README
chmod -x vendor/icinga/zf1/library/Zend/Locale/Data/fy.xml

# unsuitable
truncate -s0 vendor/masterminds/html5/README.md

%build
# noting to build

%install
mkdir -vp %buildroot%basedir

cp -vr asset %buildroot%basedir
cp -vr vendor %buildroot%basedir
cp -vr composer.* %buildroot%basedir
cp -vr VERSION %buildroot%basedir

fdupes %buildroot%basedir

# Do not generate dependencies on contents of Docker files:
%add_findreq_skiplist %basedir/vendor/predis/predis/docker/unstable_cluster/*.sh

%files
%doc README.md
%basedir

%changelog
* Mon Nov 09 2026 Paul Wolneykien <manowar@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Mon Nov 09 2026 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt1
- New version 1.0.1.
- Fixes:
  + GHSA-x424-64qh-5j54 A malformed HTTP chunked body can lead to a
    denial-of-service and peg the CPU.
  + GHSA-g4f2-2pf3-2pwj Unbounded HTTP Client Response Header
    Buffering Leads to Memory Exhaustion DoS.
  + GHSA-v5mv-p594-2x33 Noncanonical host can bypass host-based checks.
  + GHSA-f7vp-7xgx-4w4r Noncanonical cookie domain keeps subdomain scope.
  + GHSA-wm3w-8rrp-j577 Host-only cookie scope is not preserved.
  + GHSA-f283-ghqc-fg79 Unbounded response cookies risk denial of service.
  + GHSA-h95v-h523-3mw8 URI fragments disclosed in redirect Referer headers.
  + GHSA-94pj-82f3-465w Proxy-Authorization headers can be sent to origin
    servers.
  + GHSA-cx96-42px-69fm Local file read due to improper file path
    validation in SVG images encoded as data-URI.
  + GHSA-wvh6-f5jh-8gw4 Chroot Validation Bypass.

* Mon Nov 09 2026 Paul Wolneykien <manowar@altlinux.org> 0.14.0-alt1
- New version 0.14.0.

* Tue Oct 06 2026 Paul Wolneykien <manowar@altlinux.org> 0.13.1-alt3
- Truncate unsuitable README.
- Updated timezone data according to zones in actual use.

* Mon Dec 29 2025 Paul Wolneykien <manowar@altlinux.org> 0.13.1-alt2
- Select PHP version using %%php_defver macro.

* Fri Aug 15 2025 Paul Wolneykien <manowar@altlinux.org> 0.13.1-alt1
- New version 0.13.1.

* Wed May 28 2025 Paul Wolneykien <manowar@altlinux.org> 0.12.1-alt1
- New version 0.12.1.

* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt2
- Save git remotes.

* Wed Nov 15 2023 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
