Name:          ruby2ruby
Version:       2.4.2
Release:       alt2
Summary:       ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby2ruby
# VCS:         https://github.com/seattlerb/ruby2ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-sexp-processor
BuildRequires: ruby-parser
BuildRequires: ruby-hoe

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%prep
%setup

%build
%gem_build --use ruby2ruby --join=lib:bin

%install
%gem_install

%check
%gem_test

%files
%doc README*
%_bindir/r2r_show
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Sat Mar 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt2
- Use Ruby Policy 2.0
- Bump to 2.4.2

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
