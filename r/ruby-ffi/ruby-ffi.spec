%define pkgname ffi

%global gem_dir %ruby_libdir/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%global gem_instdir %gem_dir/gems
%global gem_docdir %gem_dir/doc
%global gem_cache %gem_dir/cache

Name: ruby-%pkgname
Version: 1.9.23
Release: alt2

Summary: Ruby foreign function interface
Group: Development/Ruby
License: BSD
Url: https://github.com/ffi/ffi

Source: %pkgname-%version.tar
Patch1: %name-alt-fix-requires.patch
Patch2: ruby-ffi-alt-gemspec.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel libruby-devel ruby-tool-setup

%filter_from_requires \,^ruby(lib/ffi/.*generator),d
%filter_from_requires /^ruby(spec)/d

%description
A Ruby foreign function interface.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

Requires: %name = %EVR

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch1 -p1
%patch2 -p1

%build
gem build %pkgname.gemspec

%install
# install first to temp directory instead of buildroot due to invalid file owner of some files installed by 'gem install'
mkdir -p .%pkgname
gem install -V --local --build-root .%pkgname --force --document=ri,rdoc %pkgname-%version.gem
cp -a .%pkgname %buildroot

# Remove some cruft
rm -rf %buildroot%gem_instdir/%pkgname-%version/ext
rm -rf %buildroot%gem_instdir/%pkgname-%version/setup.rb
find %buildroot%gem_dir -name gem.build_complete -delete
find %buildroot%gem_dir -name gem_make.out -delete
find %buildroot%gem_dir -name mkmf.log -delete

%check
pushd .%pkgname
ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%doc README.md LICENSE
%gem_dir
%exclude %gem_cache
%exclude %gem_docdir
%exclude %gem_instdir/%pkgname-%version/samples

%files doc
%gem_docdir
%gem_instdir/%pkgname-%version/samples

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.9.23-alt2
- Rebuild as ruby gem for openqa

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Feb 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.23-alt1
- New version.

* Fri Feb 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.22-alt1
- New version.

* Tue Feb 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.21-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt2
- Rebuild with new %%ruby_sitearchdir location

* Sat Mar 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.18-alt1
- New version

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.17-alt1
- new version 1.9.17
- fix module requires pathes

* Sat Sep 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.14-alt1
- new version 1.9.14

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version
- Fix project URL

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.6.3-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Dec 07 2012 Led <led@altlinux.ru> 0.6.3-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build

* Fri Aug 13 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.3-alt1
- 0.6.3
- Rebuild with new libffi

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.3.5-alt1
- Built for Sisyphus
