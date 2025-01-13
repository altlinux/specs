Name: wiki-js
Version: 2.5.305
Release: alt1
Summary: A modern and powerful wiki app built on Node.js
License: AGPL-3.0
Group: System/Servers
Url: https://js.wiki
VCS: https://github.com/requarks/wiki

Source: %name-%version.tar
Source1: node_modules.tar
Source2: %name.service
Patch: alt-fix-config-dir.patch
Patch1: alt-fix-node-options.patch

BuildRequires: yarn
BuildRequires: /proc

%add_findreq_skiplist %_libexecdir/%name/node_modules/**/*
%add_findprov_skiplist %_libexecdir/%name/node_modules/**/*

%description
A modern, lightweight and powerful wiki app built on NodeJS, Git and Markdown.

%prep
# npm install --force
# find node_modules -type f -name "*.node" -exec rm -vf {} \;
# git add node_modules -f && git commit -m "Updated node modules."
%setup -a 1
%patch -p1
%if "%(rpmvercmp '%{get_version node}' '17.0.0')" < "0"
# node < v17 not supported option openssl-legacy-provider
%patch1 -p1
%endif
sed -i -e '/version/s/2.0.0/%version/' -e '/dev/s/true/false/' package.json
sed -i '/dataPath/s|./data|%_sharedstatedir/%name/data|' config.sample.yml

%build
yarn run --offline build

%install
mkdir -p %buildroot%_unitdir \
         %buildroot%_sysconfdir/%name \
         %buildroot%_libexecdir/%name \
         %buildroot%_sharedstatedir/%name
install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 config.sample.yml %buildroot%_sysconfdir/%name/config.yml
cp -r server assets node_modules package.json %buildroot%_libexecdir/%name

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -g %name -s /sbin/nologin %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_libexecdir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.yml
%dir %attr(750, %name, %name) %_sharedstatedir/%name
%doc LICENSE

%changelog
* Sun Jan 12 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.5.305-alt1
- Initial build for ALT.
