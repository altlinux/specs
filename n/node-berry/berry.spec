%define _unpackaged_files_terminate_build 1
%define pname berry

Name: node-berry
Version: 4.14.1
Release: alt1
Summary: active development trunk for Yarn.
License: BSD-2-Clause
Group: Development/Tools
Url: https://yarnpkg.com/
Vcs: https://github.com/yarnpkg/berry

BuildArch: noarch

Source: %name-%version.tar
#Source1: node_module.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node 

Conflicts: yarn

%description
Yarn is a modern package manager split into various packages.
Its novel architecture allows to do things currently impossible with existing solutions:

%prep
%setup

%build
%npm_build
node packages/yarnpkg-cli/bin/yarn.js install --immutable

%install
%npm_install
mkdir -p %buildroot%_bindir

install -Dpm0755 packages/yarnpkg-cli/bin/yarn.js %buildroot%_bindir/yarn
ln -s yarn %buildroot%_bindir/yarnpkg

%files
%doc *.md
%_bindir/yarn
%_bindir/yarnpkg
%nodejs_sitelib/%pname

%changelog
* Wed Sep 30 2026 Pavel Shilov <zerospirit@altlinux.org> 4.14.1-alt1
- Initial build for Sisyphus.

