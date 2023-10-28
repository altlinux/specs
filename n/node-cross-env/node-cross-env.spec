%define _unpackaged_files_terminate_build 1
%define node_module cross-env

%def_without check

Name:    node-cross-env
Version: 7.0.3
Release: alt1

Summary: Cross platform setting of environment scripts
License: MIT
Group:   Other
URL:     https://www.npmjs.com/package/cross-env
VCS:     https://github.com/kentcdodds/cross-env

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
#BuildRequires: rpm-build-nodejs
#BuildRequires: node

%if_with check
BuildRequires: npm(hashish)
BuildRequires: npm(chai)
BuildRequires: npm(mocha)
%endif

Provides: nodejs-%node_module = %EVR

BuildArch: noarch

%description
Run scripts that set and use environment variables across platforms.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/ %buildroot%_bindir/
cp -a src %buildroot%nodejs_sitelib/%node_module/
cp -a package.json %buildroot%nodejs_sitelib/%node_module/
chmod +x %buildroot%nodejs_sitelib/%node_module/src/bin/*
rm -rf %buildroot%nodejs_sitelib/%node_module/src/__tests__
ln -s %nodejs_sitelib/%node_module/src/bin/%node_module.js \
    %buildroot%_bindir/%node_module
ln -s %nodejs_sitelib/%node_module/src/bin/%node_module-shell.js \
    %buildroot%_bindir/%node_module-shell

%check

%files
%doc *.md
%_bindir/%node_module
%_bindir/%node_module-shell
%nodejs_sitelib/%node_module

%changelog
* Fri Oct 27 2023 Andrey Limachko <liannnix@altlinux.org> 7.0.3-alt1
- Initial build for Sisyphus
