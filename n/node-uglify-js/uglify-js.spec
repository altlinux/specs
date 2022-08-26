%define node_module uglify-js

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-uglify-js
Version: 3.17.0
Release: alt1

Summary: JavaScript parser, minifier, compressor and beautifier toolkit

License: BSD License
Group: Development/Tools
Url: http://lisperator.net/uglifyjs/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mishoo/UglifyJS/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: node-mocha

Provides: uglifyjs = %version-%release

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version

#AutoReq: no
AutoProv: no
Requires: node

%description
UglifyJS is a JavaScript parser, minifier, compressor and beautifier toolkit.

Note:
* uglify-js@3 has a simplified API and CLI that is not backwards compatible with uglify-js@2.
* uglify-js only supports JavaScript (ECMAScript 5).
* To minify ECMAScript 2015 or above, transpile using tools like Babel.

%prep
%setup -a 1

%build

%check
npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/uglifyjs %buildroot%_bindir/uglifyjs
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/uglifyjs %buildroot%_bindir/uglify-js
mkdir -p %buildroot%nodejs_sitelib/%node_module/
#cp -a LICENSE README.md package.json bin/ lib/ tools/ node_modules/ %buildroot/%nodejs_sitelib/%node_module/
cp -a LICENSE README.md package.json bin/ lib/ tools/ %buildroot/%nodejs_sitelib/%node_module/

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/uglifyjs
%_bindir/uglify-js
%nodejs_sitelib/%node_module/

%changelog
* Fri Aug 26 2022 Vitaly Lipatov <lav@altlinux.ru> 3.17.0-alt1
- new version 3.17.0 (with rpmrb script)
- disable node_modules packing (no extra deps as for 3.17)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.9.4-alt1
- new version, full spec rewrite

-* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 2.8.22-alt1
-- Initial build for Sisyphus
