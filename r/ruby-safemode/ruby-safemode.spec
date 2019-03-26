%define        pkgname safemode

Name:          ruby-%pkgname
Version:       1.3.5
Release:       alt2
Summary:       A library for safe evaluation of Ruby code based on ParseTree/RubyParser and Ruby2Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/safemode
# VCS:         https://github.com/svenfuchs/safemode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby2ruby

%description
%summary.

Provides Rails ActionView template handlers for ERB and Haml.

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
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir

%changelog
* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1
- Initial build for Sisyphus
