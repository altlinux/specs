%define node_module bower

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-%node_module
Version: 1.8.14
Release: alt1
Summary: A package manager for the web
License: MIT License
Group: Development/Other
Url: https://bower.io
Vcs: https://github.com/bower/bower.git
Source: %name-%version.tar
# Source1: %name-production-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-intro >= 1.9.18
BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
Requires: node >= 0.10.0

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no

%description
Bower offers a generic, unopinionated solution to the problem of front-end
package management, while exposing the package dependency model via
an API that can be consumed by a more opinionated build stack.
There are no system wide dependencies, no dependencies are shared between
different apps, and the dependency tree is flat.

Bower runs over Git, and is package-agnostic.
A packaged component can be made up of any type of asset, and use any type
of transport (e.g., AMD, CommonJS, etc.).

%prep
# %setup -a 1
%setup

%build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a * %buildroot/%nodejs_sitelib/%node_module/
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/bower %buildroot%_bindir/%node_module
rm -rf %buildroot/%nodejs_sitelib/%node_module/test

%files
%doc README.md
%_bindir/%node_module
%nodejs_sitelib/%node_module

%changelog
* Wed Sep 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.8.14-alt1
- Initial build for Sisyphus.


