%define node_module webpack-cli

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-webpack-cli
Version: 5.0.1
Release: alt1

Summary: Webpack's Command Line Interface

License: MIT
Group: Development/Other
Url: https://webpack.js.org/api/cli

Packager: Sergey V Markov <markow@altlinux.org>

# Source-url: https://github.com/webpack/webpack-cli/archive/webpack-cli@%version.tar.gz
Source: %name-%version.tar

Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

# /usr/bin/tsc
#BuildRequires: node-typescript >= 4.1.3

# FIXME: yarn needs /proc: https://github.com/yarnpkg/yarn/issues/7251
#BuildRequires: yarn /proc

# PeerDependencies
Requires: node-webpack >= 5.18.0

#Requires: node >= 10.13.0
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
Requires: node

%description
webpack CLI provides a flexible set of commands for developers to increase speed
when setting up a custom webpack project.
As of webpack v4, webpack is not expecting a configuration file,
but often developers want to create a more custom webpack configuration based on their use-cases and needs.
webpack CLI addresses these needs by providing a set of tools to improve the setup of custom webpack configuration.

Webpack is a  bundler for javascript and friends. Packs many modules into a few bundled assets.
Code Splitting allows for loading parts of the application on demand.
Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images,
JSON, Coffeescript, LESS, ... and your custom stuff. 

%prep
%setup -a2
#ln -s %nodejs_sitelib/webpack node_modules/
# only yarn install does it
#ln -s ../packages/webpack-cli node_modules/

%build
#npm run-script build

# do not work without development requires
# and needs xvfb-maybe
#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

#npm install --prefix %buildroot
mkdir -p %buildroot%nodejs_sitelib/%node_module/
#chmod a+x bin/*
#cp -rp bin node_modules package.json %buildroot/%nodejs_sitelib/%node_module
cp -a packages/webpack-cli/* %buildroot/%nodejs_sitelib/%node_module/
cp -v packages/webpack-cli/package.json ./
cp -a node_modules/ %buildroot/%nodejs_sitelib/%node_module/

mkdir -p %buildroot%_bindir/
#ln -s %nodejs_sitelib/%node_module/bin/webpack.js %buildroot%_bindir/webpack
%_ln_sr %buildroot%nodejs_sitelib/%node_module/bin/cli.js %buildroot%_bindir/webpack
%_ln_sr %buildroot%nodejs_sitelib/%node_module/bin/cli.js %buildroot%_bindir/webpack-cli

#nodejs_symlink_deps
#\npm_prune

#check
#npm_test

%files
%doc LICENSE README.md
%_bindir/webpack
%_bindir/webpack-cli
%nodejs_sitelib/%node_module/

%changelog
* Wed Mar 22 2023 Sergey V Markov <markow@altlinux.org> 5.0.1-alt1
- new version 5.0.1 (with rpmrb script)

* Tue Feb 23 2021 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt1
- new version 4.5.0 (with rpmrb script)
- pack only packages/webpack-cli

* Tue Oct 13 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 3.3.9-alt1
- initial build for ALT Sisyphus
