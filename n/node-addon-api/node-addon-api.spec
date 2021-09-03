%define node_module node-addon-api

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-addon-api
Version: 4.1.0
Release: alt1

Summary: Module for using Node-API from C++

License: MIT
Group: Development/Other
Url: https://github.com/nodejs/node-addon-api/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nodejs/node-addon-api/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs node

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version

AutoReq: yes, nonodejs
AutoProv: no

#BuildRequires: libleveldb-devel
# >= 1.20

Requires: node

# for test, otherwise
# Expected `concurrency` to be a number from 1 and up, got `0` (number)
#BuildRequires: /proc

#BuildRequires: node-nyc

%description
This module contains header-only C++ wrapper classes
which simplify the use of the C based Node-API provided by Node.js when using C++.
It provides a C++ object model and exception handling semantics with low overhead.

%prep
%setup -a 1
# is it correct way?
#subst 's|<node_api.h>|<node/node_api.h>|' napi.h

%build
#npm run install
# TODO: test
#npm_build
#npm test

#rm -rfv node_modules/.cache/
#rm -fv node_modules/{nyc,.bin/nyc}
npm prune --production

# do not work without development requires
#check

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -rp package.json *.js *.h %buildroot/%nodejs_sitelib/%node_module

%files
%doc CHANGELOG.md LICENSE.md README.md
%nodejs_sitelib/%node_module

%changelog
* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- initial build for ALT Sisyphus
