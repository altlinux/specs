%define _unpackaged_files_terminate_build 1

Name: alt-components-base
Version: 0.5.3
Release: alt1

Summary: Base set of ALT Distributions components
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alt-components-base

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: cmark
BuildRequires: alterator-entry >= 0.3.1
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

%prep
%setup

%build
for d in components/*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

%install
# install Components
mkdir -p "%buildroot%_alterator_datadir/components/categories"

for d in components/*/ ; do
    d="$(basename "$d")"
    mkdir -p "%buildroot%_alterator_datadir/components/$d"
    install -v -p -m 644 -D "components/$d/$d.component" "%buildroot%_alterator_datadir/components/$d"

    find "components/$d" -name '*.png' -type f | while read -r file; do
        install -v -p -m 664 -D "$file" "%buildroot%_alterator_datadir/components/$d"
    done

    find "components/$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/components/$d"
    done
done

for d in categories/* ; do
    d="$(basename "$d")"
    install -v -p -m 644 -D "categories/$d" "%buildroot%_alterator_datadir/components/categories"
done

# install Editions
mkdir -p "%buildroot%_alterator_datadir/editions"

for d in editions/*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

for edition_dir in editions/*/; do
    edition="$(basename "$edition_dir")"

    mkdir -p "%buildroot%_alterator_datadir/editions/$edition"

    install -v -p -m 644 -D "$edition_dir/$edition.edition" "%buildroot%_alterator_datadir/editions/$edition"

    find "$edition_dir" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/editions/$edition"
    done
done

%check
# check Components
./scripts/validate_categories.py

# check Editions
for e in `find ./editions -name '*.edition' -type f`; do
    alterator-entry validate "$e"
    (alterator-entry get "$e" sections.base.components &&
           alterator-entry get "$e" sections.main.components) 2>/dev/null |
    while read c; do
        if ! test -f "components/$c/$c.component"; then
            echo "failed to locate component $c in edition $e"
            exit 1
        fi
    done
done

%files
%_alterator_datadir/components/*

%files -n alt-editions-server
%dir %_alterator_datadir/editions
%_alterator_datadir/editions/edition_server
%_alterator_datadir/editions/edition_domain

%changelog
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
