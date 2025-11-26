%define _unpackaged_files_terminate_build 1
%define node_module prettier

Name: %node_module
Version: 3.6.2
Release: alt1

Summary: Opinionated code formatter
License: MIT
Group: Development/Tools

URL: https://prettier.io/
VCS: https://github.com/prettier/prettier
Source0: %name-%version.tar
Source1: %name-node_modules.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs

Provides: node-%node_module

ExclusiveArch: x86_64

%description
Prettier is an opinionated code formatter. It enforces a consistent
style by parsing your code and re-printing it with its own rules
that take the maximum line length into account, wrapping code when
necessary.

Prettier can be run in your editor on-save, in a pre-commit hook,
or in CI environments to ensure your codebase has a consistent
style without devs ever having to post a nit-picky comment on a
code review ever again!

%prep
%setup -a1


%build
npm run build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
mkdir -p %buildroot%_bindir/

cp -a dist/* %buildroot%nodejs_sitelib/%node_module
ln -s %nodejs_sitelib/%node_module/%node_module/bin/%node_module.cjs %buildroot%_bindir/%node_module

%files
%doc README.md LICENSE
%_bindir/%name
%nodejs_sitelib/%node_module/

%changelog
* Wed Nov 26 2025 David Sultaniiazov <x1z53@altlinux.org> 3.6.2-alt1
- Initial build.
