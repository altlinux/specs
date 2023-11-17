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
%global basedir %_datadir/icinga-php/ipl

Name:           icinga-php-library
Version:        0.13.1
Release:        alt1
Summary:        Icinga PHP Library for Icinga Web 2
License:        MIT
Group:          Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%name/archive/v%version/%name-%version.tar

BuildRequires(pre): rpm-build-php-version

BuildRequires:  fdupes
BuildArch:      noarch

Requires: php%_php_major.%_php_minor-intl

%description
This project bundles all Icinga PHP libraries into one
piece and can be integrated as library into Icinga Web 2.

%prep
%setup

%build
# nothing to build

%install
mkdir -vp %buildroot%basedir

cp -vr asset %buildroot%basedir
cp -vr vendor %buildroot%basedir
cp -vr composer.* %buildroot%basedir
cp -vr VERSION %buildroot%basedir

fdupes %buildroot%basedir

%files
%doc README.md
%basedir

%changelog
* Wed Nov 15 2023 Paul Wolneykien <manowar@altlinux.org> 0.13.1-alt1
- Initial build for Sisyphus.
