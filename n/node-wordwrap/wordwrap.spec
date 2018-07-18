%define _unpackaged_files_terminate_build 1
%define node_module wordwrap

%def_without check

Name: node-wordwrap
Version: 1.0.0
Release: alt1

Summary: Word wrapping library for node
License: MIT
Group: Development/Other
Url: https://www.npmjs.com/package/wordwrap
# Source-git: https://github.com/substack/node-wordwrap.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(tape)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
Wrap those words. Show them at what columns to start and stop.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json index.js %buildroot/%nodejs_sitelib/%node_module

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node -e 'require("./")'
ln -sf .. node_modules/wordwrap
tape test/*.js

%files
%doc LICENSE README.markdown
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
