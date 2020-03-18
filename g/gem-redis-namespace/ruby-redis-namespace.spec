%define        pkgname redis-namespace

Name:          gem-%pkgname
Version:       1.7.0
Release:       alt1
Summary:       This gem adds a Redis::Namespace class which can be used to namespace Redis keys
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/resque/redis-namespace
Vcs:           https://github.com/resque/redis-namespace.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Sat Mar 07 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- > Ruby Policy 2.0
- ^ 1.6.0 -> 1.7.0
- ! spec

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
