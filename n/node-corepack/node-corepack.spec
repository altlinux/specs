%define node_module corepack

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-corepack
Version: 0.10.0
Release: alt2
Summary: Bridge between Node projects and their package managers
License: MIT License
Group: Development/Other
Url: https://github.com/nodejs/corepack.git
Vcs: https://github.com/nodejs/corepack.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: /proc
BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
Provides: nodejs-%node_module = %EVR
Requires: node

AutoReq: no
AutoProv: no

%description
Corepack is a zero-runtime-dependency Node.js script that acts as a bridge
between Node.js projects and the package managers they are intended to be used
with during development. In practical terms, **Corepack will let you use
Yarn and pnpm without having to install them** - just like what currently
happens with npm, which is shipped by Node.js by default.

**Important:** At the moment, Corepack only covers Yarn and pnpm.
Given that we have little control on the npm project, we prefer to focus
on the Yarn and pnpm use cases.
As a result, Corepack doesn't have any effect at all on the way you use npm.

%prep
%setup

%build
YARN_ENABLE_PROGRESS_BARS=false .yarn/releases/yarn-3.0.0.cjs build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a dist %buildroot%nodejs_sitelib/%node_module
cp -a shims %buildroot%nodejs_sitelib/%node_module
chmod a+x %buildroot%nodejs_sitelib/%node_module/dist/*.js
rm -rf %buildroot%nodejs_sitelib/%node_module/shims/nodewin
rm -f %buildroot%nodejs_sitelib/%node_module/shims/*.{cmd,ps1}
cp -a package.json %buildroot%nodejs_sitelib/%node_module

ln -sr %buildroot%nodejs_sitelib/%node_module/dist/corepack.js %buildroot%_bindir/corepack

%files
%doc README.md
%_bindir/*
%nodejs_sitelib/%node_module

%changelog
* Tue Apr 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt2
- Fix install files.

* Tue Apr 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt1
- Initial build.

