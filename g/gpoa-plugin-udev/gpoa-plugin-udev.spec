%define _unpackaged_files_terminate_build 1
%define _destdir %_datadir/PolicyDefinitions

Name: gpoa-plugin-udev
Version: 0.0.3
Release: alt1

Summary: USB device control plugin for gpupdate via udev rules
License: GPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/gpupdate-plugin-udev
BuildArch: noarch
AutoReqProv: no

BuildRequires(pre): rpm-build-python3
BuildRequires: gettext-tools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jinja2
BuildRequires: admx-lint

Requires: udev
Requires: gpoa-lib >= 0.16.1

Source0: %name-%version.tar

%description
USB device control policy plugin for gpupdate. Generates udev rules
from GPO settings to block/allow USB devices by VID:PID,
vendor ID, or serial number.

%package -n admx-basealt-udev
Summary: BaseALT Udev device management ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Requires: admx-basealt

%description -n admx-basealt-udev
BaseALT ADMX templates for managing device access via udev rules.
Provides policies to block USB devices, manage allow/deny lists by
VID:PID, serial number, and vendor ID.

%prep
%setup -q

%install
mkdir -p %buildroot/usr/lib/gpoa/plugins
install -m0644 plugin/udev_applier.py \
    %buildroot/usr/lib/gpoa/plugins/udev_applier.py

mkdir -p %buildroot%_datadir/%name/templates
install -m0644 templates/99-gpoa-udev.rules.j2 \
    %buildroot%_datadir/%name/templates/99-gpoa-udev.rules.j2

mkdir -p %buildroot/usr/lib/gpoa/plugins/locale/ru_RU/LC_MESSAGES
msgfmt -o %buildroot/usr/lib/gpoa/plugins/locale/ru_RU/LC_MESSAGES/udev_applier.mo \
    locale/ru_RU/LC_MESSAGES/udev_applier.po

mkdir -p %buildroot%_destdir
cp -r admx/ru-RU/ admx/en-US/ admx/BaseALT*.admx %buildroot%_destdir/

%check
%__python3  -m pytest -vra tests/
for file in admx/*.admx admx/*-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
/usr/lib/gpoa/plugins/udev_applier.py*
/usr/lib/gpoa/plugins/locale
%_datadir/%name

%files -n admx-basealt-udev
%dir %_destdir
%_destdir

%changelog
* Mon Aug 17 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.3-alt1
- build: bump to 0.0.3-alt1, ignore compiled .mo files
- fix: atomic rules write and verified udev reload
- fix: accept common boolean representations in policy values
- fix: normalize and validate VID values in policy lists
- fix: decide implicit block-all from validated lists only
- fix: scope root hub guard test to usb subsystem deny rules
- fix: emit block-device rule for deny-listed devices
- fix: exclude root hubs from blocking rules
- fix: deny list takes priority over allow rules
- build: add admx-lint validation to check section (thx Valentin Sokolov)
- fix: resolve admx-basealt file conflict, add category nesting (thx Valentin Sokolov)
- Improved supported platforms in Udev policies (thx Valentin Sokolov)

* Mon Jun 29 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.2-alt1
- feat: add admx-basealt-udev subpackage with ADMX policy templates
- refactor: rename jinja template from gpupdate to gpoa naming
- feat: implicitly enable block_usb_all when allowlists are
  configured
- fix: update test mocks to use gpoa_lib instead of gpoa
- fix: use real gpoa_lib import in tests, add gpoa-lib dependency
  to spec (thx Valery Sinelnikov)
- build: change install path to /usr/lib/gpoa/plugins/ (thx Valery Sinelnikov)
- feat: support custom registry_path via constructor parameter (thx Valery Sinelnikov)
- fix: use gpoa_lib instead of gpoa for plugin_base import (thx Valery Sinelnikov)

* Wed May 13 2026 BaseALT <skachedubov@altlinux.org> 0.0.1-alt1
- Initial release
