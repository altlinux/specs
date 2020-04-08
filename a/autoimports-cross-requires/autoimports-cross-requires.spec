Name: autoimports-cross-requires
Version: 1.0.0
Release: alt1

Summary: keeps genbasedir from optimizing out fs provides used in autoimports.
License: public domain
Group: Other
BuildArch: noarch

%description
genbasedir by default creates list of --useful-files based on
fs requires from Sisyphus packages. However some autoimports'
packages has filesystem requires as well but they are unknown
to genbasedir and ignored, thus generating unmets in autoimports/Sisyphus
packages.

This package is a trick to force genbasedir to explicitly
add specified provides required by packages from autoimports/Sisyphus.

%prep

%build

%install
mkdir -p %buildroot%_datadir/%name/
ln -s /usr/lib/node_modules/mocha %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Wed Apr 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- force fs provides for node-mocha

