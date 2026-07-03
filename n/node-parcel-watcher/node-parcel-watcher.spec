%define pname @parcel/watcher

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-parcel-watcher
Version: 2.5.6
Release: alt1

Summary: Native C++ Node.js module for filesystem events
License: MIT
Group: Development/Other
Url: https://github.com/parcel-bundler/watcher
Vcs: https://github.com/parcel-bundler/watcher.git

Source: %name-%version.tar

ExclusiveArch: %nodejs_arches

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node node-devel node-gyp node-addon-api
BuildRequires: gcc-c++ make

Requires: node
Requires: node-detect-libc >= 2.0.3
Requires: node-is-glob >= 4.0.3
Requires: node-picomatch >= 4.0.3

Provides: npm(@parcel/watcher) = %version
Provides: nodejs-parcel-watcher = %EVR

%description
@parcel/watcher is a native Node.js module for querying and subscribing to
filesystem events. It provides recursive file watching with platform backends
for Linux, macOS, Windows, FreeBSD, Watchman, and WASM.

%prep
%setup
touch .npmignore

%build
%npm_build

%install
%npm_install

rm -rf %buildroot%nodejs_sitelib/%pname/{src,test,wasm,scripts,watchman,binding.gyp,Makefile}
rm -f %buildroot%nodejs_sitelib/%pname/{yarn.lock,index.js.flow,.editorconfig,.prettierrc}

%files
%doc LICENSE README.md
%nodejs_sitelib/%pname/

%changelog
* Thu Jul 02 2026 Grant Makyan <karonus@altlinux.org> 2.5.6-alt1
- Initial build for ALT.
