%define pname msgpack
%def_with system_msgpack

Name: node-msgpack
Version: 1.0.3
Release: alt2

Summary: MessagePack implementation for Node.js

License: MIT License
Group: Development/Other
Url: https://github.com/msgpack/msgpack-node

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/msgpack/msgpack-node/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-development-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

%if_with system_msgpack
BuildRequires: libmsgpack-devel
%endif

BuildRequires: node-nodeunit node-nan
BuildRequires: /proc

#AutoReq: no
#AutoProv: no

%description
node-msgpack is an addon for NodeJS that provides an API for serializing
and de-serializing JavaScript objects using the MessagePack library.
The performance of this addon compared to the native JSON object isn't too bad,
and the space required for serialized data is far less than JSON.

%prep
%setup
%if_with system_msgpack
rm -rfv deps/msgpack/
cat <<EOF >binding.gyp
{
    "targets": [
        {
            'target_name': 'msgpackBinding',
            'sources': [
                'src/msgpack.cc',
            ],
            'include_dirs': [
               '<!(node -e "require(\'nan\')")'
            ],
            'cflags_cc': [
                    '<!(pkg-config --cflags msgpack)',
                    '$CFLAGS',
                ],
            'cflags_cc!': [
              '-fno-exceptions',
              '-Wno-unused-function'
            ],
          'link_settings': {
            'libraries': [
              '<!(pkg-config --libs msgpack)',
            ],
          }

        }
    ]
}
EOF
%endif

%build
#ln -s %nodejs_sitelib/node-gyp node_modules/
#node-gyp rebuild
%npm_build
#rm -f node_modules/node-gyp

# most test is failed due using obsoleted nodeunit in upstream
npm test
npm prune --production

#%check
#npm test

%install
%npm_install
mkdir -p %buildroot%_bindir/
cp bin/* %buildroot%_bindir/
# nan is devdeps
#cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
#rm -rf %buildroot/%nodejs_sitelib/%pname/{test,build,media,src}/

%files
%doc LICENSE README.md
%_bindir/json2msgpack
%_bindir/msgpack2json
%nodejs_sitelib/%pname/

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt2
- regenerate addition modules

* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Sisyphus
