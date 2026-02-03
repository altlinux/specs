%global _unpackaged_files_terminate_build 1
%define name_orig rake-release
%def_with check

Name: gem-rake-release
Version: 1.4.0
Release: alt1
Summary: Customized fork for bundlers gem task helpers
License: MIT
Group: Development/Ruby
Url: https://rubygems.org/gems/rake-release
Vcs: https://github.com/jgraichen/rake-release

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby
BuildRequires: bundle

%description
Automatically detects multiple gemspecs and protect from releasing code
not matching git version tag.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspecdir/%name_orig-%version.gemspec
%ruby_gemslibdir/%name_orig-%version
%ruby_gemsdocdir/%name_orig-%version
%doc LICENSE README.md

%changelog
* Fri Jan 30 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.4.0-alt1
- Initial built for ALT Sisyphus.
