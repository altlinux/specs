%define _unpackaged_files_terminate_build 1
%define node_module yargs

%def_without check

Name: node-yargs
Version: 3.2.1
Release: alt1

Summary: Light-weight option parsing with an argv hash
License: MIT
Group: Development/Tools
Url: https://www.npmjs.com/package/yargs
# Source-git: https://github.com/yargs/yargs.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(hashish)
BuildRequires: npm(chai)
BuildRequires: npm(mocha)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
Yargs helps to build interactive command line tools, by parsing arguments and
generating an elegant user interface.

%prep
%setup
%nodejs_fixdep window-size
%nodejs_fixdep wordwrap

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json lib index.js %buildroot/%nodejs_sitelib/%node_module

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
mocha -R nyan

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
