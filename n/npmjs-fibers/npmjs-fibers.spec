%define        pname fibers

Name:          npmjs-%pname
Version:       4.0.3
Release:       alt2
Summary:       Fiber support for v8 and Node
License:       MIT
Group:         Development/Other
Url:           https://github.com/laverdet/node-fibers
Vcs:           https://github.com/laverdet/node-fibers.git
Packager:      Node Team <node@packages.altlinux.ru>

Source:        %name-%version.tar
BuildRequires: rpm-build-nodejs

%description
Fibers, sometimes called coroutines, are a powerful tool which expose an API to
jump between multiple call stacks from within a single thread. This can be
useful to make code written for a synchronous library play nicely in an
asynchronous environment.


%prep
%setup
#sed "s/\('cflags': \[ \).*\( \].*\)/\1'-O2', '-fpic'\2/" -i binding.gyp

%build
%npm_build

%install
%npm_install

%files
%doc README.md
%nodejs_sitelib/%pname


%changelog
* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt2
- BR: rpm-build-nodejs

* Fri Jan 10 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- NPM.js package for %pname built for Sisyphus
