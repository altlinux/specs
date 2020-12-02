%define        pkgname faraday

Name:          gem-%pkgname
Version:       0.17.3
Release:       alt1
Summary:       Simple, but flexible HTTP client library, with support for multiple backends
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday
Vcs:           https://github.com/lostisland/faraday.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-multipart-post

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Faraday is an HTTP client lib that provides a common interface over many
adapters (such as Net::HTTP) and embraces the concept of Rack middleware when
processing the request/response cycle.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.17.3-alt1
- ^ 0.15.4 -> 0.17.3
- ! spec tags

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.15.4-alt1
- > Ruby Policy 2.0
- ^ 0.15.2 -> 0.15.4

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
