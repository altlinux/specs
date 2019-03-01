%define        pkgname rake-compiler-dock

Name:          gem-%pkgname
Version:       0.7.1
Release:       alt1
Summary:       Easy to use and reliable cross compiler environment for building Windows, Linux and JRuby binary gems.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rake-compiler/rake-compiler-dock
# VCS:         https://github.com/rake-compiler/rake-compiler-dock.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(test-unit)

%description
Easy to use and reliable cross compiler environment for building Windows, Linux
and JRuby binary gems.

It provides cross compilers and Ruby environments for 2.2 and newer versions of
the RubyInstaller and Linux runtime environments. They are prepared for use with
rake-compiler. It is used by many gems with C or JRuby extentions.

This is kind of successor of rake-compiler-dev-box. It is wrapped as a gem for
easier setup, usage and integration and is based on lightweight Docker
containers. It is also more reliable, since the underlying docker images are
versioned and immutable.


%package       doc
Summary:       Documentation files for %pkgname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{pkgname} gem.


%package       -n %pkgname
Summary:       Executable for %pkgname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executable for %{pkgname} gem.


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
* Thu Feb 28 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
