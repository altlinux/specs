%define        pkgname nori

Name:          gem-%pkgname
Version:       2.6.0
Release:       alt1
Summary:       XML to Hash translator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/nori
# VCS:         https://github.com/savonrb/nori.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

Really simple XML parsing ripped from Crack which ripped it from Merb.
Nori was created to bypass the stale development of Crack, improve its XML parse
and fix certain issues.

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

%files doc
%ruby_gemdocdir

%changelog
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
