%define node_module md2html

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-%node_module
Version: 1.4.4
Release: alt1
Summary: @udx/md2html Magazine-Quality Markdown to HTML Converter
License: MIT
Group: Development/Other
URL: https://udx.dev/docs/cli/core/
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

AutoReq: no
AutoProv: no
Requires: node

%description
A sophisticated tool for converting markdown files into a single, visually
polished HTML document with magazine-quality styling. Perfect for creating
professional documentation, reports, and publications from markdown source
files.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/index.js \
 %buildroot%_bindir/%node_module

%files
%_bindir/%node_module
%nodejs_sitelib/%node_module
%doc README.md

%changelog
* Wed Aug 19 2026 Artyom Osipchuk <artos@altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus.
