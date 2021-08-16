%define        gemname request_store

Name:          gem-request-store
Version:       1.5.0
Release:       alt1
Summary:       Per-request global storage for Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/steveklabnik/request_store/
Vcs:           https://github.com/steveklabnik/request_store.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack) >= 1.4
BuildRequires: gem(rake) >= 10.5 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(rack) >= 1.4
Obsoletes:     ruby-request_store < %EVR
Provides:      ruby-request_store = %EVR
Provides:      gem(request_store) = 1.5.0


%description
Ever needed to use a global variable in Rails? Ugh, that's the worst. If you
need global state, you've probably reached for Thread.current.


%package       -n gem-request-store-doc
Version:       1.5.0
Release:       alt1
Summary:       Per-request global storage for Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета request_store
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(request_store) = 1.5.0

%description   -n gem-request-store-doc
Per-request global storage for Rack documentation files.

Ever needed to use a global variable in Rails? Ugh, that's the worst. If you
need global state, you've probably reached for Thread.current.

%description   -n gem-request-store-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета request_store.


%package       -n gem-request-store-devel
Version:       1.5.0
Release:       alt1
Summary:       Per-request global storage for Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета request_store
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(request_store) = 1.5.0
Requires:      gem(rake) >= 10.5 gem(rake) < 14
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6

%description   -n gem-request-store-devel
Per-request global storage for Rack development package.

Ever needed to use a global variable in Rails? Ugh, that's the worst. If you
need global state, you've probably reached for Thread.current.

%description   -n gem-request-store-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета request_store.


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

%files         -n gem-request-store-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-request-store-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.4.1 -> 1.5.0

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
