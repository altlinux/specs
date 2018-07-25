%define _unpackaged_files_terminate_build 1
%define node_module uglify-js

%def_without check

Name: node-uglify-js
Version: 2.8.22
Release: alt1

Summary: JavaScript parser, minifier, compressor and beautifier toolkit
License: BSD
Group: Development/Tools
Url: https://www.npmjs.com/package/uglify-js
# Source-git: https://github.com/mishoo/UglifyJS2

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(acorn)
BuildRequires: npm(async)
BuildRequires: npm(mocha)
BuildRequires: npm(optimist)
BuildRequires: npm(source-map)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
%summary.

%prep
%setup
%nodejs_fixdep yargs

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a bin lib tools package.json %buildroot/%nodejs_sitelib/%node_module

mkdir -p %buildroot%_bindir
ln -s %nodejs_sitelib/%node_module/bin/uglifyjs %buildroot%_bindir

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node -e 'require("./")'
node test/run-tests.js

%files
%doc LICENSE README.md
%_bindir/uglifyjs
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 2.8.22-alt1
- Initial build for Sisyphus
