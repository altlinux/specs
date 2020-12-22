# vim: set ft=spec: -*- rpm-spec -*-
Name:          foreman-addons
Version:       0.0.2
Release:       alt1
Summary:       Default addons for Foreman
License:       GPLv3
Group:         Development/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        modules.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

%prep
tar -xf %SOURCE0

%build
%ruby_build --use=foreman-tasks-core --alias=foreman-addons,foreman_ansible_core --join=bin:lib \
            --use=foreman_remote_execution --alias=foreman-addons --join=bin:lib \
            --use=foreman_templates --alias=foreman-addons --join=bin:lib \
            --use=foreman-tasks --alias=foreman-addons --join=bin:lib \
            --use=foreman_ansible --alias=foreman-addons --join=bin:lib \
            --use=foreman_discovery --alias=foreman-addons --join=bin:lib \
            --use=foreman_remote_execution_core --alias=foreman-addons --join=bin:lib 

%install
%ruby_install

%files
%ruby_gemspecdir/*
%ruby_gemslibdir/*

%changelog
* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- 6 modules added for old foreman

* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- + defaultly packaged
