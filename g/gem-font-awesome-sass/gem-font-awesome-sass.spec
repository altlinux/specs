%define        pkgname font-awesome-sass

Name:          gem-%pkgname
Version:       5.8.1
Release:       alt1
Summary:       Font-Awesome SASS gem for use in Ruby projects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/FortAwesome/font-awesome-sass
%vcs           https://github.com/FortAwesome/font-awesome-sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
'font-awesome-sass' is a Sass-powered version of FontAwesome for your Ruby
projects and plays nicely with Ruby on Rails, Compass, Sprockets, etc.

Refactored to support more Ruby environments with code and documentation humbly
used from the excellent bootstrap-sass project by the Bootstrap team.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


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

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.8.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
