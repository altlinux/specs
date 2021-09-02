%define        gemname dalli

Name:          gem-dalli
Version:       2.7.11
Release:       alt1
Summary:       High performance memcached client for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/petergoldstein/dalli
Vcs:           https://github.com/petergoldstein/dalli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: memcached

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-dalli < %EVR
Provides:      ruby-dalli = %EVR
Provides:      gem(dalli) = 2.7.11


%description
Dalli is a high performance pure Ruby client for accessing memcached servers. It
works with memcached 1.4+ only as it uses the newer binary protocol. It should
be considered a replacement for the memcache-client gem.

The name is a variant of Salvador Dali for his famous painting The Persistence
of Memory.


%package       -n gem-dalli-doc
Version:       2.7.11
Release:       alt1
Summary:       High performance memcached client for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dalli
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dalli) = 2.7.11

%description   -n gem-dalli-doc
High performance memcached client for Ruby documentation files.

Dalli is a high performance pure Ruby client for accessing memcached servers. It
works with memcached 1.4+ only as it uses the newer binary protocol. It should
be considered a replacement for the memcache-client gem.

The name is a variant of Salvador Dali for his famous painting The Persistence
of Memory.

%description   -n gem-dalli-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dalli.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-dalli-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.7.11-alt1
- ^ 2.7.10 -> 2.7.11

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.10-alt1
- Use Ruby Policy 2.0
- Bump to 2.7.10

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.6-alt1
- Initial build in Sisyphus
