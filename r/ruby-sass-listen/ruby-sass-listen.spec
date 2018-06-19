%define _unpackaged_files_terminate_build 1
%define  pkgname sass-listen
%define gem_dir %ruby_libdir/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%define gem_docdir %gem_dir/doc
%define gem_cache %gem_dir/cache


Name:    ruby-%pkgname
Version: 4.0.0
Release: alt2

Summary: The Listen gem listens to file modifications and notifies you about the changes
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sass/listen

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch1: ruby-listen-alt-no-git.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(wdm)/d
%filter_from_requires /^ruby(rb-fsevent)/d
%filter_from_requires /^ruby(rb-kqueue)/d

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

Requires: %name = %EVR

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1


sed -i -e "/rb-fsevent/d" %pkgname.gemspec
sed -i -e "/rb-kqueue/d" %pkgname.gemspec
sed -i -e "/wdm/d" %pkgname.gemspec

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
%doc README.md CHANGELOG.md CONTRIBUTING.md
%gem_dir
%exclude %gem_cache
%exclude %gem_docdir

%files doc
%gem_docdir

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.0.0-alt2
- Rebuild as ruby gem for openqa

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
