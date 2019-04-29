%define        pkgname  opener

Name:          gem-%pkgname
Version:       0.1.0
Release:       alt1
Summary:       A 33-line alternative to Ruby's launchy gem
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/sunaku/opener
# VCS:         https://github.com/sunaku/opener.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Opener is a Ruby library for opening things in an cross-platform way.

It is a tiny (33 lines of code) alternative to the launchy library.


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
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
