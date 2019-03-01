%define        pkgname coveralls

Name:          gem-%pkgname
Version:       0.8.22
Release:       alt1
Summary:       Coveralls for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lemurheavy/coveralls-ruby
# VCS:         https://github.com/lemurheavy/coveralls-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%gem_replace_version thor ~> 0.19

%description
Coveralls was designed with Ruby projects in mind, and we've made it as easy as
we possibly can to get started.


%package       doc
Summary:       Documentation files for %pkgname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{pkgname}.


%package       -n %pkgname
Summary:       Executable for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executable for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.22-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
