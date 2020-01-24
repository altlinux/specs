%define node_module node-sass

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-sass
Version: 4.13.1
Release: alt1

Summary: Node.js bindings to libsass

License: MIT License
Group: Development/Other
Url: https://github.com/sass/sass

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sass/node-sass/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: libsass-devel

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
Requires: node

%description
Node-sass is a library that provides binding for Node.js to LibSass,
the C version of the popular stylesheet preprocessor, Sass.

It allows you to natively compile .scss files to css at incredible speed
and automatically via a connect middleware.

%prep
%setup -a 1

%build
ln -s %nodejs_sitelib/node-gyp node_modules/
LIBSASS_EXT=auto npm run-script build
rm -f node_modules/node-gyp
npm prune --production

#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/node-sass %buildroot%_bindir/node-sass
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/{test,build,media,src}/

%files
%doc LICENSE README.md TROUBLESHOOTING.md
%_bindir/node-sass
%nodejs_sitelib/%node_module/

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.1-alt1
- initial build for ALT Sisyphus
