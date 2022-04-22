%define pname canvas

Name: node-canvas
Version: 2.8.0
Release: alt1

Summary: node-canvas is a Cairo-backed Canvas implementation for Node.js

License: MIT
Group: Development/Other
Url: https://github.com/Automattic/node-canvas

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Automattic/node-canvas/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar


BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: gcc-c++ libcairo-devel pango-devel libjpeg-devel libgif-devel libpixman-devel
BuildRequires: node-nan node-mocha node-gyp

%description
node-msgpack is an addon for NodeJS that provides an API for serializing
and de-serializing JavaScript objects using the MessagePack library.
The performance of this addon compared to the native JSON object isn't too bad,
and the space required for serialized data is far less than JSON.

%prep
%setup -a1

%build
%npm_build

npm test || :
npm prune --production

#%check
#npm test

%install
%npm_install
rm -rf %buildroot/%nodejs_sitelib/%pname/{prebuild,examples,src,test,binding.gyp}/

%files
%doc Readme.md
%nodejs_sitelib/%pname/

%changelog
* Mon Dec 20 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- initial build for ALT Sisyphus
