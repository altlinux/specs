%define        gemname rb-fsevent

Name:          gem-rb-fsevent
Version:       0.11.1
Release:       alt1
Summary:       Very simple & usable FSEvents API
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/rb-fsevent
Vcs:           https://github.com/thibaudgg/rb-fsevent.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(rb-fsevent) = 0.11.1


%description
FSEvents API with Signals catching (without RubyCocoa)


%package       -n gem-rb-fsevent-doc
Version:       0.11.1
Release:       alt1
Summary:       Very simple & usable FSEvents API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rb-fsevent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rb-fsevent) = 0.11.1

%description   -n gem-rb-fsevent-doc
Very simple & usable FSEvents API documentation files.

FSEvents API with Signals catching (without RubyCocoa)

%description   -n gem-rb-fsevent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rb-fsevent.


%package       -n gem-rb-fsevent-devel
Version:       0.11.1
Release:       alt1
Summary:       Very simple & usable FSEvents API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rb-fsevent
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rb-fsevent) = 0.11.1
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(rake) >= 12.0 gem(rake) < 14

%description   -n gem-rb-fsevent-devel
Very simple & usable FSEvents API development package.

FSEvents API with Signals catching (without RubyCocoa)

%description   -n gem-rb-fsevent-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rb-fsevent.


%prep
%setup
%autopatch

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

%files         -n gem-rb-fsevent-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rb-fsevent-devel
%doc README.md
%ruby_includedir/*


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.11.1-alt1
- ^ 0.11.0 -> 0.11.1

* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
