%define _unpackaged_files_terminate_build 1

Name: alt-components-base
Version: 0.9.4
Release: alt1

Summary: Base set of ALT Distributions components
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alt-components-base

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: cmark
BuildRequires: autoconf-common
BuildRequires: alterator-entry >= 0.4.4
BuildRequires(pre): rpm-macros-alterator

Provides: alterator-components-base = 0.1.5
Obsoletes: alterator-components-base < 0.2.0

%description
%summary.

%package -n alt-editions-server
Summary: Editions of BaseALT distribution ALT Server
Group: System/Configuration/Other

Requires: alt-components-base = %version-%release

%description -n alt-editions-server
%summary.

%package -n alt-editions-education
Summary: Editions of BaseALT distribution ALT Education
Group: System/Configuration/Other

Requires: alt-components-base = %version-%release

%description -n alt-editions-education
%summary.

%package -n alt-components-vendors
Summary: Vendors set of ALT Distributions components
Group: System/Configuration/Other

Requires: alt-components-base = %version-%release

%description -n alt-components-vendors
%summary.

%prep
%setup

%build
for d in components/*/ vendors/*/*/ categories/* ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

cd editions
autoconf
./configure

%install
# install Components
mkdir -p "%buildroot%_alterator_datadir/components/categories"

rm -f install.base_components.list install.vendors_components.list vendors_categories.list
touch install.base_components.list install.vendors_components.list vendors_categories.list

for d in categories/*/ ; do
    d="$(basename "$d")"
    f="categories/$d/$d.category"
    c="$(alterator-entry get "$f" category ||:)"

    mkdir -p "%buildroot%_alterator_datadir/components/categories/$d"
    install -v -p -m 644 -D "$f" "%buildroot%_alterator_datadir/components/categories/$d/"

    find "categories/$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/components/categories/$d"
    done

    if [ "$c" != "vendors" ]; then
        echo "%_alterator_datadir/components/categories/$d" >>install.base_components.list
    else
        echo "%_alterator_datadir/components/categories/$d" >>install.vendors_components.list
        echo "$(alterator-entry get "$f" name)" >>vendors_categories.list
    fi
done

for d in components/*/ vendors/*/*/ ; do
    dd="$(dirname "$d")"
    d="$(basename "$d")"
    f="$dd/$d/$d.component"
    c="$(alterator-entry get "$f" category)"

    mkdir -p "%buildroot%_alterator_datadir/components/$d"
    install -v -p -m 644 -D "$f" "%buildroot%_alterator_datadir/components/$d"

    find "$dd/$d" -name '*.png' -type f | while read -r file; do
        install -v -p -m 664 -D "$file" "%buildroot%_alterator_datadir/components/$d"
    done

    find "$dd/$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/components/$d"
    done

    if grep -q "^$c$" vendors_categories.list; then
        echo "%_alterator_datadir/components/$d" >>install.vendors_components.list
    else
        echo "%_alterator_datadir/components/$d" >>install.base_components.list
    fi
done

# install Editions
mkdir -p "%buildroot%_alterator_datadir/editions"

for d in editions/edition_*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

for edition_dir in editions/edition_*/; do
    edition="$(basename "$edition_dir")"

    mkdir -p "%buildroot%_alterator_datadir/editions/$edition"

    install -v -p -m 644 -D "$edition_dir/$edition.edition" "%buildroot%_alterator_datadir/editions/$edition"

    find "$edition_dir" -type f -name "*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/editions/$edition"
    done
done

%check
# check Components and Editions
./scripts/validate_categories.py

%files -f install.base_components.list
%dir %_alterator_datadir/components
%dir %_alterator_datadir/components/categories

%files -n alt-components-vendors -f install.vendors_components.list

%files -n alt-editions-server
%dir %_alterator_datadir/editions
%_alterator_datadir/editions/edition_server
%_alterator_datadir/editions/edition_domain

%files -n alt-editions-education
%dir %_alterator_datadir/editions
%_alterator_datadir/editions/edition_education

%changelog
* Sun Oct 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.9.4-alt1
- components: remove alt-domain-server from education-server-apps

* Wed Oct 15 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.9.3-alt1
- Remove fonts-ttf-ms from education edition.
- Fix the changelog for the 0.9.2-alt1.

* Mon Oct 13 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.9.2-alt1
- Fix edition_domain: add alterator-service-samba-ad component
- Fix components (thx Maria Alexeeva):
  + new alterator-service-samba-ad component
  + add the alt-services package to the alterator-explorer component
  + update packages names in alterator-explorer component
- Fix docs: change .section to .edition (thx Maria Alexeeva)

* Tue Sep 30 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.9.1-alt1
- editions: update final-notes for edition_domain, edition_server,
  edition_education (thx Maria Fokanova)
- components: fix typo in displayname of docs category (thx Kirill Sharov)

* Mon Sep 22 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.9.0-alt1
- editions: add edition_education for ALT Education product

* Tue Sep 16 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.8.4-alt1
- components: add alt-domain-docs
- components: update links to official "Basealt LLC" documentation
  (thx Olga Kamaeva)
- editions: replace alt-server-docs with alt-domain-docs
  in edition_domain

* Tue Aug 19 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.8.3-alt1
- feat: update editions validation with vendors components not included
- components: replace vendors to separate packages
- components: add pptpd component (thx Andrey Limachko)
- editions: remove alterator-legacy-kiosk from server
- editions: add pptpd to main section (thx Andrey Limachko)

* Wed Aug 13 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.8.2-alt1
- editions: change behaviour and appearance of links in final-notes
  (thx Maria Fokanova)

* Tue Aug 12 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.8.1-alt1
- editions: up license version 11.0 -> 11.1

* Mon Aug 11 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.8.0-alt1
- feat: add support editions to validation script
- add conntrack-tools, haproxy and keepalived to main section in
  edition_server (closes: 55510)
- Fix components:
  + add x2goserver component
  + add conntrack-tools component
  + add keepalived component
  + add haproxy component
  + revert glibc meta package in glibc component (closes: 55498)

* Fri Aug 08 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.7.16-alt1
- editions(release-notes): fix Proxmox VE Backup Server version
  (thx Maria Fokanova)
- build: add year configuring for edition notes

* Thu Jul 31 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.7.15-alt1
- components: expand metapackages for education components

* Mon Jul 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.7.14-alt1
- editions: put notes for edition_domain & edition_server
- editions: fix display name of main section in edition_domain

* Tue Jul 08 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.7.13-alt1
- components: update descriptions
- categories: fix display name (windows-env, infra)

* Mon May 26 2025 Michael Chernigin <chernigin@altlinux.org> 0.7.12-alt1
- components: add directory for each category to support descriptions
- components: remove component descriptions headings

* Wed May 21 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.11-alt1
- editions: revert alt-server-docs to base section

* Wed May 21 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.10-alt1
- editions: replace lsb-core to main section

* Wed May 21 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.9-alt1
- Fix components:
  + extend hw packages in hardware-tools
  + fix diffutils package name in dev-utils
- Fix editions:
  + fix system/utils packages list
  + replace io-utils to main section
  + replace hardware-tools to main section
  + add lsb to main section
  + replace fwupd to main section

* Tue May 20 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.8-alt1
- components: add comments for yandex and fonts-ttf-ms

* Fri May 16 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.7-alt1
- components: add localized comments for education components

* Fri May 16 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.6-alt1
- editions: add alterator-legacy-ulogd and zabbix-agent2 to main section
- Fix components:
  + add zabbix-agent2 component
  + add alterator-legacy-ulogd component
  + add admx-thunderbird package to admx-templates component

* Thu May 15 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.5-alt1
- Fix components:
  + replace branding-alt-server-{alterator,indexhtml}
    from branding-alt-server to separate component
  + replace patch and xml-utils from base-utils to separate component
  + replace fwupd from firmware-tools to separate component
  + fix kernel-modules-virtualbox package name in virtualbox component
- Fix editions:
  + replace alt-server-docs, pax, gnupg2, avahi-mdns components to main
    section for server and domain editions
  + add fwupd, branding-alt-server-common and dev-utils to main section

* Wed May 14 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.4-alt1
- editions: add gnome-boxes to server (main section)

* Wed May 14 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- components: add mediawiki, moodle and education-robotics

* Wed May 14 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt1
- components: add fonts-ttf-ms
- components/yandex: fix name

* Tue May 06 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.1-alt1
- components: replace alterator-legacy-vsftpd to
  alterator-legacy-services category

* Mon May 05 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.7.0-alt1
- Fix components:
  + add userpasswd-gnome package to gnome-base component
  + add alterator-legacy-vsftpd component
- Fix editions:
  + add genisoimage to server main section for testing
  + add alterator-legacy-vsftpd to server
  + remove podsec from server and domain

* Thu Apr 24 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.9-alt1
- editions: replace postfix-server from main to base section
- components: remove by comment xdg and menu packages from
  base-special component
- components: remove by comment scanssh package from
  network-diag-tools component
- components: fixing typos (thx Alena Belaya) (closes: #53967)

* Mon Apr 21 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.8-alt1
- components: fix alterator-legacy-web (set alterator-net-eth)

* Sat Apr 19 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.7-alt1
- Fix editions:
  + change alterator-legacy-shares category to alterator-legacy-services
  + apply splited alterator-legacy-network-services
  + remove alterator-legacy-base component
- Fix components:
  + split alterator-legacy-network-services component for separate services
  + fix displayname and category of alterator-browser component
  + add alterator-net-eth package to alterator-legacy-lan component
  + split alterator-legacy-lan to ethernet, wifi and bondging
  + fix alterator-legacy-control component displayname and description
  + remove alterator-legacy-base component
  + replace alterator-legacy module to specific categories
  + add base alterator legacy modules to alterator-legacy-web
  + create new alterator-legacy components from alterator-legacy-base

* Fri Apr 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.6-alt1
- components: remove alterator-application-license package from
  alterator-explorer component.
- editions: corrected description for server and domain (thx Olga Kamaeva).

* Thu Apr 17 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.5-alt1
- editions: update descriptions for server and domain.

* Wed Apr 16 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.4-alt1
- Add samba-ad-client-support to base and main sections of alt-domain and
  alt-server editions respectively.

* Sat Apr 12 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.3-alt1
- components: remove mingetty package from base component
- Fix editions:
  + replace kernel-modules-r8168 from base to main section
  + replace systemd-timesyncd with chrony in base section
  + replace cgroup from main to base section
  + replace reiserfsprogs from main to base section

* Thu Apr 10 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.2-alt1
- Fix editions:
  + replace lsb component with lsb-core
  + replace ntp-utils from base to main section
  + replace network-manager from base to main section
- Fix components:
  + add lsb-core component
  + remove cpufreq-simple package from hardware-tools component
  + remove glibc meta package from glibc component
  + remove pam0_console from pam component
  + added new organizations to vendors (thx Anna Ivanova)

* Tue Apr 01 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.1-alt1
- Set system browser as component in server editions
- Add system browser component for products on different architectures

* Sat Mar 29 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.6.0-alt1
- Replace all vendors components and categories to separate
  alt-components-vendors subpackage

* Sat Mar 29 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5.5-alt1
- components: adjust desktop option for alterator-legacy-kiosk,
  gtkhash and libreoffice{-still}
- components: add new vendors with compatible components (thx Anna Ivanova)
- components: add telegram_desktop to the desktop-apps category (thx Anna Ivanova)

* Wed Mar 26 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5.4-alt1
- Remove jitsi-meet and nextcloud components from server edition

* Wed Mar 26 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5.3-alt1
- Add proxmox-backup-server and urbackup-server components to server
  edition and urbackup-client component to server and domain editions

* Tue Mar 25 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5.2-alt1
- Change apt-conf-branch-gostcrypto to apt-conf-branch in apt component
- Replace alterator-legacy to main section from base
- Add fonts-source component to main section for gnome-console

* Wed Mar 19 2025 Andrey Limachko <liannnix@altlinux.org> 0.5.1-alt1
- Add glibc package to glibc component
- Add inxi component to base section in server edition

* Wed Mar 19 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5-alt1
- Merge alt-editions-server-0.4.1-alt1 package as subpackage
- Adjust display names, descriptions, etc for various components
- Move alterator-legacy-* components to alterator-legacy category
- Add brasero component and cd-dvd-apps category
- Add genisoimage, gnome-boxes, lshw and inxi components

* Tue Mar 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4.1-alt1
- Replace altmediawriter and isomaster to separate category
  bootable-media-tools
- Set vendors categories and components as drafts
- Add openssh-askpass-common to ssh-client component
- Replace ssh-server component to internal services category
- Replace outdated firmware to separate component firmware-legacy
- Add iscan-firmware component for Epson flatbed scanners

* Fri Mar 14 2025 Andrey Limachko <liannnix@altlinux.org> 0.4-alt1
- feat: the pacemaker component has been added to the cluster
  category (thx Sergey Savelev)
- feat: new subdirectories with organizations have been added to the
  Vendors directory:
  + IT BASTION.
  + Gazinformservice.
  + Doctor Web.
  + ABP2B.
  Components by product names have been added to the listed
  organizations as well as to the 1C subdirectory (thx Anna Ivanova)
- feat: in the Vendors directory, subdirectories have been
  created for each vendor, with the name of the organization (without
  its legal form). For each product, components with a description
  are added to the subdirectories (thx Anna Ivanova)

* Tue Mar 11 2025 Andrey Limachko <liannnix@altlinux.org> 0.3.4-alt1
- fix: add aarch64 excludes for packages that are not in the
  aarch64 repository

* Sat Mar 08 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.3.3-alt1
- fix: rename obsolete systeminfo-license-viewer to
  alterator-application-license
- feat: add componentctl helper script for check, copy and move

* Fri Mar 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.3.2-alt1
- Fixed errors in some components (thx Sergey Savelev).

* Fri Mar 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.3.1-alt1
- Replace all -infra categories into common infra category.

* Fri Mar 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.3.0-alt1
- Complete refactoring: all in one for all products.

* Fri Feb 21 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.7-alt2
- Add simple category validation script.
- Fix errors detected by validate_categories.py.
  + Rename edication.category into education.category.
  + Remove nonexistent category downloading from initialization.category.

* Wed Feb 19 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.7-alt1
- The "downloading" category has been renamed to "boot", unnecessary
  packages have been removed (thx Sergey Savelev)

* Mon Feb 17 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.6-alt1
- Added categories for file system, disk utilities, archiving, and
  libraries (thx Sergey Savelev)

* Wed Feb 12 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.5-alt1
- The category System/graphics subsystem/fonts with fonts
  has been added (thx Anna Fomina)
- The Nginx category has been added (thx Sergey Savelev)

* Fri Feb 07 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.4-alt1
- Added a category for package management, vendors, and terminal
  (thx Sergey Savelev)

* Fri Feb 07 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.3-alt1
- Subcategories of desktop environments have been moved to the graphics
  category (thx Sergey Savelyev)
- The components with printing services, avahi, core modules, xdg and
  cryptography are divided into several parts (thx Sergey Savelev)

* Mon Feb 03 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.2-alt2
- Remove backends from requires (alterator-backend-component and
  alterator-backend-component_categories).

* Fri Jan 31 2025 Michael Chernigin <chernigin@altlinux.org> 0.2.2-alt1
- Remove all backend files in favour of autogenerated ones.
- Add %check section to validate all components and categories.

* Fri Jan 31 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.2.1-alt1
- Added category for Alt SP (thx Sergey Savelev)
- Added subcategory for fonts (thx Anna Fomina)
- Added category for alterator modules (thx Sergey Savelev)

* Fri Jan 31 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt1
- Rename to alt-components-base (this is common part of alt descriptions).

* Tue Jan 21 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.5-alt1
- Added components of the gnome environment (thx Sergey Savelev)

* Tue Dec 24 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Add stdout_strings to components status method to get list of installed
  packages.

* Mon Dec 23 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Added sections for categories (thx Sergey Savelev)
- Added nested categories (thx Sergey Savelev)

* Tue Dec 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- New components including some related to kde (thx Sergey Savelev, Elena
  Dyatlenko, Anna)
- Move categories into own dir

* Mon Nov 04 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- A basic set of components for ALT Server.

* Thu Oct 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build with example components.
