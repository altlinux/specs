# Copyright (c) 2022 SUSE LLC
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

%define basedir     %_datadir/icinga-L10n

Name:           icinga-l10n
Version:        1.3.0
Release:        alt2
Summary:        Icinga L10n
License:        GPL-2.0-or-later
Group:          Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/L10n/archive/v%version/%name-%version.tar

BuildArch:      noarch

%description
L10n (short for Localization) provides all translations available for Icinga (icinga2 package).

%prep
%setup

%build
# TODO: Regenerate *.mo files from *.po?
find locale -name '*.po' -delete

%install
mkdir -p %buildroot/%basedir
cp -prv locale %buildroot/%basedir

%files
%doc README.md
%basedir

%changelog
* Thu Nov 23 2023 Paul Wolneykien <manowar@altlinux.org> 1.3.0-alt2
- Save git remotes.

* Thu Nov 16 2023 Paul Wolneykien <manowar@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
