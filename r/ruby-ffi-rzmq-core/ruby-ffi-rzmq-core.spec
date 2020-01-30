%define        pkgname ffi-rzmq-core

Name:          ruby-%pkgname
Version:       1.0.7
Release:       alt1
Summary:       FFI wrapper for the ZeroMQ networking library
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)

%description
This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library.
Project can be used by any other zeromq gems that want to provide their own high-level Ruby API.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation


%description   doc
Documentation files for %gemname gem.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemsdocdir/*

%changelog
* Thu Jan 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt1
- Initial build.
