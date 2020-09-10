# TODO: use system leveldb, snappy
%define node_module leveldown

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-leveldown
Version: 5.6.0
Release: alt1

Summary: Pure C++ Node.js LevelDB binding serving as the back-end to LevelUP

License: MIT License
Group: Development/Other
Url: https://github.com/Level/leveldown

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Level/leveldown/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

#BuildArch: noarch

#BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
#Requires: node
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version

AutoReq: yes, nonodejs
AutoProv: no

BuildRequires: libleveldb-devel
# >= 1.20

Requires: node

# for test, otherwise
# Expected `concurrency` to be a number from 1 and up, got `0` (number)
BuildRequires: /proc

BuildRequires: node-nyc

%description
A Low-level Node.js LevelDB binding.
LevelDOWN was extracted from LevelUP and now serves as a stand-alone binding for LevelDB.

%prep
%setup -a 1
rm -rf deps
rm -fv test/port-libuv-fix-test.js

#__subst "s|.*prebuild-install.*||g" package.json
cat <<EOF >binding.gyp
{
    "targets": [
        {
            'target_name': '%node_module',
            'sources': [
                'binding.cc',
            ],
            'include_dirs': [
               '<!(node -e "require(\'napi-macros\')")'
            ],
            'cflags_cc': [
                    '<!(pkg-config --cflags leveldb)',
                    '$CFLAGS',
                ],
            'cflags_cc!': [
              '-fno-exceptions',
              '-Wno-unused-function'
            ],
          'link_settings': {
            'libraries': [
              '<!(pkg-config --libs leveldb)',
            ],
          }
        }
    ]
}
EOF

%build
#npm run install
%npm_build
npm test

rm -rfv node_modules/.cache/
rm -fv node_modules/{nyc,.bin/nyc}
npm prune --production

# do not work without development requires
#check

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -rp package.json *.js node_modules %buildroot/%nodejs_sitelib/%node_module

install -m644 -D build/Release/leveldown.node %buildroot/%nodejs_sitelib/%node_module/build/Release/leveldown.node

%files
%doc CHANGELOG.md LICENSE.md README.md
%nodejs_sitelib/%node_module

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- new version (5.6.0) with rpmgs script

* Wed Mar 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.5.1-alt1
- new version (5.5.1) with rpmgs script

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- initial build for ALT Sisyphus
