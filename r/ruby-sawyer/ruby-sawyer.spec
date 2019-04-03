%define        pkgname sawyer

Name: 	       ruby-%pkgname
Version:       0.8.1
Release:       alt2
Summary:       Secret User Agent of HTTP
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/sawyer
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest)
BuildRequires: ruby-faraday
BuildRequires: ruby-addressable
%gem_replace_version addressable ~> 2.3

%description
Sawyer is an experimental hypermedia agent for Ruby built on top of Faraday.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem

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
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.1-alt2
- Use Ruby Policy 2.0
- Increase gem addressable dep to ~> 2.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.1-alt1
- Initial build in Sisyphus
