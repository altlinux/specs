%define _unpackaged_files_terminate_build 1
%define  pkgname sass
%define gem_dir %ruby_libdir/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%define gem_instdir %gem_dir/gems
%define gem_docdir %gem_dir/doc
%define gem_cache %gem_dir/cache

Name:    ruby-%pkgname
Version: 3.5.6
Release: alt2

Summary: Sass makes CSS fun again.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sass/sass

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(compass)/d
%filter_from_requires /^ruby(mock_importer)/d

%description
Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

Requires: %name = %EVR

%description doc
Documentation files for %{name}.

%package tests
Summary: Tests for %name
Group: Development/Ruby
Requires: %name = %EVR

%description tests
Tests for %name.

%prep
%setup -n %pkgname-%version


%build
gem build %pkgname.gemspec

%install
# install first to temp directory instead of buildroot due to invalid file owner of some files installed by 'gem install'
mkdir -p .%pkgname
gem install -V --local --build-root .%pkgname --force --document=ri,rdoc %pkgname-%version.gem
cp -a .%pkgname %buildroot

%check
pushd .%pkgname
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%doc MIT-LICENSE README.md
%_bindir/*
%gem_dir
%exclude %gem_cache
%exclude %gem_instdir/%pkgname-%version/test
%exclude %gem_docdir

%files tests
%gem_instdir/%pkgname-%version/test

%files doc
%gem_docdir

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 3.5.6-alt2
- Rebuild as ruby gem for openqa

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- Initial build for Sisyphus
