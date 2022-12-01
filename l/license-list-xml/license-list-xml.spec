Name: license-list-xml
Version: 3.19
Release: alt1

Summary: Contains the various common licenses used in the %distribution
License: CC0-1.0
Group: System/Base
BuildArch: noarch
Url: https://github.com/spdx/license-list-XML

BuildRequires: python3

Source: %name-%version.tar

Patch0001: 0001-Bitstream-Vera-Separate-the-title-from-the-paragraph.patch
Patch0002: 0002-LGPL-3.0-Remove-optional-GPL-license-from-the-text.patch
Patch0003: 0003-GCC-exception-2.0-Fix-spacing.patch
Patch0004: 0004-openvpn-openssl-exception-Fix-spacing.patch

%description
The SPDX License List is an integral part of the SPDX Specification. The SPDX
License List itself is a list of commonly found licenses and exceptions used in
free and open or collaborative software, data, hardware, or documentation.

%package -n common-licenses
Summary: Contains the various common licenses used in the %distribution in XML format
Group: System/Base

%description -n common-licenses
Contains the various common licenses uses by the %distribution.
Instead of including the COPYING file in every package,
just refer to this one.

%prep
%setup -q
%autopatch -p1

%build
mkdir -- .export

rpm/spdx-sync.py .export \
	rpm/not-spdx \
	src \
	src/exceptions

cp -a rpm/license-ambiguous .export/

while read -r alias target; do
	ln -s -- "$target" ".export/license/$alias"
done < rpm/symlinks.not-spdx

cd .export

if find license license-ambiguous -mindepth 1 -maxdepth 1 -printf '%%f\n' | sort | uniq -d | grep ^; then
	echo >&2 'These licenses are listed in both directories simultaneously.'
	exit 1
fi

if find license -mindepth 1 -maxdepth 1 -name '*-with-*-exception' |grep ^; then
	echo >&2 'License exceptions should be in the license-exception directory.'
	exit 1
fi

%install
mkdir -p -- \
	%buildroot%_licensedir \
	%buildroot%_licensedir-ambiguous \
	%buildroot%_licensedir-exception

cp -dp .export/license/* %buildroot%_licensedir
cp -dp .export/license-ambiguous/.desc %buildroot%_licensedir-ambiguous
cp -dp .export/license-ambiguous/* %buildroot%_licensedir-ambiguous
cp -dp .export/license-exception/* %buildroot%_licensedir-exception

mkdir -p -- \
	%buildroot%_datadir/%name/exceptions

cp -dp rpm/not-spdx/*.xml   %buildroot%_datadir/%name/
cp -dp src/*.xml            %buildroot%_datadir/%name/
cp -dp src/exceptions/*.xml %buildroot%_datadir/%name/exceptions/

%files
%_datadir/%name

%files -n common-licenses
%_licensedir
%_licensedir-ambiguous
%_licensedir-exception

%changelog
* Thu Dec 01 2022 Alexey Gladkov <legion@altlinux.ru> 3.19-alt1
- New release (3.19).
- Add:
  + checkmk
  + FSFULLRWD
  + Knuth-CTAN
  + libutil-David-Nugent
  + x11vnc-openssl-exception

* Fri Aug 12 2022 Alexey Gladkov <legion@altlinux.ru> 3.18-alt1
- New release (3.18).
- Add:
  + CC-BY-3.0-IGO
  + GStreamer-exception-2005
  + GStreamer-exception-2008
  + LZMA-SDK-9.11-to-9.20
  + LZMA-SDK-9.22
  + MS-LPL
  + Minpack
  + mpi-permissive
  + NICTA-1.0
  + Python-2.0.1

* Tue Aug 09 2022 Alexey Gladkov <legion@altlinux.ru> 3.17-alt2
- Add Yandex Browser Software License Agreement (ALT#43480)

* Tue Jul 19 2022 Alexey Gladkov <legion@altlinux.ru> 3.17-alt1
- Change the source repository to license-list-XML.
- Subpackage common-licenses contains the exported data from the XML format.
- Change License to CC0-1.0.
- Remove Packager tag.

* Thu Aug 05 2021 Alexey Gladkov <legion@altlinux.ru> 1.13-alt1
- Fix formatting of the MPL-2.0 (ALT#40506)

* Sun Feb 07 2021 Arseny Maslennikov <arseny@altlinux.org> 1.12-alt1
- Add licenses:
  + Add the Z Shell license (ALT-Zsh)

* Mon Aug 24 2020 Fr. Br. George <george@altlinux.ru> 1.11-alt1
- Add licenses:
  + Add ParaType Open Font license

* Tue Mar 24 2020 Alexey Gladkov <legion@altlinux.ru> 1.10-alt1
- Rename ALT-CyrusIMAP -> ALT-Cyrus (ALT#38223)
- Remove licenses with exceptions from the license directory

* Mon Feb 24 2020 Alexey Gladkov <legion@altlinux.ru> 1.9-alt1
- Add licenses:
  + Add RADVD license (ALT-RADVD) (ALT#38133)
  + Add OpenPub-1.0 license (ALT-OpenPub-1.0) (ALT#20245)

* Mon Dec 16 2019 Alexey Gladkov <legion@altlinux.ru> 1.8-alt1
- Add licenses:
  + Add PLATON "license" (ALT-Proprietary-PLATON)

* Thu Nov 28 2019 Alexey Gladkov <legion@altlinux.ru> 1.7-alt1
- Add licenses:
  + Add Free Art License 1.3 (ALT-Free-Art-1.3)
- Rename non-standard licenses and create compatibility links

* Wed Nov 20 2019 Alexey Gladkov <legion@altlinux.ru> 1.6-alt1
- Sync with SPDX.
- Add licenses:
  + BSD 3-Clause Open MPI variant (BSD-3-Clause-Open-MPI)
  + Blue Oak Model License 1.0.0 (BlueOak-1.0.0)
  + Creative Commons Public Domain Dedication and Certification (CC-PDDC)
  + CERN Open Hardware Licence v1.1 (CERN-OHL-1.1)
  + CERN Open Hardware Licence v1.2 (CERN-OHL-1.2)
  + Historical Permission Notice and Disclaimer - sell variant (HPND-sell-variant)
  + Japan Network Information Center License (JPNIC)
  + Mulan Permissive Software License, Version 1 (MulanPSL-1.0)
  + Open Government Licence - Canada (OGL-Canada-2.0)
  + The Parity Public License (Parity-6.0.0)
  + Solderpad Hardware License v0.5 (SHL-0.5)
  + Solderpad Hardware License, Version 0.51 (SHL-0.51)
  + SSH OpenSSH license (SSH-OpenSSH)
  + SSH short notice (SSH-short)
  + Server Side Public License v1 (SSPL-1.0)
  + TAPR Open Hardware License v1.0 (TAPR-OHL-1.0)
  + Upstream Compatibility License v1.0 (UCL-1.0)
  + SQLite Blessing (blessing)
  + Etalab Open License 2.0 (etalab-2.0)
  + PNG Reference Library version 2 (libpng-2.0)
- Add exceptions:
  + GPL Cooperation Commitment Version 1.0 (GPL-CC-1.0)
  + Runtime Library Exception to the Apache 2.0 License (Swift-exception)
  + The Universal FOSS Exception, Version 1.0 (Universal-FOSS-exception-1.0)

* Mon Nov 18 2019 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- Add ambiguous license names
- Add Bitstream Vera license
- Add compatibility link for PHP-3.01
- Add compatibility links for GPL and LGPL
- Add copyleft-next-0.3.0
- Add NVIDIA license
- Add Perl license
- Add script to synchronize with SPDX
- Add text for Public Domain
- Add Thor Public License
- Add Ubuntu Font License 1.0
- Add Unicode Character Database Terms Of Use
- Remove non-obvious alias
- Rename exception/ to license-exception/
- Update MIT from SPDX

* Fri Nov 09 2018 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- Add licenses from SPDX version 3.3 2018-10-24 (https://spdx.org/licenses/).
- Add licenses exceptions from SPDX version 3.2 (https://spdx.org/licenses/exceptions-index.html).
- Add aliases without version for licenses without variants.

* Thu Sep 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Adeed new licenses:
  + FDL-1.2, GPL-3, LGPL-3: Imported from ftp://ftp.gnu.org/gnu/Licenses/ (#12612)
  + Artistic-2: Imported from http://www.perlfoundation.org/attachment/legal/artistic-2_0.txt
  + ISC: Imported from dhcp-3.0.6

* Fri Jul 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated: FDL-1.1, GPL-2, LGPL-2.1.
  (updated FSF postal mail address).

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated: GPL-2, LGPL-2.0, LGPL-2.1.
- Added: GPL-1, Apache-2.0, ZPL-2.1.

* Thu Jun 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1-alt1
- Changed license of this package to "distributable".

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1mdk
- Initial revision.
