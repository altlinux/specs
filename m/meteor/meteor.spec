%define        _name meteor

Name:          %_name
Version:       2.2.0
Release:       alt0.1
Summary:       Meteor, the JavaScript App Platform
License:       MIT
Group:         Development/Other
Url:           https://www.meteor.com
Vcs:           https://github.com/meteor/meteor.git
Packager:      Node Team <node@packages.altlinux.ru>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-nodejs

%add_findreq_skiplist %%_libexecdir/%_name/**/*
Autoprov:      yes,noshebang,nopython,noperl,nosymlinks,noshell
Autoreq:       yes,noshebang,nopython,noperl,nosymlinks,noshell
Requires:      node
Requires:      npmjs-fibers

ExclusiveArch: x86_64

%description
Meteor is an ultra-simple environment for building modern web applications.

With Meteor you write apps:

* in modern JavaScript
* that send data over the wire, rather than HTML
* using your choice of popular open-source libraries


%prep
%setup

%install
mkdir -p %buildroot/%_libdir/%_name %buildroot/%_bindir
cp -rp * %buildroot/%_libdir/%_name
chmod a+x %buildroot/%_libdir/%_name/%_name
ln -s %_libdir/%_name/%_name %buildroot/%_bindir/%_name

%files
%_bindir/%_name
%_libdir/%_name


%changelog
* Fri Jun 11 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt0.1
- ^ 0.5.9 -> 2.2.0
- ! build

* Fri Jan 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.5.9-alt1
- %_name package built for Sisyphus
