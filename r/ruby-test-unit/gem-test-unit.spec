%define        pkgname test-unit

Name:          ruby-%pkgname
Epoch:         1
Version:       3.3.1
Release:       alt1
Summary:       An xUnit family unit testing framework for Ruby
License:       GPLv2
Group:         Development/Ruby
Url:           http://test-unit.github.io/
# VCS:         https://github.com/test-unit/test-unit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(yard)

%description
An xUnit family unit testing framework for Ruby.

test-unit (Test::Unit) is unit testing framework for Ruby, based on xUnit
principles. These were originally designed by Kent Beck, creator of extreme
programming software development methodology, for Smalltalk's SUnit. It allows
writing tests, checking results and automated testing in Ruby.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
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
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.3.1-alt1
- Bump to 3.3.1
- Use Ruby Policy 2.0

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 1:3.2.9-alt1
- Bump to 3.2.9

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.3-alt1
- Initial build for Sisyphus, packaged as a gem
