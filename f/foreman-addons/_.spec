# vim: set ft=spec: -*- rpm-spec -*-
Name:          foreman-addons
Version:       0.0.4
Release:       alt1
Summary:       Default addons for Foreman
License:       GPLv3
Group:         Development/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        modules.tar
Source1:       Gemfile
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby

Conflicts:     smart-proxy-dynflow-core
Requires:      gem-ed25519
Requires:      gem-bcrypt-pbkdf
Requires:      node-gyp
#Requires:      npm(react-json-tree)
#Requires:      npm(react-base16-styling)
#Requires:      npm(base16)
#Requires:      npm(babel-plugin-module-resolver)

Autoreq:       yes,nopython

%description
%summary.

%prep
tar -xf %SOURCE0
%patch
find -name 'package.json' -exec rm -rf "{}" \;

%build
%ruby_build --use=foreman-tasks-core --alias=foreman-addons --join=bin:lib \
            --use=foreman-tasks --alias=foreman-addons --join=bin:lib \
            --use=foreman_templates --alias=foreman-addons --join=bin:lib \
            --use=foreman_ansible --alias=foreman-addons --join=bin:lib \
            --use=foreman_ansible_core --alias=foreman-addons --join=bin:lib \
            --use=foreman_discovery --alias=foreman-addons --join=bin:lib \
            --use=foreman_remote_execution_core --alias=foreman-addons --join=bin:lib \
            --use=foreman_remote_execution --alias=foreman-addons --join=bin:lib \
            --use=smart_proxy_dynflow_core --alias=foreman-addons --join=bin:lib \
            --use=smart_proxy_dynflow --alias=foreman-addons --join=bin:lib \
            --use=smart_proxy_remote_execution_ssh --alias=foreman-addons --join=bin:lib

%install
%ruby_install
install -Dm0644 smart_proxy_dynflow_core-0.2.6/deploy/smart_proxy_dynflow_core.service %buildroot%_unitdir/smart-proxy-dynflow-core.service
install -Dm0644 smart_proxy_dynflow_core-0.2.6/config/settings.yml.example %buildroot%_sysconfdir/smart_proxy_dynflow_core/settings.yml
mkdir -p %buildroot%_sharedstatedir/smart-proxy-dynflow-core \
         %buildroot/run/smart-proxy-dynflow-core
#TODO move to setup.rb
install -Dm0644 %SOURCE1 %buildroot%_sharedstatedir/smart-proxy-dynflow-core/Gemfile


%files
%_bindir/*
%ruby_gemspecdir/*
%ruby_gemslibdir/*
%_unitdir/*
%attr(770,_smartforeman,foreman) %_sharedstatedir/smart-proxy-dynflow-core
%attr(770,_smartforeman,foreman) /run/smart-proxy-dynflow-core
%config(noreplace) %_sysconfdir/smart_proxy_dynflow_core/*

%post
%post_service smart-proxy-dynflow-core

%preun
railsctl cleanup %name
%preun_service smart-proxy-dynflow-core


%changelog
* Tue Mar 09 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- ^ some gems to newer patch version
- - precompiled public from precompiled gems

* Tue Feb 09 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt2
- + requires to ed25519 and bcrypt_pbkdf for smart_proxy_dynflow_core gem
- ! smart_proxy_dynflow_core gem to support new ssh option

* Thu Jan 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1.1
- ! post and preus scripts

* Fri Jan 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1
- + supplement files (service and init) for "smart_proxy_dynflow_core" gem
- + 3 modules for old foreman
- ! modules aliases and thus requires

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- 6 modules added for old foreman

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + defaultly packaged
