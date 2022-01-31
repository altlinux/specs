%global _unpackaged_files_terminate_build 1

%define oname extjs

Name: javascript-%oname
Summary: Exr JS cross-browser JavaScript library
Version: 7.0.0
Release: alt1
License: GPL-3.0
Group: Development/Other
Url: https://www.sencha.com/legal/gpl/
Source: %name-%version.tar
# Patch: %%name-%%version.patch
BuildArch: noarch
Provides: libjs-%oname = %EVR
Provides: %oname = %EVR

Requires: javascript-common
BuildRequires(pre): rpm-macros-javascript

%description
Ext JS is a cross-browser JavaScript library for building rich internet
applications.

%prep
%setup
# %%patch -p1

%build
%install

mkdir -p %buildroot%_jsdir/%oname
cp -p -r build/classic/locale %buildroot%_jsdir/%oname
cp -p -r build/classic/theme-crisp %buildroot%_jsdir/%oname
cp -p -r build/classic/theme-classic %buildroot%_jsdir/%oname

cp -p build/ext-all-debug.js %buildroot%_jsdir/%oname
cp -p build/ext-all.js %buildroot%_jsdir/%oname
cp -p build/packages/charts/classic/charts-debug.js %buildroot%_jsdir/%oname
cp -p build/packages/charts/classic/charts.js %buildroot%_jsdir/%oname
cp -p -r build/packages/charts/classic/crisp %buildroot%_jsdir/%oname
cp -p -r build/packages/charts/classic/classic %buildroot%_jsdir/%oname

%files
%_jsdir/%oname

%changelog
* Tue Jan 25 2022 Alexey Shabalin <shaba@altlinux.org> 7.0.0-alt1
- Initial build.

