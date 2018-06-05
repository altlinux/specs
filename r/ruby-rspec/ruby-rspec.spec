%define  pkgname rspec

Name:    ruby-%pkgname
Version: 3.7.0
Release: alt1

Summary: RSpec meta-gem that depends on the other components
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rspec/rspec

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%changelog
* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus
