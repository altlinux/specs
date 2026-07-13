%define _unpackaged_files_terminate_build 1
%define node_module pnpm

Name:           pnpm
Version:        11.5.0
Release:        alt1

Summary:        Fast, disk space efficient package manager for Node.js
License:        MIT
Group:          Development/Tools
Url:            https://pnpm.io
Vcs:            https://github.com/pnpm/pnpm

Source0:        %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs

BuildArch:      noarch

Requires:       node >= 22.13
Requires:       /usr/bin/node

# self-contained bundle with vendored node_modules: no module deps to generate
AutoReq:        no
AutoProv:       no

Provides:       node-%node_module = %version-%release

%description
pnpm is a fast, disk space efficient package manager for Node.js. It uses a
content-addressable store and hard links so that a package version is stored
on disk only once, and creates a strict, non-flat node_modules layout.

This package ships the upstream-built distribution and runs on the system
Node.js interpreter.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%name
mkdir -p %buildroot%_bindir

cp -a . %buildroot%nodejs_sitelib/%name/

rm -rf %buildroot%nodejs_sitelib/%name/dist/vendor/*.exe
rm -rf %buildroot%nodejs_sitelib/%name/dist/node_modules/@reflink/reflink-win32-* \
       %buildroot%nodejs_sitelib/%name/dist/node_modules/@reflink/reflink-darwin-*

ln -s %nodejs_sitelib/%name/bin/pnpm.mjs %buildroot%_bindir/pnpm
ln -s %nodejs_sitelib/%name/bin/pnpx.mjs %buildroot%_bindir/pnpx
ln -s %nodejs_sitelib/%name/bin/pnpm.mjs %buildroot%_bindir/pn
ln -s %nodejs_sitelib/%name/bin/pnpx.mjs %buildroot%_bindir/pnx

%files
%doc README.md LICENSE
%_bindir/pnpm
%_bindir/pnpx
%_bindir/pn
%_bindir/pnx
%nodejs_sitelib/%name/

%changelog
* Tue Jun 02 2026 Anton Politov <ampernic@altlinux.org> 11.5.0-alt1
- Initial build.
