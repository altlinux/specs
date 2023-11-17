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
Version:        0.12.0
Release:        alt1
Summary:        Icinga PHP Thirdparty for Icinga Web 2
License:        MIT
Group:          Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%name/archive/v%version/%name-%version.tar

BuildRequires:  fdupes
BuildArch:      noarch

%description
This package bundles all 3rd party PHP libraries
used by Icinga Web products into one piece,
which can be integrated as library into Icinga Web 2.

%prep
%setup
find vendor/shardj -type f -name "*.php" -exec chmod -x {} \;
find vendor/predis -type f -name "*.sh" -exec chmod +x {} \;
chmod -x vendor/ezyang/htmlpurifier/library/HTMLPurifier/DefinitionCache/Serializer/README
chmod -x vendor/shardj/zf1-future/README-GIT.md
chmod -x vendor/shardj/zf1-future/library/Zend/Locale/Data/fy.xml

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
* Wed Nov 15 2023 Paul Wolneykien <manowar@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
