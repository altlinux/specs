%define        pkgname faraday

Name: 	       ruby-%pkgname
Version:       0.15.4
Release:       alt1
Summary:       Simple, but flexible HTTP client library, with support for multiple backends
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-multipart-post

%description
Faraday is an HTTP client lib that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.4-alt1
- Bump to 0.15.4
- Use Ruby Policy 2.0

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Jul 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.2-alt1
- new version 0.15.2

* Sat Oct 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1.1
- Rebuild with Ruby 2.4.1

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.12.1-alt1
- Initial build in Sisyphus
