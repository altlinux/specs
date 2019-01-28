%define _unpackaged_files_terminate_build 1
%define  pkgname packaging

Name:    ruby-%pkgname
Version: 0.99.22
Release: alt1

Summary: Packaging automation for Puppet software
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/packaging

BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

Requires: ruby-bundler


%description
This is a repository for packaging automation for Puppet software. The goal is 
to abstract and automate packaging processes beyond individual software 
projects to a level where this repo can be cloned inside any project.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README* LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*


%changelog
* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.99.22-alt1
- Version updated to 0.99.22

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.99.20-alt1
- Initial build for Sisyphus

