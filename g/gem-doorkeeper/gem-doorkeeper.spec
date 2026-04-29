%define _unpackaged_files_terminate_build 1
%define  pkgname doorkeeper

Name: gem-%pkgname
Version: 5.8.2
Release: alt1

Summary: Doorkeeper is an OAuth 2 provider for Ruby on Rails / Grape 
License: MIT
Group: Development/Ruby
Url: https://github.com/doorkeeper-gem/doorkeeper
VCS: https://github.com/doorkeeper-gem/doorkeeper
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
Doorkeeper is a gem (Rails engine) that makes it easy to
introduce OAuth 2 provider functionality to your Ruby on 
Rails or Grape application.

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Aleksandr Dovydenkov <asd@altlinux.org> 5.8.2-alt1
- Initial build for ALT Linux.
