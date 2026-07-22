%define node_module zeromq
%define pname zeromq

%filter_from_requires /^nodejs.engine./d
%filter_from_requires /^npm(cmake-ts)/d
%filter_from_requires /^npm(node-addon-api)/d
%{?nodejs_find_provides_and_requires}

Name: node-zeromq
Version: 6.5.0
Release: alt1

Summary: Node.js bindings for the ZeroMQ messaging library
License: MIT
Group: Development/Other
Url: https://github.com/zeromq/zeromq.js
Vcs: https://github.com/zeromq/zeromq.js.git

Source: %name-%version.tar
ExclusiveArch: %nodejs_arches

BuildRequires(pre): rpm-build-intro >= 1.9.18
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs node node-devel
BuildRequires: node-addon-api
BuildRequires: libzeromq-devel
BuildRequires: gcc-c++ pkg-config

Requires: node
Requires: libzeromq

Provides: npm(%node_module) = %EVR
Provides: nodejs-%node_module = %EVR

%description
Next-generation ZeroMQ bindings for Node.js. Builds the native N-API addon
against the system libzmq (no bundled/vcpkg copy) and ships the transpiled
JavaScript API.

%prep
%setup

%build
./node_modules/.bin/tsc -p src/tsconfig.json

mkdir -p build/Release
g++ %optflags -std=c++20 -fPIC -shared \
    -o build/Release/addon.node \
    src/context.cc src/incoming_msg.cc src/module.cc src/observer.cc \
    src/outgoing_msg.cc src/proxy.cc src/socket.cc \
    -I%_includedir/node \
    -I%nodejs_sitelib/node-addon-api \
    $(pkg-config --cflags libzmq) \
    -DBUILDING_NODE_EXTENSION \
    -DNAPI_CPP_EXCEPTIONS \
    -DV8_COMPRESS_POINTERS \
    -DV8_31BIT_SMIS_ON_64BIT_ARCH \
    -DV8_REVERSE_JSARGS \
    $(pkg-config --libs libzmq)

cat > lib/load-addon.js <<'EOF'
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = require("../build/Release/addon.node");
EOF

rm -rf node_modules
rm -f .gitignore

%install
%npm_install
rm -rf %buildroot%nodejs_sitelib/%pname/{src,script,test,examples,docker}
rm -f  %buildroot%nodejs_sitelib/%pname/{CMakeLists.txt,vcpkg.json,tsconfig.json,tsconfig.docs.json,typedoc.json,CONTRIBUTING.md,package-lock.json,pnpm-lock.yaml}
rm -f  %buildroot%nodejs_sitelib/%pname/lib/tsconfig.tsbuildinfo
find %buildroot%nodejs_sitelib/%pname -name '*.js.map' -delete
find %buildroot%nodejs_sitelib/%pname -mindepth 1 -maxdepth 1 -name '.*' -exec rm -rf {} +

%check
node -e '
const zmq = require("%buildroot%nodejs_sitelib/%pname");
for (const name of ["Subscriber", "Publisher", "Context"]) {
  if (typeof zmq[name] !== "function") {
    throw new Error(name + " is not exported");
  }
}
console.log("zeromq addon loaded, version:", zmq.version);
'

%files
%doc LICENSE.txt README.md
%nodejs_sitelib/%pname/

%changelog
* Fri Jul 10 2026 Alexander Burmatov <thatman@altlinux.org> 6.5.0-alt1
- Initial build for ALT.
- Build the native addon against the system libzmq instead of the bundled
  cmake-ts/vcpkg copy; patch the addon loader accordingly.
