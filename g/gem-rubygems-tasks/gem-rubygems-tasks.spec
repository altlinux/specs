%define        pkgname rubygems-tasks

Name:          gem-%pkgname
Version:       0.2.4
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/postmodern/rubygems-tasks
# VCS:         https://github.com/postmodern/rubygems-tasks.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

The Rake tasks which you use to manage a Ruby project should not be coupled
to the project generator which you used to create the project. Project
generators have nothing to do with the Rake tasks used to build, install and
release a Ruby project.

Recently, many Ruby Developers began creating Ruby projects by hand,
building/releasing RubyGems using gem build / gem push. Sometimes this resulted
in RubyGems being released with uncommitted changes, or the developer forgetting
to tag the release. Ruby Developers should have access to agnostic and
unobtrusive Rake tasks, to automate the release process.

This is what rubygems-tasks seeks to provide.


%package       doc
Summary:       Documentation files for %pkgname
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %pkgname

%prep
%setup

%build
%gem_build

%install
%gem_show
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
