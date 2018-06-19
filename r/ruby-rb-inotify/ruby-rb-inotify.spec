%define pkgname rb-inotify
%define _unpackaged_files_terminate_build 1
%define gem_dir %ruby_libdir/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%define gem_instdir %gem_dir/gems
%define gem_docdir %gem_dir/doc
%define gem_cache %gem_dir/cache

Name: ruby-%pkgname
Version: 0.9.10
Release: alt2

Summary: A thorough inotify wrapper for Ruby using FFI
License: MIT
Group: Development/Ruby
Url: https://github.com/guard/rb-inotify/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source: %pkgname-%version.tar
Patch1: ruby-rb-inotify-alt-no-git.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(bundler\/setup)/d
%filter_from_requires /^ruby(spec_helper)/d

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -n %pkgname-%version
%patch1 -p1

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
%doc README.md
%gem_dir
%exclude %gem_cache
%exclude %gem_docdir

%files doc
%gem_docdir

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.9.10-alt2
- Rebuild as ruby gem for openqa

* Thu Sep 28 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus
