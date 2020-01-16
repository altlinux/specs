%define        pname fibers

Name:          npmjs-%pname
Version:       4.0.3
Release:       alt1
Summary:       Fiber support for v8 and Node
License:       MIT
Group:         Development/Other
Url:           https://github.com/laverdet/node-fibers
Vcs:           https://github.com/laverdet/node-fibers.git
Packager:      Node Team <node@packages.altlinux.ru>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-nodejs

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
* Fri Jan 10 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- NPM.js package for %pname built for Sisyphus
